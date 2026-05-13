---
doc_type: provider_card
content_lane: reference
status: review_ready
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: opta
entity_types: [player, team, coach, competition, season, match]
access_tier: paid_or_private
source_kind: living
authority_role: canonical_candidate
bridge_providers: [fpl, wikidata, premier_league]
matching_fields:
  [
    opta_uuid,
    opta_numeric,
    optacore,
    name,
    date_of_birth,
    team_id,
    competition_id,
    season_id,
  ]
confidence_floor: 1.0
private_dependencies: []
---

# Opta / Stats Perform

Opta is a major commercial football data family, but "Opta ID" is not one thing. Before
ingesting Opta-related data, establish which namespace each ID belongs to.

## Why It Matters Before You Start

A large class of football identity bugs comes from mixing Opta namespaces. A numeric ID
from one surface is not interchangeable with a modern UUID from another surface. Treat
each namespace as its own provider ID until a documented mapping proves equivalence.

## ID Systems

| Namespace        | Shape                                      | Entity coverage                                                     | Notes                                                             |
| ---------------- | ------------------------------------------ | ------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `opta`           | 25-character alphanumeric UUID-like string | Player, team, competition, season, match.                           | Modern Stats Perform surface.                                     |
| `opta_numeric`   | numeric                                    | Player, team, coach, competition, season in legacy/public surfaces. | Publicly recoverable in some contexts, especially FPL.            |
| `optacore`       | numeric                                    | Competition and season.                                             | Separate small-integer namespace; do not mix with `opta_numeric`. |
| `premier_league` | numeric                                    | Premier League player pages.                                        | Related public ecosystem, but not equal to Opta numeric.          |

## Matching Surface

| Field                       | Use                                     | Gotcha                                                                    |
| --------------------------- | --------------------------------------- | ------------------------------------------------------------------------- |
| Modern Opta ID              | Strong bridge inside licensed feeds.    | Not publicly available in bulk.                                           |
| Opta numeric                | Public bridge in FPL/Wikidata contexts. | Not equal to modern Opta ID.                                              |
| Name and DOB                | Strong player matching when supplied.   | Feed shapes vary by product.                                              |
| Team ID                     | Team context.                           | Keep namespace explicit.                                                  |
| Competition/season mappings | Season model.                           | Competition and season IDs can exist in multiple Opta-related namespaces. |

## Bridge Surface

| Bridge route                            | Use                                      | Caution                                                            |
| --------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------ |
| FPL `code` → `opta_numeric` player      | Public Premier League player bridge.     | It is not a modern Opta UUID.                                      |
| FPL `team_code` → `opta_numeric` team   | Public Premier League team bridge.       | Do not confuse with the per-season FPL `team` ID.                  |
| Wikidata → `opta_numeric`               | Public player/team/competition evidence. | Coverage is sparse and namespace-specific.                         |
| Licensed mapping → `opta` UUID          | Strong bridge inside licensed feeds.     | Keep payloads and private mappings out of public examples.         |
| `optacore` mapping → competition/season | Useful structural mapping.               | Small integers can collide visually with other numeric namespaces. |

## Reep-Style Linking Advice

- Store `opta`, `opta_numeric`, `optacore`, and `premier_league` as separate provider
  namespaces.
- Add explicit bridge rows only when a source proves the relationship between
  namespaces.
- Reject Opta IDs that fail namespace format checks.
- For public docs, describe the namespace model and gotchas; do not publish licensed
  payloads.
- When using Opta as a creation source, document which surface is authoritative for each
  entity type.

## Safe Use Matrix

| Task               | Recommended use                                                    | Review trigger                                  |
| ------------------ | ------------------------------------------------------------------ | ----------------------------------------------- |
| Modern ID bridge   | Accept only when the source clearly names the modern Opta surface. | Numeric value appears under `opta`.             |
| Numeric bridge     | Store as `opta_numeric`, not as modern `opta`.                     | Source says only "Opta ID" without namespace.   |
| Competition/season | Keep `opta`, `opta_numeric`, and `optacore` separate.              | Small integer could belong to multiple systems. |
| Player/team match  | Prefer direct ID; fallback needs DOB/name or strong context.       | Name-only or current-team-only match.           |
| Match identity     | Use schedule/fixture identity with resolved teams and season.      | Event payload exists without fixture context.   |

## Do Not Do

- Do not coerce all "Opta ID" values into one provider namespace.
- Do not infer modern Opta UUIDs from public numeric IDs.
- Do not publish licensed payload examples in public docs.
- Do not let product-surface terminology hide whether the ID is for a competition,
  season, stage, team, player, or match.

## Useful Examples

- [Opta namespace confusion](../examples/opta-namespace-confusion.md).
- [Match fixture identity](../examples/match-fixture-identity.md).

## Gotchas

- A small integer can be `optacore`, not `opta_numeric`.
- FPL `code` is public evidence for `opta_numeric`, not for modern Opta UUIDs.
- FPL `team_code` is the team `opta_numeric`; FPL `team` is a season-scoped FPL ID.
- Third-party docs often say "Opta ID" without naming the namespace.
- Competition, season, and match modelling can differ between product surfaces.
- Event-data consumers such as WhoScored can licence Opta data without becoming part of
  the Opta/Stats Perform ID family.

## References

- [Stats Perform](https://www.statsperform.com/)
- [The Analyst](https://theanalyst.com/)
- [FPL bootstrap API](https://fantasy.premierleague.com/api/bootstrap-static/)
- Wikidata [P8735](https://www.wikidata.org/wiki/Property:P8735),
  [P8736](https://www.wikidata.org/wiki/Property:P8736),
  [P8737](https://www.wikidata.org/wiki/Property:P8737)
