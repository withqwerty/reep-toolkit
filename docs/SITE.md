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

This folder is source content for a guide website. Front matter drives validation,
catalogues, and future browsing surfaces; the current site uses an explicit Starlight
sidebar plus full-text search.

## V1 Site Decision

Build the first website as a static documentation site over this repository. The docs
are the product: contributors edit Markdown, CI validates metadata and links, and the
site renders the same files without a separate CMS.

The current implementation uses Astro Starlight. Source Markdown remains in `docs/`,
top-level contributor files, and `README.md`; generated Starlight content is written to
`src/content/docs/` by `npm run site:sync` and is not edited by hand.

Current V1 shape:

| Area              | Treatment                                                                    |
| ----------------- | ---------------------------------------------------------------------------- |
| Home              | Use [README.md](../README.md) as the overview and route map.                 |
| Navigation        | Explicit Starlight sidebar in `astro.config.mjs`, grouped by task area.      |
| Provider pages    | Reference pages with evidence-backed facts, safe-use matrices, and gotchas.  |
| Practice guides   | Opinionated doctrine pages, maintained more tightly than provider reference. |
| Examples          | First-class pages, browsable by failure mode and decision.                   |
| Search            | Starlight full-text search over generated Markdown pages.                    |
| Contribution flow | Pull request edits to Markdown; generated catalogue committed with changes.  |

Do not make the first site a marketing page. The first screen should help a reader pick
a task: understand a provider, ingest a provider, review a match, resolve a duplicate,
or maintain a register.

## V1 Navigation

Use the explicit task-first sidebar in `astro.config.mjs` as the current navigation
authority:

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

## Search Metadata

Source pages keep metadata such as provider, entity types, failure mode, decision,
search tags, content lane, access tier, authority role, bridge providers, matching
fields, confidence floor, status, and stance. Today that metadata is validated and used
for generated catalogues. A future custom browser can expose it as filters.

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
regenerated before publishing. If the generated catalogue is stale, the committed docs
view will drift even though the source pages still build.
