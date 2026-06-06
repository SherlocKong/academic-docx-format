#!/usr/bin/env python3
"""Read-only environment preflight for academic DOCX formatting work."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import sys
from pathlib import Path


def locate_docx_skill() -> str | None:
    candidates = []
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    candidates.extend([codex_home / "skills" / "docx", codex_home / "skills" / "doc"])
    for path in candidates:
        if (path / "SKILL.md").is_file():
            return str(path)
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    modules = {name: bool(importlib.util.find_spec(name)) for name in ("docx", "lxml")}
    tools = {
        name: shutil.which(name)
        for name in ("python3", "uv", "soffice", "libreoffice", "pdftoppm", "pdfinfo")
    }
    report = {
        "ready_for_read_only_survey": bool(locate_docx_skill() and modules["docx"] and modules["lxml"]),
        "ready_for_render_validation": bool(
            (tools["soffice"] or tools["libreoffice"]) and tools["pdftoppm"]
        ),
        "docx_skill_path": locate_docx_skill(),
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0],
        "python_modules": modules,
        "tools": tools,
        "dedicated_environment_recommended": not all(modules.values()),
    }
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for key, value in report.items():
            print(f"{key}: {value}")
    return 0 if report["ready_for_read_only_survey"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

