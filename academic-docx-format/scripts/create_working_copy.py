#!/usr/bin/env python3
"""Create a timestamped DOCX working copy without modifying the source."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slugify(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value.strip()).strip("-").lower()
    return value or "format-work"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--task", required=True, help="Short task label used in the filename.")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--timestamp", help="Override timestamp as YYYYMMDD_HHMMSS.")
    args = parser.parse_args()

    source = args.source.resolve()
    if source.suffix.lower() != ".docx" or not source.is_file():
        parser.error("source must be an existing .docx file")
    timestamp = args.timestamp or datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = (args.output_dir or source.parent).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{source.stem}_{timestamp}_{slugify(args.task)}{source.suffix}"
    if output.exists():
        parser.error(f"refusing to overwrite existing output: {output}")

    source_hash = sha256(source)
    shutil.copy2(source, output)
    output_hash = sha256(output)
    if source_hash != output_hash:
        output.unlink(missing_ok=True)
        raise RuntimeError("copy hash mismatch; removed output")

    print(
        json.dumps(
            {
                "source": str(source),
                "source_sha256": source_hash,
                "working_copy": str(output),
                "working_copy_sha256": output_hash,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

