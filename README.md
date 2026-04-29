---
doc_type: project_overview
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: home
stance: descriptive
contribution_model: maintainer_doctrine
---

# Reep Toolkit

Reep Toolkit is a public guide to football identity work: provider world models,
Reep-informed register practice, and pipeline patterns for turning provider records into
stable entity mappings.

The docs are designed as source material for a guide website. Improve the docs and the
site improves with them.

This is still a draft. The structure is in place; the next work is review, provider-card
depth, runnable examples, and site generation.

## How to Read This Repo

Use this README as the human overview and table of contents. Use
[docs/INDEX.md](docs/INDEX.md) as the more detailed documentation map and future search
landing page.

There are three useful ways through the material:

| Reader goal                         | Start here                                                  | Then read                                                                                                                    |
| ----------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Understand the register worldview   | [World model](docs/world-model/README.md)                   | [IDs and lineage](docs/world-model/ids-and-lineage.md), [source authority](docs/world-model/source-authority.md)             |
| Add or evaluate a provider          | [Before you ingest](docs/guides/before-you-ingest.md)       | [Provider docs](docs/providers/README.md), [provider catalogue](docs/providers/CATALOGUE.md)                                 |
| Implement matching or review logic  | [Matching thresholds](docs/guides/matching-thresholds.md)   | [Bridging provider IDs](docs/guides/bridging-provider-ids.md), [examples](docs/examples/README.md)                           |
| Maintain a register after ingestion | [Register maintenance](docs/guides/register-maintenance.md) | [Duplicate resolution](docs/guides/duplicate-resolution.md), [snapshot drift report](docs/examples/snapshot-drift-report.md) |
| Contribute documentation            | [Contributing](CONTRIBUTING.md)                             | [Editorial standard](docs/EDITORIAL.md), [front matter taxonomy](docs/FRONTMATTER.md)                                        |

Read the examples early. The doctrine is intentionally opinionated, but the examples
show the practical shape: accepted writes, rejected writes, review candidates, and
merge/audit records.

## Purpose

Football data projects repeatedly need to answer the same identity questions:

- Which entity types does a provider actually identify?
- Which fields are safe for matching, and which are decorative?
- Which provider IDs are direct bridges, derived bridges, aliases, or unstable slugs?
- How should a register preserve stable IDs while upstream data changes?
- How do loaders, matchers, registries, snapshots, review queues, and writes fit
  together?

Reep Toolkit answers those questions with the parts of Reep's practice that are worth
sharing: thresholds, merge doctrine, source-authority choices, provider gotchas, and
maintenance patterns. It does not expose private Reep execution details, paid snapshots,
local paths, or operational runbooks.

## Audience

- Analysts joining data across providers.
- Clubs and vendors maintaining internal IDs across third-party feeds.
- Open-data maintainers building or maintaining football registers.
- Contributors who want to improve public provider documentation.
- Reep maintainers deciding which parts of Reep's matching practice are valuable and
  safe to share.

## Content Lanes

The docs have three editorial jobs.

| Lane                 | What it is                                                                                             | Tone                          | Contribution model                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------- | ----------------------------------------------------------------------------- |
| Provider reference   | Facts about a provider's entity model, IDs, fields, bridges, access, and quirks.                       | Descriptive and evidence-led. | Community contributions welcome with reproducible evidence.                   |
| Practice guides      | Reep-informed guidance on matching, minting, bridging, duplicate resolution, and register maintenance. | Opinionated and prescriptive. | Maintainer-owned doctrine; contributions should argue from concrete evidence. |
| Examples and schemas | Small concrete examples that show how the practice can be implemented.                                 | Practical and adaptable.      | Contributions welcome when they stay public-safe and reproducible.            |

The practice guides are allowed to say "we recommend this" and "do not do that". The
point is to share the judgement Reep has accumulated. The provider reference pages
describe the provider, not Reep's private implementation.

## Detailed Contents

### Orientation

- [Documentation index](docs/INDEX.md): the main docs map.
- [Roadmap](docs/ROADMAP.md): draft scope and review gates.
- [Guide site model](docs/SITE.md): how the docs can feed a guide website.
- [Editorial standard](docs/EDITORIAL.md): how to keep public docs useful and safe.
- [Front matter taxonomy](docs/FRONTMATTER.md): metadata keys for search and
  publication.
- [Contributing](CONTRIBUTING.md): contribution rules.

### World Model

- [World model overview](docs/world-model/README.md).
- [Entity model](docs/world-model/entities.md): players, teams, coaches, competitions,
  seasons, and matches.
- [IDs and lineage](docs/world-model/ids-and-lineage.md): stable register IDs, provider
  bridges, aliases, provenance, tombstones, and redirects.
- [Confidence and validation](docs/world-model/confidence-and-validation.md): confidence
  labels and review routing.
- [Seasons and matches](docs/world-model/seasons-and-matches.md): parent seasons, leaf
  stages, and fixture identity.
- [Source authority](docs/world-model/source-authority.md): choosing canonical sources.
- [Public/private boundary](docs/world-model/public-private-boundary.md): what belongs
  in this public toolkit.

### Practice Guides

- [Practice guides overview](docs/guides/README.md).
- [Before you ingest](docs/guides/before-you-ingest.md): questions to answer before
  writing a loader or matcher.
- [Golden path provider ingest](docs/guides/golden-path-provider-ingest.md): one route
  from provider card to snapshot, matching, review, write set, and maintenance.
- [Matching thresholds](docs/guides/matching-thresholds.md): `1.0`, `0.95`, `0.90`,
  `0.80`, and reject/discovery bands.
- [Bridging provider IDs](docs/guides/bridging-provider-ids.md): direct, hub, derived,
  signal, slug, and conflict bridge handling.
- [Minting and entity creation](docs/guides/minting-and-entity-creation.md): when to
  create entities and when to defer.
- [Duplicate resolution](docs/guides/duplicate-resolution.md): merge, tombstone,
  redirect, and data movement policy.
- [Register maintenance](docs/guides/register-maintenance.md): recurring checks for
  drift, conflicts, freshness, and coverage.

### Provider Knowledge

- [Provider docs overview](docs/providers/README.md).
- [Provider catalogue](docs/providers/CATALOGUE.md).
- [Provider template](docs/providers/_template.md).
- [Source taxonomy](docs/providers/sources.md).
- Current provider cards: [Wikidata](docs/providers/wikidata.md),
  [Transfermarkt](docs/providers/transfermarkt.md), [Opta](docs/providers/opta.md),
  [SportMonks](docs/providers/sportmonks.md), [FBref](docs/providers/fbref.md),
  [FotMob](docs/providers/fotmob.md), [TheSportsDB](docs/providers/thesportsdb.md),
  [Soccerdonna](docs/providers/soccerdonna.md).

### Pipeline Concepts

- [Pipeline overview](docs/pipelines/README.md): acquire, load, match, review, write,
  export.
- [Loaders](docs/pipelines/loaders.md): provider-native records to stable shapes.
- [Registries](docs/pipelines/registries.md): target-store lookup interfaces.
- [Matchers](docs/pipelines/matchers.md): pure candidate generation.
- [Writes and lineage](docs/pipelines/writes-and-lineage.md): confidence-aware writes.
- [Snapshots](docs/pipelines/snapshots.md): reproducible source capture and replay.

### Worked Examples

- [Examples catalogue](docs/examples/CATALOGUE.md): generated table of failure modes,
  decisions, providers, entity types, and search tags.
- [Build a small register](docs/examples/build-a-small-register.md).
- [Add a provider](docs/examples/add-a-provider.md).
- [Update from a snapshot](docs/examples/update-from-snapshot.md).
- [Review weak matches](docs/examples/review-weak-matches.md).
- [Provider ingest walkthrough](docs/examples/provider-ingest-walkthrough.md).
- [SportMonks Transfermarkt bridge](docs/examples/sportmonks-transfermarkt-bridge.md).
- [FotMob signal-only player match](docs/examples/fotmob-signal-only-player.md).
- [Women-only prior beats fuzzy bridge](docs/examples/women-only-prior-fuzzy-bridge.md).
- [Team name collision](docs/examples/team-name-collision.md).
- [Match fixture identity](docs/examples/match-fixture-identity.md).
- [Opta namespace confusion](docs/examples/opta-namespace-confusion.md).
- [Type-gated provider ID lookup](docs/examples/type-gated-provider-id-lookup.md).
- [Alias variant duplicate prevention](docs/examples/alias-variant-duplicate-prevention.md).
- [Name-token subset bridge](docs/examples/name-token-subset-bridge.md).
- [Semantic team prefix collision](docs/examples/semantic-team-prefix-collision.md).
- [Fixture-overlap team bridge](docs/examples/fixture-overlap-team-bridge.md).
- [SportMonks stage and season mismatch](docs/examples/sportmonks-stage-season-mismatch.md).
- [Structural season ID collision](docs/examples/structural-season-id-collision.md).
- [Second-order bridge rejection](docs/examples/second-order-bridge-rejection.md).
- [Local mirror staleness](docs/examples/local-mirror-staleness.md).
- [Duplicate player merge](docs/examples/duplicate-player-merge.md).
- [Duplicate merge with provider conflict](docs/examples/duplicate-merge-with-provider-conflict.md).
- [Bridge conflict case study](docs/examples/bridge-conflict-case-study.md).
- [Snapshot drift report](docs/examples/snapshot-drift-report.md).

### Reference Schema

- [Reference register schema](schemas/reference-register.sql): optional SQLite-shaped
  schema for examples and small deployments.

## Example Sources

The examples should be public-safe rewrites of real classes of problems, not private
runbooks. Good source material lives in:

- provider cards and docs imported from `reep-scripts`,
- public provider documentation,
- Reep handovers that describe reusable failure modes,
- validator warnings and review CSV patterns,
- resolved duplicate and bridge-conflict incidents,
- snapshot refreshes where upstream data changed shape or meaning.

When turning a real incident into an example, keep the lesson and replace private
identifiers, file paths, production counts, and operational commands with small invented
records.

## Repo Shape

```text
reep-toolkit/
├── docs/
│   ├── FRONTMATTER.md
│   ├── INDEX.md
│   ├── guides/
│   ├── world-model/
│   ├── providers/
│   ├── pipelines/
│   └── examples/
└── schemas/
    └── reference-register.sql
```

## Working Boundary

Share:

- Provider world models, field semantics, bridge paths, and quirks.
- Reep-informed register practice: stable IDs, provenance, confidence routing, aliases,
  duplicate resolution, soft deletes, redirects, and ambiguity handling.
- Public pipeline primitives: loader shapes, matcher cascades, registry interfaces,
  lineage-aware writes, snapshot replay.
- Reep's decision-making when the lesson can be shared without exposing private files or
  operational paths.

Do not share:

- Private `reep-custom` scripts, local file paths, D1 promotion details, Linear
  operations, paid snapshots, unreleased source-specific phase plans, or exact private
  doctrine that depends on licensed feeds.
- Internal Reep IDs or production counts unless they already appear in public Reep
  material.
- Operational instructions that would only make sense inside the private Reep
  infrastructure.

## Editorial Rule

Write for someone who is about to work with a provider or maintain a register.

Good:

> A provider bridge should not overwrite stronger curated evidence unless the new source
> has a documented authority advantage. Keep the older bridge as history and route
> conflicts to review.

Bad:

> Run this private script from this private repository against this local file and
> promote the result.

Good:

> When merging duplicates, keep one canonical entity, redirect the retired ID, move
> non-conflicting provider bridges and aliases to the canonical entity, and preserve
> rejected/conflicting mappings for audit.

Bad:

> Reep's exact production merge command is the public recommendation.

## First-Pass Review Questions

1. Is the public/private boundary right?
2. Are the practice guides opinionated enough without exposing private Reep internals?
3. Does the repo now read like guide-site source material?
4. Which provider cards should be promoted first from `reep-scripts`?
5. What should be code in `reep-scripts` versus documentation in this toolkit?
