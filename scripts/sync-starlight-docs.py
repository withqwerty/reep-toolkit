#!/usr/bin/env python3
"""Generate Starlight-compatible Markdown from the docs source tree."""

from __future__ import annotations

import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "src" / "content" / "docs"
SOURCE_FILES = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
SOURCE_ROOTS = [ROOT / "docs"]
SKIP_PARTS = {".git", ".history", "node_modules"}
FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"(\[[^\]]+\]\()([^)#]+)(#[^)]+)?(\))")
SOURCE_TO_OUTPUT: dict[Path, Path] = {}


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, text[match.end() :]


def is_publishable(front_matter: dict[str, str]) -> bool:
    if front_matter.get("public_safe") == "false":
        return False
    if front_matter.get("publish") == "false":
        return False
    return True


def title_for(path: Path, body: str) -> str:
    match = H1_RE.search(body)
    if match:
        return match.group(1).strip().replace('"', '\\"')
    return path.stem.replace("-", " ").replace("_", " ").title()


def source_root_relative(path: Path) -> Path:
    return path.relative_to(ROOT)


def generated_relative_for(root_relative: Path) -> Path:
    if root_relative == Path("README.md"):
        return Path("index.md")
    if root_relative == Path("CONTRIBUTING.md"):
        return Path("contributing.md")

    if root_relative.parts[0] != "docs":
        return root_relative.with_name(root_relative.name.lower())

    relative = Path(*root_relative.parts[1:])
    top_level = {
        "INDEX.md": "docs-index.md",
        "SITE.md": "site-model.md",
        "ROADMAP.md": "roadmap.md",
        "EDITORIAL.md": "editorial.md",
        "FRONTMATTER.md": "frontmatter.md",
    }
    if len(relative.parts) == 1 and relative.name in top_level:
        return Path(top_level[relative.name])

    if relative.name == "README.md":
        return relative.parent / "index.md"
    return relative.with_name(relative.name.lstrip("_").lower())


def site_path_for(output_relative: Path) -> str:
    if output_relative.name == "index.md":
        path = output_relative.parent.as_posix()
    else:
        path = output_relative.with_suffix("").as_posix()
    return "/" if not path or path == "." else f"/{path}"


def resolve_generated_target(source: Path, target: str) -> str | None:
    root_relative = source_root_relative(source)
    source_target = (ROOT / root_relative.parent / target).resolve()
    try:
        source_target = source_target.relative_to(ROOT)
    except ValueError:
        return None

    output = SOURCE_TO_OUTPUT.get(source_target)
    if not output:
        return None
    return site_path_for(output)


def rewrite_links(source: Path, body: str) -> str:
    def replace(match: re.Match[str]) -> str:
        prefix, target, anchor, suffix = match.groups()
        if (
            "://" in target
            or target.startswith("/")
            or target.startswith("mailto:")
            or target.startswith("tel:")
        ):
            return match.group(0)
        if target.endswith(".md"):
            target = resolve_generated_target(source, target) or target[:-3]
        return f"{prefix}{target}{anchor or ''}{suffix}"

    return LINK_RE.sub(replace, body)


def render(path: Path, body: str) -> str:
    title = title_for(path, body)
    body_without_title = H1_RE.sub("", body, count=1).lstrip()
    return f'---\ntitle: "{title}"\n---\n\n{rewrite_links(path, body_without_title)}'


def should_skip(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return bool(SKIP_PARTS.intersection(relative.parts))


def iter_sources() -> list[tuple[Path, Path]]:
    sources = [
        (path, generated_relative_for(source_root_relative(path)))
        for path in SOURCE_FILES
        if path.exists()
    ]
    for root in SOURCE_ROOTS:
        for path in sorted(root.rglob("*.md")):
            if should_skip(path):
                continue
            sources.append((path, generated_relative_for(source_root_relative(path))))
    return sources


def main() -> int:
    SOURCE_TO_OUTPUT.clear()
    for source, relative in iter_sources():
        SOURCE_TO_OUTPUT[source_root_relative(source)] = relative

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    written = 0
    skipped = 0
    for source, relative in iter_sources():
        text = source.read_text()
        front_matter, body = parse_front_matter(text)
        if not is_publishable(front_matter):
            skipped += 1
            continue

        destination = OUT_DIR / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(render(source, body))
        written += 1

    print(f"synced {written} docs to {OUT_DIR.relative_to(ROOT)} ({skipped} skipped)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
