---
doc_type: project_overview
content_lane: reference
status: draft
public_safe: false
publish: false
last_verified: 2026-05-13
site_section: internal
stance: descriptive
contribution_model: maintainer_doctrine
---

# Site Implementation Plan

This is the proposed target shape for a combined public Reep Toolkit site that absorbs
the useful guide, provider, schema, and reference-code material from `reep-scripts`
without presenting it as a production package.

This document is an internal implementation plan, not public site content. Split any
stable contributor-facing guidance out into publishable pages before launch.

There are no existing public consumers to preserve. Treat this as a clean consolidation,
not a backwards-compatible package migration.

## Product Definition

Reep Toolkit is a public football identity-resolution handbook with reference code. The
docs are the product. The code is illustrative: small examples, templates, fixtures, and
schemas that readers can copy, adapt, or use to test their own thinking.

The site should answer five reader questions:

1. How should a football entity register model teams, people, competitions, seasons,
   matches, bridges, aliases, provenance, and redirects?
2. What does each provider identify, and which fields are safe identity evidence?
3. How do I turn provider-shaped records into candidates, decisions, review residue, and
   writes?
4. What recurring failure modes should I expect?
5. What reference scripts or schemas can I copy into my own project?

## Non-Goals

- It is not a maintained Python package with semver or import-stability guarantees.
- It is not the Reep Register or Reep Next control plane.
- It is not a private partner operating manual.
- It is not a data-acquisition manual. Public examples should assume readers already
  have provider exports, licensed API responses, open datasets, or public fixtures they
  are allowed to use.
- It is not a guide to scraping or bypassing provider access controls. Provider pages
  can describe accepted input shapes and link to official/source documentation; they
  should not teach acquisition mechanics.

## Audience

| Audience                                    | Need                                                                         | Primary Site Route                                |
| ------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------- |
| Club or analyst building an internal ID map | Understand provider IDs, bridge confidence, and false-positive traps.        | Providers, guides, examples.                      |
| Open-data contributor                       | Add a provider fact, quirk, or example with evidence.                        | Providers, contribution docs, examples.           |
| Developer adapting a script                 | Copy a small reference pattern into their own stack.                         | Reference scripts, schemas, templates.            |
| Reep user evaluating decisions              | Understand why Reep models an entity or bridge conservatively.               | World model, casebook examples, source authority. |
| Partner prospect                            | Understand the public methodology before asking for deeper private material. | Start here, source authority, worked examples.    |

## Repository Boundary

| Surface                    | Target Role                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `reep-toolkit`             | Public docs site, provider catalogue, worked examples, schemas, and reference scripts.                                                  |
| `reep-scripts`             | Source material to mine, migrate, and then archive. It should not remain a parallel package/docs surface.                               |
| `football-docs`            | Source/provenance research surface during migration. It should not remain a second public provider authority after toolkit launch.      |
| `reep-matching-logic-pack` | Private partner-safe operating model with deeper source-authority playbooks, review behaviour, validation loops, and sample write sets. |
| `reep-register-next`       | Private execution/control plane for Reep's actual register generation.                                                                  |

For launch, `reep-toolkit` owns the public provider reference. `football-docs` can
remain a local/operator research backend or MCP source, but any public provider claim
must either be migrated into the toolkit with evidence or linked as an explicit source
note. Do not run two public provider-doc authorities.

## Site Engine Decision

Use a Git-backed static docs site. Keep Markdown as source and keep GitHub pull requests
as the contribution path.

Decision: **Astro Starlight**.

Why:

- Markdown/MDX content is first-class.
- Front matter can drive provider cards, examples, search facets, and generated
  catalogues.
- The site can host custom pages later: provider matrices, evidence-schema viewers,
  example browsers, JSON-schema previews, and decision filters.
- It avoids locking the content model to a hosted docs product before we know the
  contribution and search shapes.

Hosted docs products remain useful for external preview or editing experiments, but the
long-term source of truth should stay in this repository and the site should be
reproducible from CI.

## Target Information Architecture

```text
docs/
  start-here/
    overview.md
    how-to-use-the-toolkit.md
    public-private-boundary.md

  register-basics/
    entities.md
    ids-bridges-and-aliases.md
    provenance-and-lineage.md
    confidence-and-review.md
    tombstones-and-redirects.md
    seasons-stages-and-matches.md
    relationships-and-edges.md

  providers/
    README.md
    CATALOGUE.md
    _template.md
    sources.md
    ecosystem-notes.md
    transfermarkt.md
    opta.md
    statsbomb.md
    whoscored.md
    soccerdonna.md
    ...

  data-models/
    README.md
    provider-extracts.md
    opta-substrate-model.md
    transfermarkt-identity-surfaces.md
    statsbomb-open-data-model.md
    wikidata-external-id-model.md

  guides/
    before-you-ingest.md
    choosing-source-authority.md
    bridging-provider-ids.md
    relationship-constrained-matching.md
    minting-and-entity-creation.md
    duplicate-resolution.md
    register-maintenance.md

  templates/
    README.md
    candidate-evidence-schema.md
    match-bridge-template.md
    relationship-constrained-template.md
    split-season-stage-template.md
    duplicate-resolution-template.md
    review-residue-template.md

  examples/
    CATALOGUE.md
    provider-duplicate.md
    fixture-date-drift.md
    playoff-stage-modelling.md
    cross-role-player-coach.md
    supplier-id-collision.md
    local-mirror-staleness.md
    ...

  reference-scripts/
    README.md
    python/
      normalise_names.py
      match_candidates.py
      build_evidence_json.py
      validate_bridge_conflicts.py
      split_stage_candidates.py
    fixtures/
      README.md
      providers/
      expected/

  schemas/
    README.md
    candidate.schema.json
    evidence.schema.json
    provider-record.schema.json
    reference-register.sql

  contributing/
    README.md
    editorial-standard.md
    frontmatter.md
    evidence-requirements.md
    provider-card-template.md
```

The current repo should move toward this structure directly. Because there are no
existing consumers, prefer a clean information architecture over compatibility folders.
Use redirects or archive notes only when they help humans understand where material
moved.

## Content Migration From `reep-scripts`

`reep-scripts` contains two kinds of useful material:

1. Provider knowledge that belongs in `docs/providers/`.
2. Library mechanics that should become reference examples, templates, schemas, or
   fixture-backed snippets.

### Migration Manifest

Before files move, maintain [MIGRATION-MANIFEST.md](MIGRATION-MANIFEST.md) so it
inventories every relevant `reep-scripts` source:

- all Markdown docs;
- provider docs and catalogues;
- fixtures;
- schemas and migrations;
- selected modules under `reep_scripts/`;
- tests that may become example validation;
- package/build metadata that should be dropped.

Each row should include:

| Field                | Meaning                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------- |
| `source_path`        | Original path in `reep-scripts`.                                                         |
| `destination`        | Target path in `reep-toolkit`, or `none`.                                                |
| `disposition`        | `migrate`, `rewrite`, `drop`, `archive`, or `source_only`.                               |
| `public_safe_review` | `pending`, `pass`, or `fail`.                                                            |
| `evidence_status`    | `checked`, `needs_source`, `synthetic_only`, or `not_applicable`.                        |
| `verification`       | Required check: link check, schema validation, fixture smoke test, docs review, or none. |

`reep-scripts` cannot be archived until every manifest row is resolved.

### Promote To Provider Docs

Move and review:

- all provider cards that exist only in `reep-scripts`;
- the fuller provider catalogue;
- ecosystem notes;
- source taxonomy details;
- access notes rewritten as "accepted input/source shape" guidance, not collection
  instructions;
- bridge tables, matching fields, quirks, and known issues.

Do not copy blindly. Each promoted page needs:

- front matter matching this repo's taxonomy;
- public-safe wording;
- checked references or reproducible evidence;
- current source-role language;
- no package-specific import examples unless they are in a reference-script section.
- no live-fetch, scrape, or provider-access instructions beyond official links and
  source-shape descriptions.

### Promote To Templates And Reference Scripts

Move concepts, not package promises:

- `evidence.py` becomes a documented evidence/candidate schema plus a compact reference
  implementation.
- `templates/recipes.py` becomes small template pages and example functions.
- loader and matcher examples become fixture-backed reference scripts.
- tests become fixture-backed example validation, not public API compatibility
  guarantees.

Module-level disposition:

| Source family                                  | Disposition                                                                             |
| ---------------------------------------------- | --------------------------------------------------------------------------------------- |
| `reep_scripts/evidence.py`                     | Rewrite as JSON schemas, fixture examples, and a compact reference implementation.      |
| `reep_scripts/templates/`                      | Rewrite as non-mutating template examples over committed fixtures.                      |
| `reep_scripts/standardise/`                    | Migrate small pure helpers as reference snippets when broadly useful.                   |
| `reep_scripts/loaders/`                        | Rewrite only as fixture readers for documented input shapes; no live-provider fetchers. |
| `reep_scripts/matchers/`                       | Rewrite as small candidate-generation examples; no package API or registry dependency.  |
| `reep_scripts/adapters/`                       | Do not migrate, except as conceptual schema notes.                                      |
| `reep_scripts/linkage/`                        | Rewrite only as public-safe write-shape examples; no production upsert helpers.         |
| `reep_scripts/matchers/reep.py`                | Do not migrate unless rewritten as a generic target-register example.                   |
| `config.py`, package metadata, build artefacts | Drop or archive only.                                                                   |

Reference scripts must not import `reep_scripts`, fetch live providers, include D1/Reep
adapters, or depend on private Reep registry helpers.

### Leave Behind Or Archive

Do not migrate:

- semver/package claims;
- adapter code whose only purpose is supporting an installable package;
- import-stability documentation;
- package build metadata;
- Reep-specific registry helpers unless rewritten as generic examples.

## Reference Script Policy

Reference scripts should be:

- small enough to read in one sitting;
- deterministic against committed fixtures;
- written for copying and adaptation;
- explicit about expected input and output shapes;
- free of credentials, private paths, and live-provider assumptions;
- fixture-backed and tested by CI when presented as runnable.

Code snippets embedded in narrative docs may be illustrative only. Standalone files
under `reference-scripts/` should run against committed fixtures.

Each script should have a neighbouring Markdown page:

```text
reference-scripts/python/match_candidates.py
reference-scripts/match-candidates.md
```

The page should explain:

- what pattern the script demonstrates;
- input fixture shape;
- output fixture shape;
- what decisions are deliberately left to the caller;
- which provider docs and templates to read next.

## Provider And Data Model Pages

Provider pages should describe identity surfaces, not collection mechanics.

Each provider card should answer:

- What entity types does the provider identify?
- What are the ID namespaces?
- Which fields are useful identity evidence?
- Which fields are only display, URL, or weak context?
- What bridge paths exist?
- What source-role should this provider normally play?
- What false-positive risks are known?
- What public evidence supports the claims?

Data model pages should describe example input shapes:

- provider record shape;
- useful fields;
- identity grain;
- nullable or missing-field behaviour;
- historical quirks;
- example JSON/CSV snippets with synthetic or public-safe values.

They must not expose private Reep mirror table names, local paths, endpoint-run
commands, credentials, or acquisition recipes. A public version of an internal substrate
doc should preserve the identity-grain lesson and permitted field shape, not the private
storage or fetch machinery.

## Automation

Before public launch, `npm run check` should be the blocking CI gate. It should include
the current checks plus the site-specific layer.

| Check                         | Purpose                                                     |
| ----------------------------- | ----------------------------------------------------------- |
| Markdown formatting           | Keeps PRs reviewable.                                       |
| Front matter validation       | Makes search, nav, and catalogues reliable.                 |
| Local link validation         | Prevents dead docs.                                         |
| Public-boundary validation    | Blocks private paths, credentials, and operational leakage. |
| Provider catalogue generation | Builds provider tables from front matter.                   |
| Examples catalogue generation | Builds example search pages from front matter.              |
| Schema validation             | Validates committed JSON examples against schemas.          |
| Reference-script smoke tests  | Runs scripts only against committed fixtures.               |
| Site build                    | Confirms navigation, search index, and pages compile.       |

Target gate:

```text
npm run check
  npm run format:check
  npm run docs:check
  npm run providers:catalogue -- --check
  npm run examples:catalogue -- --check
  npm run schemas:check
  npm run reference-scripts:test
  npm run site:build
```

Developer convenience commands can remain separate:

```text
npm run format
npm run providers:catalogue
npm run examples:catalogue
```

## Contribution Model

Use normal GitHub pull requests. Contributions should be routed by content type:

| Contribution     | Accepted When                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------ |
| Provider fact    | Backed by public documentation, a public dataset row, a permitted payload shape, or a minimal fixture. |
| Provider quirk   | Includes a concrete failure mode and the safer matching consequence.                                   |
| Guide change     | Improves doctrine clarity without weakening conservative identity gates.                               |
| Worked example   | Small, public-safe, reproducible, and tagged with failure mode and decision.                           |
| Reference script | Runs against committed fixtures and avoids live-provider assumptions.                                  |
| Schema change    | Includes examples and compatibility notes.                                                             |

Provider facts can be community-editable. Practice doctrine should remain
maintainer-reviewed. Reference scripts should require fixture-backed checks.

## Initial Site Navigation

The first public navigation should be task-first, not marketing-first:

1. Start here
2. Register basics
3. Provider catalogue
4. Data models
5. Guides
6. Templates
7. Worked examples
8. Reference scripts
9. Schemas
10. Contributing

The home page should help readers choose a path:

- "I need to understand a provider."
- "I need to decide if a match is safe."
- "I need to model seasons, stages, or matches."
- "I need to review a duplicate."
- "I need a reference script or schema."

## Phased Implementation

### Phase 1: Decision And Skeleton

- Use Starlight as the site engine.
- Add site dependencies and build command.
- Keep Markdown content as source.
- Add navigation and search.
- Preserve existing docs checks.

Done when:

- a site build runs in CI;
- the home page routes readers by task;
- current Markdown checks still pass;
- the repo boundary says `reep-toolkit` is the canonical public docs/reference-code
  surface.
- [MIGRATION-MANIFEST.md](MIGRATION-MANIFEST.md) exists and covers docs, fixtures,
  schemas, selected modules, tests, and package/build artefacts from `reep-scripts`;
- [FOOTBALL-DOCS-BOUNDARY.md](FOOTBALL-DOCS-BOUNDARY.md) defines the explicit launch
  boundary: source backend, migrated public content, or deferred non-public material.

### Phase 2: Provider Consolidation

- Promote `reep-scripts` provider docs into `docs/providers/`.
- Keep the toolkit card format.
- Expand catalogue generation.
- Add provider status badges: draft, reviewed, stable.

Done when:

- every `reep-scripts/docs/providers/*.md` page is either migrated, deliberately
  dropped, or listed in a migration manifest;
- every relevant `football-docs` public-provider claim is either migrated, cited, or
  explicitly kept out of the public launch;
- migrated provider cards carry toolkit front matter;
- collection/scraping wording is removed or rewritten as accepted input/source shape;
- provider catalogue generation covers the full migrated set.

### Phase 3: Reference Code Migration

- Move useful `reep_scripts` mechanics into `reference-scripts/`, `templates/`,
  `schemas/`, and fixtures.
- Remove package positioning.
- Add fixture-backed smoke tests.

Done when:

- selected reference scripts run against committed fixtures in CI;
- evidence/candidate and provider-record schemas validate their examples;
- package, semver, and import-stability claims have been removed from the public toolkit
  surface;
- no standalone reference script imports `reep_scripts`, fetches live provider data, or
  uses Reep/D1-specific adapters;
- any non-migrated code is explicitly archived or dropped.

### Phase 4: Public Contribution Readiness

- Add "Edit this page" links.
- Add provider-card issue templates.
- Add contribution checklist.
- Add public-boundary and evidence-requirement guidance to PR templates.

Done when:

- contribution routes distinguish provider facts, examples, schema changes, and
  reference scripts;
- provider-fact PRs require evidence;
- maintainer-reviewed doctrine pages are labelled as such;
- public-boundary checks run in CI.

### Phase 5: Archive `reep-scripts`

- Freeze `reep-scripts` once migrated.
- Replace its README with a pointer to Reep Toolkit.
- Keep history available, but stop presenting it as the current public package.

Done when:

- `reep-scripts` no longer claims to be the active public package or docs source;
- all kept material has a canonical home in `reep-toolkit`;
- the migration manifest has no unresolved rows;
- the archive README points contributors and readers to the toolkit.

## Open Decisions

1. Should provider docs keep one page per provider, or split large providers into
   identity surfaces, access model, quirks, and examples?

## Settled Decisions

- Keep the public name `reep-toolkit` for now.
- Use Astro Starlight for the public docs site.
- Make `reep-toolkit` the canonical public docs/reference-code repo.
- Archive `reep-scripts` after migration rather than maintaining a compatibility
  package.
- Make `reep-toolkit` the public provider-reference authority at launch.
- Keep `football-docs` out of the public-authority role unless a separate migration
  explicitly moves its public-safe provider facts into the toolkit.
- Pair meaningful runnable examples with fixtures and schemas. Narrative-only examples
  are fine when they are explaining a decision rather than presenting reusable code.
