---
doc_type: contributor_guide
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: contributors
stance: directive
contribution_model: maintainer_doctrine
---

# AGENTS.md

This repo is public guide-site source material for football identity work. Treat it as a
documentation and examples repository, not as a mirror of private Reep operations.

## Read First

Before editing, read:

- [README.md](README.md) for the overview and table of contents.
- [docs/INDEX.md](docs/INDEX.md) for the documentation map.
- [docs/EDITORIAL.md](docs/EDITORIAL.md) for the writing standard.
- [docs/world-model/public-private-boundary.md](docs/world-model/public-private-boundary.md)
  before adding anything derived from private Reep work.
- [docs/FRONTMATTER.md](docs/FRONTMATTER.md) before adding or moving Markdown files.

## Public Boundary

Share reusable judgement:

- provider world models,
- field semantics,
- bridge and alias behaviour,
- matching thresholds,
- duplicate-resolution doctrine,
- snapshot and review patterns,
- public-safe examples with invented IDs.

Do not share:

- private repository paths,
- private script names as instructions,
- credentials or paid snapshot details,
- private Linear workflow details,
- unreleased operational runbooks,
- production counts or IDs unless already public.

## Writing Standard

Write for someone who is about to ingest a provider, review matches, or maintain a
register. Prefer concrete cases over abstract principles.

Good pages usually include:

- the entity type,
- the provider or source shape,
- the proposed match or write,
- the evidence,
- the decision,
- what gets written, reviewed, deferred, or rejected,
- the doctrine demonstrated.

Avoid pages that only say "run this tool" or "look at this private file". This toolkit
should explain the decision model, not expose private implementation details.

## Examples

Examples should be small, public-safe, and explicit. Use invented register IDs and
provider IDs unless the identifiers are already public and necessary for the lesson.

Good example sources:

- provider-card gotchas,
- bridge conflicts,
- duplicate merge reviews,
- type or namespace collisions,
- snapshot drift,
- weak-match review queues,
- match or season model mismatches.

Every example should make the outcome visible: auto-write, review, defer, reject,
tombstone, redirect, or preserve as conflict evidence.

## Checks

Run the repo checks before declaring docs work done:

```bash
npm run check
```

Use `npm run format` before committing if formatting has changed.

The checks validate formatting, required front matter, local Markdown links, example
search metadata, and obvious public-boundary leaks such as private absolute paths or
credential literals.
