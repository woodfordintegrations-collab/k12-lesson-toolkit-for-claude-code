"""Document generation for k12-lesson-toolkit.

The renderer is VENDORED from the k12-teacher-skills plugin (Apache-2.0, Anthropic PBC and
Learning Commons), whose per-file copyright headers are retained unmodified. This project
could ground a lesson but not produce one; this closes that gap so the project can emit the
artifacts a teacher actually receives rather than the process files a build leaves behind.

One addition beyond upstream: a `figure` block type. Upstream's block vocabulary has no image
of any kind, which is workable for prose subjects and useless for geometry. See `figure.py`.

Nothing is re-exported here on purpose. `from .rasterize import rasterize` used to sit at the
foot of this file, which rebound the name `rasterize` in this package from the SUBMODULE to
the FUNCTION inside it. After that, `import k12_toolkit.docgen.rasterize` silently handed back
a function, and the module's own attributes (the backend chain, the install hint) were
unreachable through the obvious path. Import from the submodule directly:

    from k12_toolkit.docgen.rasterize import rasterize, viewbox_aspect
"""
