---
doc_type: pipeline
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: pipelines
stance: opinionated
contribution_model: maintainer_doctrine
---

# Pipeline Architecture

The toolkit architecture is a composition pattern, not a framework requirement. Keep
source loading, candidate matching, target-register lookup, review, and writes as
separate concerns so each step can be tested, replayed, and replaced.

```text
source snapshot -> loader -> matcher -> registry lookup -> review/write decision -> lineage-aware write
```

## Components

| Component      | Responsibility                                                    | Must not do                                                   |
| -------------- | ----------------------------------------------------------------- | ------------------------------------------------------------- |
| Loader         | Convert provider-native rows into stable provider-shaped records. | Write to the target register or hide provider quirks.         |
| Matcher        | Produce candidates, evidence, blockers, and confidence labels.    | Mutate bridges, allocate IDs, or make irreversible decisions. |
| Registry       | Answer target-store lookups by bridge or identity signals.        | Guess when the target store has multiple plausible answers.   |
| Review surface | Preserve uncertainty and operator decisions.                      | Re-run matching logic with looser hidden thresholds.          |
| Writer         | Apply accepted decisions with provenance and lineage.             | Overwrite stronger evidence with weaker evidence.             |

## Loader Boundary

Loaders should preserve provider semantics. If a provider has `team_code`, `team_id`,
and `opta_numeric`, keep those distinctions visible rather than flattening them into a
generic `id` column too early.

Good loaders emit typed records:

```text
ProviderPlayer(provider_id, name, date_of_birth, nationality, team_context, source_snapshot)
ProviderTeam(provider_id, name, country, source_snapshot)
ProviderMatch(provider_id, date, home_provider_id, away_provider_id, competition_context)
```

The same matcher should be able to consume records loaded from a downloaded CSV, a
cached API response, or a user-supplied vendor export if those records have the same
shape.

## Matcher Boundary

Matchers are pure functions. They should return a payload, not a write:

```text
records + registry -> candidates + blockers + rejected rows + review residue
```

This makes it cheap to:

- rerun against the same snapshot;
- compare two matcher versions;
- inspect weak candidates before accepting them;
- test difficult edge cases without touching a real register.

## Registry Boundary

Registries are where target-store strictness belongs. A matcher can ask "who has this
Transfermarkt player ID?" or "who matches this DOB/name pair?" The registry decides
whether the target store has one safe answer.

Examples of registry strictness:

- reject a player lookup when two live candidates share the same DOB and alias;
- require country for team name lookup;
- require resolved home and away team IDs before match lookup;
- refuse cross-type bridge hits.

## Template Versus Recipe

Portable templates and private register recipes are different artefacts.

A public template:

- accepts explicit provider records or fixtures;
- returns candidates, evidence, conflicts, or blockers;
- leaves acceptance thresholds to the caller;
- has synthetic or public-safe examples.

A register recipe:

- reads a private doctrine matrix or local mirrors;
- emits a private action plan;
- respects a project-specific review/apply gate;
- publishes project-specific projections.

The toolkit should contain templates, fixtures, and examples. Private control planes
should stay outside it.

## Six Concerns

| Concern         | Public-toolkit shape                                                |
| --------------- | ------------------------------------------------------------------- |
| Source snapshot | Durable source state with a version, hash, and licence/access note. |
| Standardisation | Deterministic text/date/country/position normalisation.             |
| Identification  | Stable target IDs owned by the consuming register.                  |
| Linking         | Candidate generation and bridge evidence.                           |
| Verification    | Schema, type, uniqueness, and coverage checks.                      |
| Publication     | Consumer-owned exports, APIs, or downstream tables.                 |

The toolkit can show small examples for each concern, but it should not turn them into
one mandatory runtime.

## Reproducibility

A good run can be explained with:

- source snapshot label;
- matcher/template version;
- target-register baseline;
- method and confidence;
- blockers or review decision;
- final write lineage.

If any of those are missing, future maintainers will not know whether a changed outcome
is genuine source drift, a matcher change, or a target-register repair.
