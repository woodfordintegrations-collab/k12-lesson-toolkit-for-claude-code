"""The rasterizer backend chain: fallthrough, and the two failures that are silent by default.

Figures reach a `.docx` as PNG, and for a long time that meant macOS only. The chain now tries
several backends, which introduces its own hazard: "installed" is not "working". `cairosvg`
pip-installs perfectly happily without its native cairo library and raises only when asked to
render, so a chain that probed by import would pick it and then fail on the first figure.
Every backend is therefore probed by *rendering*, and these tests pin that.

The other silent failure is a blank image. QuickLook substitutes a generic document icon for a
file it cannot read, which once meant a deliverable could receive 73 identical useless
pictures without anything raising. The ink check guards every backend, not just QuickLook.
"""

from __future__ import annotations

from pathlib import Path

import pytest

# NOT `from k12_toolkit.docgen import rasterize`: the package re-exports a *function* of that
# name, which shadows this submodule and yields a function object instead.
import k12_toolkit.docgen.rasterize as R

# Every assertion below inspects pixels. Without Pillow these would not fail, they would
# assert nothing, so the module skips rather than passing vacuously.
pytest.importorskip("PIL", reason="figure tests need Pillow: pip install '.[docgen]'")

SQUARE = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 55" width="160" '
          'height="55"><rect x="4" y="4" width="152" height="47" fill="black"/></svg>')


@pytest.fixture
def svg(tmp_path: Path) -> Path:
    p = tmp_path / "fig.svg"
    p.write_text(SQUARE, encoding="utf-8")
    return p


def _png_writer(antialiased: bool = True):
    """A fake backend writing a 30x10 ink block inside a 40x20 canvas."""
    def write(svg: Path, dest: Path, size: int) -> None:
        from PIL import Image
        im = Image.new("RGB", (40, 20), "white")
        for x in range(5, 35):
            for y in range(5, 15):
                edge = antialiased and (x in (5, 34) or y in (5, 14))
                im.putpixel((x, y), (128, 128, 128) if edge else (0, 0, 0))
        im.save(dest, "PNG")
    return write


def _blank_writer(svg: Path, dest: Path, size: int) -> None:
    from PIL import Image
    Image.new("RGB", (40, 20), "white").save(dest, "PNG")


def _raiser(svg: Path, dest: Path, size: int) -> None:
    raise RuntimeError("no native library")


def _writes_nothing(svg: Path, dest: Path, size: int) -> None:
    return None


def test_viewbox_aspect_is_read_from_the_source(svg: Path, tmp_path: Path) -> None:
    assert R.viewbox_aspect(svg) == pytest.approx(160 / 55)
    bare = tmp_path / "bare.svg"
    bare.write_text('<svg xmlns="http://www.w3.org/2000/svg"></svg>', encoding="utf-8")
    assert R.viewbox_aspect(bare) == 1.0


def test_a_backend_that_raises_falls_through_to_the_next(
    svg: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """cairosvg-without-libcairo is exactly this shape: importable, then it raises."""
    monkeypatch.setattr(R, "BACKENDS", [("broken", _raiser), ("good", _png_writer())])
    out, aspect = R.rasterize(svg, tmp_path / "out.png")
    assert out.exists()
    assert aspect == pytest.approx(160 / 55), "aspect comes from the viewBox, not the canvas"


def test_a_backend_that_writes_nothing_falls_through(
    svg: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(R, "BACKENDS", [("silent", _writes_nothing), ("good", _png_writer())])
    assert R.rasterize(svg, tmp_path / "out.png")[0].exists()


def test_a_failed_backends_leftover_file_is_not_read_as_the_next_ones_success(
    svg: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Without the clear-before-attempt, a partial write would be picked up as a good render."""
    def writes_then_raises(s: Path, dest: Path, size: int) -> None:
        _png_writer()(s, dest, size)
        raise RuntimeError("died after writing")

    monkeypatch.setattr(R, "BACKENDS", [("half", writes_then_raises), ("silent", _writes_nothing)])
    with pytest.raises(RuntimeError) as excinfo:
        R.rasterize(svg, tmp_path / "out.png")
    assert "could not rasterize" in str(excinfo.value)


def test_a_blank_render_raises_rather_than_shipping(
    svg: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(R, "BACKENDS", [("blank", _blank_writer)])
    with pytest.raises(RuntimeError, match="blank or nearly blank"):
        R.rasterize(svg, tmp_path / "out.png")


def test_a_crisp_single_colour_render_is_accepted_from_a_real_renderer(
    svg: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """cairosvg draws a rect on exact pixel boundaries with no antialiasing.

    The ink guard used to demand more than one non-white colour for every backend, which
    rejected exactly this: a correct, crisp, two-colour figure. That clause describes
    QuickLook's generic-icon substitution and now applies only there.
    """
    monkeypatch.setattr(R, "BACKENDS", [("cairosvg", _png_writer(antialiased=False))])
    assert R.rasterize(svg, tmp_path / "out.png")[0].exists()


def test_the_same_flat_image_from_quicklook_is_rejected(
    svg: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Same pixels, different backend, opposite verdict -- because the failure is QuickLook's."""
    monkeypatch.setattr(R, "BACKENDS", [("qlmanage", _png_writer(antialiased=False))])
    with pytest.raises(RuntimeError, match="generic document icon"):
        R.rasterize(svg, tmp_path / "out.png")


def test_exhausting_every_backend_reports_each_failure_and_how_to_fix_it(
    svg: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(R, "BACKENDS", [("one", _raiser), ("two", _writes_nothing)])
    with pytest.raises(RuntimeError) as excinfo:
        R.rasterize(svg, tmp_path / "out.png")
    message = str(excinfo.value)
    assert "one:" in message and "two:" in message, "each backend's failure must be named"
    assert "pip install cairosvg" in message and "librsvg2-bin" in message


def test_output_is_cropped_to_the_ink_and_padded(
    svg: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Undoes QuickLook's square canvas; harmless for backends that honour the viewBox."""
    from PIL import Image
    monkeypatch.setattr(R, "BACKENDS", [("good", _png_writer())])
    out, _ = R.rasterize(svg, tmp_path / "out.png", pad=3)
    # ink was a 30x10 block inside a 40x20 canvas -> cropped to 30x10, plus 3px padding a side
    assert Image.open(out).size == (36, 16)


def test_this_machine_has_a_working_backend_and_it_renders_a_real_figure(
    svg: Path, tmp_path: Path
) -> None:
    """Not a mock. Whatever backend this platform actually provides must produce real ink."""
    from PIL import Image
    backend = R.available_backend()
    assert backend is not None, f"no rasterizer on this machine.\n{R.INSTALL_HINT}"
    out, aspect = R.rasterize(svg, tmp_path / "real.png")
    im = Image.open(out).convert("RGB")
    dark = sum(n for n, c in (im.getcolors(maxcolors=10**6) or []) if sum(c) < 400)
    assert dark > 100, f"backend {backend} produced almost no ink"
    assert aspect == pytest.approx(160 / 55)
