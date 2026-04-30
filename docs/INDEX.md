---
doc_type: docs_index
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: home
stance: descriptive
contribution_model: evidence_required
---

# Documentation Index

Use this index as the search landing page. Every public Markdown document carries front
matter so it can be filtered by `content_lane`, `doc_type`, `entity_types`, `provider`,
`access_tier`, `matching_fields`, `confidence_floor`, and `status`.

## How to Read These Docs

The toolkit has two main reading modes:

- **Reference pages** describe provider facts and are open to evidence-backed
  contributions.
- **Practice guides** are opinionated Reep-style guidance. They explain the judgements,
  thresholds, and maintenance patterns we think are worth sharing.

The distinction matters. A provider page tells you what a provider exposes. A practice
guide tells you what to do with that knowledge when building or maintaining a register.

## Contribution and Site Model

- [Contributing](../CONTRIBUTING.md): how to contribute provider facts, practice
  guidance, examples, and schema changes.
- [Guide site model](SITE.md): how front matter maps to site sections, search facets,
  and publication rules.
- [Front matter taxonomy](FRONTMATTER.md): metadata keys used by docs and future site
  tooling.
- [Editorial standard](EDITORIAL.md): how to keep the docs sharp, public-safe, and
  Reep-informed.

## World Model

- [Roadmap](ROADMAP.md): first-pass scope, review gates, and follow-up work.
- [Entity model](world-model/entities.md): players, teams, coaches, competitions,
  seasons, and matches.
- [IDs and lineage](world-model/ids-and-lineage.md): stable IDs, provider bridges,
  aliases, provenance, and redirects.
- [Confidence and validation](world-model/confidence-and-validation.md): how confidence
  labels route writes, review, and rejection.
- [Seasons and matches](world-model/seasons-and-matches.md): parent seasons, leaf
  stages, and fixture identity.
- [Source authority](world-model/source-authority.md): how to choose and document
  canonical sources.
- [Public/private boundary](world-model/public-private-boundary.md): what belongs in an
  open toolkit.

## Practice Guides

- [Practice guides overview](guides/README.md): the opinionated, Reep-informed guide
  layer.
- [Before you ingest](guides/before-you-ingest.md): what to understand before adding a
  provider to a register.
- [Golden path provider ingest](guides/golden-path-provider-ingest.md): a conservative
  end-to-end route from provider card to write set.
- [Matching thresholds](guides/matching-thresholds.md): confidence bands, auto-write
  rules, and review routing.
- [Bridging provider IDs](guides/bridging-provider-ids.md): direct bridges, derived
  bridges, conflicts, and bridge provenance.
- [Relationship-constrained provider matching](guides/relationship-constrained-provider-matching.md):
  using mapped competition, team, match, and line-up context without weakening identity
  gates.
- [Minting and entity creation](guides/minting-and-entity-creation.md): when to create
  new entities and when to defer.
- [Duplicate resolution](guides/duplicate-resolution.md): merge, tombstone, redirect,
  and data movement policy.
- [Register maintenance](guides/register-maintenance.md): recurring checks for drift,
  conflicts, freshness, and coverage.

## Provider Knowledge

- [Provider docs overview](providers/README.md): contribution rules and the
  provider-card shape.
- [Provider catalogue](providers/CATALOGUE.md): full-card coverage and queued provider
  docs.
- [Provider template](providers/_template.md): front matter and section skeleton for new
  providers.
- [Source taxonomy](providers/sources.md): living/static, authoritative/derived,
  bridge/metadata, append-only/evolving.

## Pipelines

- [Pipeline overview](pipelines/README.md): acquire, load, match, review, write, export.
- [Loaders](pipelines/loaders.md): normalising provider-native records into stable
  shapes.
- [Registries](pipelines/registries.md): target-store lookup interfaces.
- [Matchers](pipelines/matchers.md): pure cascades that produce candidate links.
- [Writes and lineage](pipelines/writes-and-lineage.md): confidence-aware upserts and
  audit fields.
- [Snapshots](pipelines/snapshots.md): reproducible source capture and replay.

## Examples

- [Examples catalogue](examples/CATALOGUE.md): generated table of failure modes,
  decisions, providers, entity types, and search tags.
- [Build a small register](examples/build-a-small-register.md).
- [Add a provider](examples/add-a-provider.md).
- [Update from a snapshot](examples/update-from-snapshot.md).
- [Review weak matches](examples/review-weak-matches.md).
- [SportMonks Transfermarkt bridge](examples/sportmonks-transfermarkt-bridge.md).
- [FotMob signal-only player match](examples/fotmob-signal-only-player.md).
- [Women-only prior beats fuzzy bridge](examples/women-only-prior-fuzzy-bridge.md).
- [Opta namespace confusion](examples/opta-namespace-confusion.md).
- [Type-gated provider ID lookup](examples/type-gated-provider-id-lookup.md).
- [Alias variant duplicate prevention](examples/alias-variant-duplicate-prevention.md).
- [Name-token subset bridge](examples/name-token-subset-bridge.md).
- [Team name collision](examples/team-name-collision.md).
- [Semantic team prefix collision](examples/semantic-team-prefix-collision.md).
- [Fixture-overlap team bridge](examples/fixture-overlap-team-bridge.md).
- [Match fixture identity](examples/match-fixture-identity.md).
- [SportMonks stage and season mismatch](examples/sportmonks-stage-season-mismatch.md).
- [Structural season ID collision](examples/structural-season-id-collision.md).
- [Second-order bridge rejection](examples/second-order-bridge-rejection.md).
- [Local mirror staleness](examples/local-mirror-staleness.md).
- [Duplicate player merge](examples/duplicate-player-merge.md).
- [Snapshot drift report](examples/snapshot-drift-report.md).
- [Bridge conflict case study](examples/bridge-conflict-case-study.md).
- [Duplicate merge with provider conflict](examples/duplicate-merge-with-provider-conflict.md).
- [Provider ingest walkthrough](examples/provider-ingest-walkthrough.md).

## Reference Schema

- [reference-register.sql](../schemas/reference-register.sql): optional SQLite-shaped
  schema for examples and small deployments.
