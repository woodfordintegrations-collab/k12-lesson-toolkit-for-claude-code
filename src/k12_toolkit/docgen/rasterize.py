#!/usr/bin/env python3
"""SVG to PNG for document embedding, across platforms.

python-docx cannot place an SVG, so every figure is rasterized first. This module tries a
chain of backends and uses the first one present, so the `.docx` path is not tied to macOS:

    cairosvg        python, any platform   -- preferred; honours the viewBox
    rsvg-convert    librsvg CLI            -- honours the viewBox
    resvg           CLI                    -- honours the viewBox
    inkscape        CLI                    -- honours the viewBox
    qlmanage        macOS only             -- last resort, and it does NOT honour the viewBox

QuickLook is last for a reason. It renders into a SQUARE canvas regardless of the source
aspect ratio, so a 160x55 viewBox comes back as 1200x1200 with the drawing small in the
middle. Cropping to the ink corrects it, which is why every backend goes through the same
crop-and-pad afterwards: the correction QuickLook needs is harmless for the ones that don't,
and one shared path means the figures a Linux user gets are the figures this repo shipped.

Three failures here are silent unless checked, so all three are checked:

- Any backend can render a **blank page**. Ink coverage is verified whatever produced it.
- QuickLook returns a **generic document icon** instead of the drawing when it cannot read a
  file, which would put 73 identical useless images into a deliverable. It is a flat glyph, so
  a single-colour image from QuickLook is refused. That clause is scoped to QuickLook on
  purpose: applied to every backend it rejected correct output, because cairosvg draws a plain
  rect on exact pixel boundaries with no antialiasing at all.
- `cairosvg` **installs cleanly without its native cairo library** and only fails when asked
  to render. So the chain probes each backend by rendering, not by importing or locating, and
  falls through on any exception rather than trusting that installed means working.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from collections.abc import Callable
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None

_VIEWBOX = re.compile(r'viewBox\s*=\s*"([-\d.\s]+)"')

INSTALL_HINT = (
    "No working SVG rasterizer was found. Install any one of:\n"
    "    pip install cairosvg          (plus libcairo: `brew install cairo`, "
    "`apt install libcairo2`)\n"
    "    apt install librsvg2-bin      (provides rsvg-convert)\n"
    "    brew install resvg            (or cargo install resvg)\n"
    "    apt/brew install inkscape\n"
    "On macOS, QuickLook (qlmanage) is used automatically and needs no install.\n"
    "The HTML output path inlines SVG directly and needs no rasterizer at all."
)


def viewbox_aspect(svg: Path) -> float:
    """Width divided by height, from the viewBox. 1.0 if it cannot be read."""
    m = _VIEWBOX.search(svg.read_text(encoding="utf-8"))
    if not m:
        return 1.0
    parts = [float(x) for x in m.group(1).split()]
    if len(parts) != 4 or parts[3] == 0:
        return 1.0
    return parts[2] / parts[3]


# --- backends: each renders `svg` to `dest`, or raises ----------------------------------


def _via_cairosvg(svg: Path, dest: Path, size: int) -> None:
    # Imported lazily and inside the try: cairosvg installs cleanly without libcairo and
    # raises only on use, so presence is not availability.
    import cairosvg

    cairosvg.svg2png(url=str(svg), write_to=str(dest), output_width=size)


def _cli_backend(binary: str, argv: Callable[[Path, Path, int], list[str]]):
    def run(svg: Path, dest: Path, size: int) -> None:
        if shutil.which(binary) is None:
            raise FileNotFoundError(binary)
        result = subprocess.run(argv(svg, dest, size), capture_output=True, check=False)
        if not dest.exists() or dest.stat().st_size == 0:
            detail = result.stderr.decode(errors="replace").strip()[:200]
            raise RuntimeError(f"{binary} produced no PNG for {svg.name}: {detail}")

    return run


def _via_qlmanage(svg: Path, dest: Path, size: int) -> None:
    if shutil.which("qlmanage") is None:
        raise FileNotFoundError("qlmanage")
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["qlmanage", "-t", "-s", str(size), "-o", td, str(svg)],
                       capture_output=True, check=False)
        made = list(Path(td).glob("*.png"))
        if not made:
            raise RuntimeError(f"qlmanage produced no PNG for {svg.name}")
        shutil.copy(made[0], dest)


BACKENDS: list[tuple[str, Callable[[Path, Path, int], None]]] = [
    ("cairosvg", _via_cairosvg),
    ("rsvg-convert", _cli_backend(
        "rsvg-convert", lambda s, d, n: ["rsvg-convert", "-w", str(n), "-o", str(d), str(s)])),
    ("resvg", _cli_backend(
        "resvg", lambda s, d, n: ["resvg", "--width", str(n), str(s), str(d)])),
    ("inkscape", _cli_backend(
        "inkscape", lambda s, d, n: ["inkscape", str(s), "--export-type=png",
                                     f"--export-width={n}", f"--export-filename={d}"])),
    ("qlmanage", _via_qlmanage),
]


def available_backend(probe_svg: Path | None = None) -> str | None:
    """Name of the first backend that actually renders, or None. Diagnostic helper."""
    svg = probe_svg
    with tempfile.TemporaryDirectory() as td:
        if svg is None:
            svg = Path(td) / "probe.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 10" width="20" '
                'height="10"><rect x="1" y="1" width="18" height="8" fill="black"/></svg>',
                encoding="utf-8")
        for name, backend in BACKENDS:
            try:
                backend(svg, Path(td) / f"{name}.png", 200)
                return name
            except Exception:
                continue
    return None


def rasterize(svg: Path, out_png: Path, size: int = 2000,
              pad: int = 12) -> tuple[Path, float]:
    """Render `svg` to `out_png`, cropped to its ink. Returns (path, viewBox aspect)."""
    aspect = viewbox_aspect(svg)
    with tempfile.TemporaryDirectory() as td:
        raw = Path(td) / "raw.png"
        failures: list[str] = []
        for name, backend in BACKENDS:
            # Clear first: a half-written PNG left by a failed backend would otherwise be
            # read as the next backend's success.
            raw.unlink(missing_ok=True)
            try:
                backend(svg, raw, size)
            except Exception as exc:
                failures.append(f"{name}: {type(exc).__name__}: {str(exc)[:120]}")
                continue
            if raw.exists() and raw.stat().st_size:
                break
            failures.append(f"{name}: wrote nothing")
        else:
            raise RuntimeError(
                f"could not rasterize {svg.name}.\n" + "\n".join(f"  {f}" for f in failures)
                + "\n\n" + INSTALL_HINT
            )

        if Image is None:
            out_png.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(raw, out_png)
            return out_png, aspect

        im = Image.open(raw).convert("RGB")

        # Two different failures, and only one of them is universal.
        #
        # Universal: a blank or near-blank page. Any backend can produce one and it must never
        # reach a document, so ink coverage is checked whatever rendered it.
        #
        # QuickLook-only: a GENERIC DOCUMENT ICON substituted for a file it cannot read. That
        # is a flat glyph, so it was detected by demanding ink in more than one colour --
        # which works because QuickLook's real output is antialiased. Applying that clause to
        # every backend was wrong: cairosvg renders a plain rect on exact pixel boundaries
        # with no antialiasing at all, giving one ink colour and a perfectly good figure. The
        # clause is therefore scoped to the backend whose failure mode it describes.
        colours = im.getcolors(maxcolors=1_000_000) or []
        non_white = [n for n, c in colours if c != (255, 255, 255)]
        if sum(non_white) < 200:
            raise RuntimeError(
                f"{svg.name}: rasterized output is blank or nearly blank (backend: {name}). "
                f"Do not ship this."
            )
        if name == "qlmanage" and len(non_white) < 2:
            raise RuntimeError(
                f"{svg.name}: QuickLook returned a flat single-colour image, which is what it "
                f"produces when it substitutes a generic document icon for a file it cannot "
                f"read. Do not ship this."
            )

        # Crop to ink, then re-pad evenly so figures sit consistently on the page. Required to
        # undo QuickLook's square canvas; a no-op for backends that honour the viewBox.
        bg = Image.new("RGB", im.size, (255, 255, 255))
        from PIL import ImageChops
        bbox = ImageChops.difference(im, bg).getbbox()
        if bbox:
            im = im.crop(bbox)
        canvas = Image.new("RGB", (im.width + 2 * pad, im.height + 2 * pad), (255, 255, 255))
        canvas.paste(im, (pad, pad))
        out_png.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(out_png, "PNG")
        return out_png, aspect


if __name__ == "__main__":  # pragma: no cover
    found = available_backend()
    print(f"rasterizer backend: {found}" if found
          else f"no rasterizer available.\n\n{INSTALL_HINT}")
