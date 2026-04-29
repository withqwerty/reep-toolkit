#!/usr/bin/env python3
"""Generate the examples catalogue from Markdown front matter."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "docs" / "examples"
OUTPUT = EXAMPLES / "CATALOGUE.md"
SKIP = {"README.md", "CATALOGUE.md"}


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    front_matter: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        front_matter[key.strip()] = value.strip()
    return front_matter, text[end + 5 :]


def title_from_body(path: Path, body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def main() -> int:
    rows: list[dict[str, str]] = []
    for path in sorted(EXAMPLES.glob("*.md")):
        if path.name in SKIP:
            continue
        front_matter, body = split_front_matter(path.read_text())
        rows.append(
            {
                "title": title_from_body(path, body),
                "path": path.name,
                "provider": front_matter.get("provider", ""),
                "entity_types": front_matter.get("entity_types", ""),
                "failure_mode": front_matter.get("failure_mode", ""),
                "decision": front_matter.get("decision", ""),
                "tags": front_matter.get("search_tags", ""),
            }
        )

    lines = [
        "---",
        "doc_type: examples_catalogue",
        "content_lane: example",
        "status: generated",
        "public_safe: true",
        "last_verified: 2026-04-29",
        "site_section: examples",
        "stance: descriptive",
        "contribution_model: generated",
        "---",
        "",
        "# Examples Catalogue",
        "",
        "This catalogue is generated from example front matter.",
        "",
        "| Example | Provider | Entity types | Failure mode | Decision | Tags |",
        "| ------- | -------- | ------------ | ------------ | -------- | ---- |",
    ]

    for row in rows:
        lines.append(
            "| "
            f"[{row['title']}]({row['path']}) | "
            f"{row['provider']} | "
            f"`{row['entity_types']}` | "
            f"`{row['failure_mode']}` | "
            f"`{row['decision']}` | "
            f"`{row['tags']}` |"
        )

    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(rows)} examples)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
