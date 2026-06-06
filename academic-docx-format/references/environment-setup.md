# DOCX Environment Setup

Run `../scripts/preflight.py --json` before reading or modifying a project DOCX.

## Required capabilities

- Installed and readable `docx` skill
- Python with `python-docx` and `lxml`
- LibreOffice/soffice or another approved Word renderer
- Poppler tools such as `pdftoppm` and `pdfinfo` for visual/PDF checks
- Fonts required by the target template

## Dedicated environment

Prefer a dedicated environment when dependencies are missing or conflict with the project:

```bash
python3 -m venv ~/.codex/skill-envs/academic-docx-format
~/.codex/skill-envs/academic-docx-format/bin/python -m pip install python-docx lxml pyyaml
```

Use the dedicated interpreter for this skill's Python helpers:

```bash
~/.codex/skill-envs/academic-docx-format/bin/python \
  ~/.codex/skills/academic-docx-format/scripts/preflight.py --json
```

Record the actual interpreter, renderer paths, package versions, and last successful preflight in the project's `AGENTS.md`. Do not alter or replace a user's project environment merely to satisfy this skill.

## Failure behavior

If reading dependencies are unavailable, stop before surveying the DOCX. If rendering dependencies are unavailable, do not claim visual validation; help configure them or explicitly leave visual QA open.
