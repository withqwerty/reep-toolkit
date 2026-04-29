---
doc_type: project_overview
content_lane: reference
status: review_ready
public_safe: true
last_verified: 2026-04-29
site_section: home
stance: descriptive
contribution_model: maintainer_doctrine
---

# Reep Toolkit

Public documentation for building and maintaining football entity registers.

Reep Toolkit collects provider knowledge, register doctrine, matching thresholds,
pipeline patterns, and concrete examples for anyone joining football data across
providers. It is opinionated because it comes from Reep practice, but it is written as
public-safe guidance rather than a mirror of private Reep operations.

Use it when you need to answer questions like:

- What does this provider actually identify?
- Is this provider ID a direct bridge, an alias, a slug, or only a weak signal?
- When should a match write automatically, route to review, defer, or reject?
- How should a register preserve stable IDs while providers change shape?
- What should happen when two register entities turn out to be duplicates?

## Start Here

| Goal                                  | Read first                                                  | Then go deeper                                                                                                        |
| ------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Understand the register model         | [World model](docs/world-model/README.md)                   | [IDs and lineage](docs/world-model/ids-and-lineage.md), [source authority](docs/world-model/source-authority.md)      |
| Ingest a new provider                 | [Before you ingest](docs/guides/before-you-ingest.md)       | [Golden path ingest](docs/guides/golden-path-provider-ingest.md), [provider cards](docs/providers/README.md)          |
| Implement matching and bridge logic   | [Matching thresholds](docs/guides/matching-thresholds.md)   | [Bridging provider IDs](docs/guides/bridging-provider-ids.md), [examples catalogue](docs/examples/CATALOGUE.md)       |
| Maintain an existing register         | [Register maintenance](docs/guides/register-maintenance.md) | [Duplicate resolution](docs/guides/duplicate-resolution.md), [snapshot drift](docs/examples/snapshot-drift-report.md) |
| Contribute provider knowledge or docs | [Contributing](CONTRIBUTING.md)                             | [Editorial standard](docs/EDITORIAL.md), [front matter](docs/FRONTMATTER.md)                                          |

For the full documentation map, use [docs/INDEX.md](docs/INDEX.md).

## What Is In The Repo

```text
docs/
├── guides/        # opinionated register practice
├── providers/     # provider world models, quirks, and ID semantics
├── world-model/   # entity, ID, source-authority, confidence, and lineage doctrine
├── pipelines/     # loader, matcher, registry, snapshot, and write patterns
└── examples/      # small public-safe cases showing decisions and failure modes
schemas/
└── reference-register.sql
```

## Core Ideas

### Matching Is Not One Fuzzy Function

Useful football identity work is a governed pipeline:

1. describe the provider's world model;
2. snapshot the source;
3. normalise records into stable shapes;
4. search candidates through typed registry lookups;
5. apply confidence and source-authority rules;
6. write bridges, aliases, provenance, and review residue;
7. keep validating as providers drift.

### Provider IDs Need A Role

The same provider can expose stable IDs, unstable slugs, derived references, display
names, hub IDs, and decorative fields. The toolkit separates these roles so a register
does not treat every identifier-shaped value as safe authority.

Start with:

- [Provider source taxonomy](docs/providers/sources.md)
- [Bridging provider IDs](docs/guides/bridging-provider-ids.md)
- [Type-gated provider ID lookup](docs/examples/type-gated-provider-id-lookup.md)

### Confidence Routes The Write

The confidence model is deliberately conservative:

- `1.0`: typed direct bridge from an authoritative source;
- `0.95`: multi-signal match that can write only under strict conditions;
- `0.90`: plausible but review-required;
- `0.80`: discovery candidate, not a write;
- below that: reject or keep only as diagnostic evidence.

Read [matching thresholds](docs/guides/matching-thresholds.md) for the full policy.

### Stable IDs Should Survive Maintenance

When a register finds duplicates, the answer is not usually to delete history. Keep a
canonical entity, redirect or tombstone the retired one, move non-conflicting bridges
and aliases, and preserve conflict evidence for audit.

Start with:

- [IDs and lineage](docs/world-model/ids-and-lineage.md)
- [Duplicate resolution](docs/guides/duplicate-resolution.md)
- [Duplicate player merge](docs/examples/duplicate-player-merge.md)
- [Duplicate merge with provider conflict](docs/examples/duplicate-merge-with-provider-conflict.md)

## Provider Knowledge

Provider cards document what a source identifies, how its fields behave, and where it
commonly misleads matching logic.

Current cards:

- [Wikidata](docs/providers/wikidata.md)
- [Transfermarkt](docs/providers/transfermarkt.md)
- [Opta](docs/providers/opta.md)
- [SportMonks](docs/providers/sportmonks.md)
- [FBref](docs/providers/fbref.md)
- [FotMob](docs/providers/fotmob.md)
- [TheSportsDB](docs/providers/thesportsdb.md)
- [Soccerdonna](docs/providers/soccerdonna.md)

Use the [provider template](docs/providers/_template.md) for new cards and the
[provider catalogue](docs/providers/CATALOGUE.md) to see coverage.

## Worked Examples

Read examples early. They show what the doctrine does to actual-looking rows:
auto-write, review, defer, reject, tombstone, redirect, or preserve as conflict
evidence.

High-signal starting points:

- [Build a small register](docs/examples/build-a-small-register.md)
- [Provider ingest walkthrough](docs/examples/provider-ingest-walkthrough.md)
- [SportMonks Transfermarkt bridge](docs/examples/sportmonks-transfermarkt-bridge.md)
- [FotMob signal-only player match](docs/examples/fotmob-signal-only-player.md)
- [Women-only prior beats fuzzy bridge](docs/examples/women-only-prior-fuzzy-bridge.md)
- [Top-down hierarchical bridge ingest](docs/examples/top-down-hierarchical-bridge-ingest.md)
- [Semantic team prefix collision](docs/examples/semantic-team-prefix-collision.md)
- [Fixture-overlap team bridge](docs/examples/fixture-overlap-team-bridge.md)
- [Match fixture identity](docs/examples/match-fixture-identity.md)
- [Local mirror staleness](docs/examples/local-mirror-staleness.md)
- [Snapshot drift report](docs/examples/snapshot-drift-report.md)

The generated [examples catalogue](docs/examples/CATALOGUE.md) is the best search
surface for failure modes, providers, entity types, and decisions.

## Public Boundary

This repo shares reusable judgement:

- provider world models;
- field semantics and ID roles;
- bridge, alias, confidence, and provenance patterns;
- matching thresholds and review routing;
- duplicate-resolution and register-maintenance doctrine;
- public-safe examples with invented IDs.

It does not share:

- private Reep scripts or local file paths;
- credentials, paid raw snapshots, or production commands;
- private issue-tracker workflow;
- unreleased operational runbooks;
- production counts or IDs unless already public.

The boundary is documented in
[public/private boundary](docs/world-model/public-private-boundary.md).

## Contributing

Contributions are welcome when they make the docs more useful and remain public-safe.

Good contributions include:

- a provider-card correction with reproducible evidence;
- a new provider quirk that affects matching;
- an example showing a concrete false-positive trap;
- a clearer write/review/defer decision;
- a schema or pipeline pattern that helps small registers.

Before opening a change, read [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/EDITORIAL.md](docs/EDITORIAL.md).

## Checks

```bash
npm install
npm run check
```

`npm run check` validates formatting, Markdown front matter, local links, example
catalogue metadata, and obvious public-boundary leaks.

Use `npm run format` before committing docs changes.
