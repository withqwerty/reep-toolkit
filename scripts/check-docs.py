#!/usr/bin/env python3
"""Validate guide-site Markdown metadata and local links."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FRONT_MATTER_KEYS = (
    "doc_type",
    "content_lane",
    "status",
    "public_safe",
    "last_verified",
    "site_section",
    "stance",
    "contribution_model",
)
EXAMPLE_FRONT_MATTER_KEYS = ("failure_mode", "decision", "search_tags")
SKIP_PARTS = {".git", ".history", "node_modules"}
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def should_skip(path: Path) -> bool:
    return bool(SKIP_PARTS.intersection(path.parts))


def split_front_matter(path: Path, text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing front matter")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{path}: unterminated front matter")

    front_matter: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        front_matter[key.strip()] = value.strip()

    return front_matter, text[end + 5 :]


def validate_front_matter(path: Path, front_matter: dict[str, str]) -> list[str]:
    errors: list[str] = []
    for key in REQUIRED_FRONT_MATTER_KEYS:
        if key not in front_matter:
            errors.append(f"{path}: missing front matter key `{key}`")

    if (
        path.parent == Path("docs/examples")
        and path.name not in {"README.md", "CATALOGUE.md"}
    ):
        for key in EXAMPLE_FRONT_MATTER_KEYS:
            if key not in front_matter:
                errors.append(f"{path}: missing example front matter key `{key}`")

    if front_matter.get("public_safe") not in {"true", "false"}:
        errors.append(f"{path}: `public_safe` must be true or false")

    return errors


def validate_local_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for match in MARKDOWN_LINK_RE.finditer(text):
        target = match.group(1)
        if (
            "://" in target
            or target.startswith("#")
            or target.startswith("mailto:")
            or target.startswith("tel:")
        ):
            continue

        target_path = target.split("#", 1)[0]
        if not target_path:
            continue

        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path}: local link escapes repo: {target}")
            continue

        if not resolved.exists():
            errors.append(f"{path}: broken local link: {target}")

    return errors


def main() -> int:
    errors: list[str] = []
    markdown_files = [
        path
        for path in sorted(ROOT.rglob("*.md"))
        if not should_skip(path.relative_to(ROOT))
    ]

    for path in markdown_files:
        relative_path = path.relative_to(ROOT)
        text = path.read_text()
        try:
            front_matter, _body = split_front_matter(relative_path, text)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        errors.extend(validate_front_matter(relative_path, front_matter))
        errors.extend(validate_local_links(relative_path, text))

    if errors:
        print("\n".join(errors))
        return 1

    print(f"docs OK ({len(markdown_files)} markdown files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
