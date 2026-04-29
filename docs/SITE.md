---
doc_type: project_overview
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: contribution
stance: descriptive
contribution_model: maintainer_doctrine
---

# Guide Site Model

This folder is source content for a guide website. A site generator can build
navigation, filters, and search facets from front matter without hard-coding every page.

## V1 Site Decision

Build the first website as a static documentation site over this repository. The docs
are the product: contributors edit Markdown, CI validates metadata and links, and the
site renders the same files without a separate CMS.

Recommended V1 shape:

| Area              | Treatment                                                                    |
| ----------------- | ---------------------------------------------------------------------------- |
| Home              | Use [README.md](../README.md) as the overview and route map.                 |
| Navigation        | Generate from `site_section`, folder order, and [docs/INDEX.md](INDEX.md).   |
| Provider pages    | Reference pages with evidence-backed facts, safe-use matrices, and gotchas.  |
| Practice guides   | Opinionated doctrine pages, maintained more tightly than provider reference. |
| Examples          | First-class pages, browsable by failure mode and decision.                   |
| Search            | Faceted search over front matter plus full-text Markdown.                    |
| Contribution flow | Pull request edits to Markdown; generated catalogue committed with changes.  |

Do not make the first site a marketing page. The first screen should help a reader pick
a task: understand a provider, ingest a provider, review a match, resolve a duplicate,
or maintain a register.

## V1 Navigation

Use a task-first navigation:

1. Start here
2. World model
3. Provider reference
4. Practice guides
5. Worked examples
6. Pipeline patterns
7. Contributing

Examples should appear in search results beside guides. A reader searching for
`name-only`, `duplicate`, `stage`, `fuzzy`, or `mirror` should see the example and the
doctrine page together.

## Site Sections

| `site_section` | Purpose                                                          |
| -------------- | ---------------------------------------------------------------- |
| `home`         | Project overview, roadmap, index.                                |
| `providers`    | Provider reference pages and source taxonomy.                    |
| `guides`       | Opinionated Reep-style practice guides.                          |
| `world-model`  | Conceptual model for entities, IDs, seasons, matches, authority. |
| `pipelines`    | Pipeline architecture and implementation patterns.               |
| `examples`     | Narrative or runnable examples.                                  |
| `contribution` | Contributor guidance and metadata taxonomy.                      |

## Search Facets

The site exposes:

- provider,
- entity types,
- failure mode,
- decision,
- search tags,
- content lane,
- access tier,
- authority role,
- bridge providers,
- matching fields,
- confidence floor,
- status,
- stance.

## Page Types

### Provider Reference

Provider pages answer:

- What does this provider identify?
- Which IDs are stable?
- Which fields are useful for matching?
- What bridge paths exist?
- What are the source-specific traps?
- What should be reviewed before writing?

### Practice Guides

Practice guides answer:

- What does Reep recommend?
- What failure mode does this prevent?
- What evidence is required?
- When should a maintainer defer or review?
- What should be preserved for audit?

### Examples

Examples are small, public-safe, and reproducible. They show one implementation without
implying that private Reep infrastructure is required.

## Publication Rule

Pages with `public_safe: false` must not be published. Draft pages can be published if
clearly marked as draft.

Generated files such as [examples/CATALOGUE.md](examples/CATALOGUE.md) should be
regenerated before publishing. If the generated catalogue is stale, the site search will
still work from front matter, but the committed docs view will drift.
