---
doc_type: project_overview
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: contribution
stance: descriptive
contribution_model: evidence_required
---

# Contributing

Reep Toolkit is intended to power a public guide site directly from the docs.
Contributions improve one of four surfaces:

- provider reference knowledge,
- Reep-informed practice guidance,
- runnable examples,
- or machine-readable metadata that makes the docs easier to search.

## Contribution Lanes

| Lane               | Good contribution                                                                     | Review bar                                                        |
| ------------------ | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Provider reference | Add or correct provider fields, ID namespaces, bridge paths, access notes, or quirks. | Reproducible evidence required.                                   |
| Practice guide     | Improve doctrine about matching, minting, bridging, duplicates, or maintenance.       | Maintainer review; explain the failure mode and tradeoff.         |
| Example            | Add a small public-safe example.                                                      | Must be runnable or clearly narrative, with no private data.      |
| Schema             | Improve reference schema or metadata taxonomy.                                        | Must remain optional and not overfit private Reep infrastructure. |

## Evidence Standard

Provider facts need reproducible evidence:

- public provider documentation,
- a public dataset row,
- a public API response shape that can be reproduced,
- a public open-source library or mapping dataset,
- a maintainer-approved redacted example for paid/private providers.

Do not cite private file paths, local snapshots, credentials, or production runbooks as
public evidence.

## Writing Standard

- Use British English.
- Explain the matching consequence of each fact.
- Prefer concrete failure modes over vague warnings.
- Keep provider facts in provider pages.
- Keep Reep-style recommendations in practice guides.
- Do not publish private Reep implementation paths.
- Write as if the reader is deciding whether to ingest a provider tomorrow.
- Avoid filler such as "useful", "interesting", or "flexible" unless the sentence
  explains why.

## Front Matter

Every Markdown file must have front matter. At minimum:

```yaml
---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: providers
stance: descriptive
contribution_model: evidence_required
---
```

Use `docs/FRONTMATTER.md` for the full taxonomy.

## Public-Safe Rewrite Pattern

Instead of:

> This private command reads this local paid snapshot and writes production mappings.

Write:

> Capture a snapshot, load provider-shaped records, run a matcher that emits candidate
> bridges with source version and method, then promote only matches that pass the
> register's confidence and ambiguity policy.
