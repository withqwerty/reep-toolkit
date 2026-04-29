#!/usr/bin/env python3
"""Fail on obvious private-path, credential, and operational leakage."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".history", "node_modules"}
CHECK_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".json", ".sql"}

FORBIDDEN_PATTERNS = {
    "absolute user path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "absolute external-drive path": re.compile(r"/Volumes/[A-Za-z0-9._-]+/"),
    "home credential path": re.compile(r"~/(?:\\.env|\\.aws|\\.config|\\.ssh)"),
    "private env file": re.compile(r"\\.env(?:\\b|/)"),
    "api key literal": re.compile(r"(?i)(api[_-]?key|secret|token)\\s*[:=]\\s*['\\\"][^'\\\"]+['\\\"]"),
    "private pending script instruction": re.compile(r"scripts/pending/"),
    "private d1 operation": re.compile(r"\\bwrangler\\s+d1\\s+execute\\b"),
}


def should_skip(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return (
        bool(SKIP_PARTS.intersection(relative.parts))
        or path.suffix not in CHECK_SUFFIXES
        or relative == Path("scripts/check-public-boundary.py")
    )


def main() -> int:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or should_skip(path):
            continue
        text = path.read_text(errors="ignore")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            for match in pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                relative = path.relative_to(ROOT)
                errors.append(f"{relative}:{line_no}: public-boundary leak: {label}")

    if errors:
        print("\n".join(errors))
        return 1

    print("public boundary OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
