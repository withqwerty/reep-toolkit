---
doc_type: practice_guide
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, match]
matching_fields:
  [
    provider_id,
    name,
    date_of_birth,
    nationality,
    country,
    match_date,
    home_team,
    away_team,
  ]
confidence_floor: 0.95
---

# Matching Thresholds

Reep's matching posture is precision-first. A public register is more damaged by a false
positive than by an unresolved record. Misses can be filled later; wrong bridges
contaminate every downstream export.

## Threshold Bands

| Confidence | Reep-style meaning                                                                                                                        | Default route                                |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `1.0`      | Direct stable bridge from a trusted provider or equivalent same-namespace evidence.                                                       | Auto-write if uniqueness checks pass.        |
| `0.95`     | Strong identity evidence, such as DOB plus normalised full name, or a trusted bridge with entity-type corroboration.                      | Auto-write if ambiguity is rejected.         |
| `0.90`     | Corroborating but not decisive evidence, such as a derived bridge, name plus nationality, or provider mapping with known false positives. | Review or require independent corroboration. |
| `0.80`     | Weak candidate, such as name-only or slug-only evidence.                                                                                  | Candidate only. Do not auto-write.           |
| `<0.80`    | Search/discovery signal.                                                                                                                  | Do not write.                                |

These values are labels for routing work. They are not calibrated probabilities.

## Auto-Write Requirements

An auto-write needs all of:

- one unambiguous target entity,
- an entity type match,
- no stronger conflicting bridge already present,
- enough source lineage to reproduce the decision,
- a method label that says why the match was accepted.

## Review Requirements

Route to review when:

- multiple candidates survive blocking,
- the match depends on fuzzy name similarity,
- the source is derived from another provider with known false positives,
- the provider field is a slug rather than a documented stable ID,
- date of birth is missing for a player or coach,
- team country or competition context is missing,
- a bridge conflicts with an existing stronger bridge.

## Practical Rule

When in doubt, make the matcher produce evidence rather than a write. A good candidate
queue is progress. A bad automatic bridge is debt.

## Threshold Examples

| Scenario                                                                                    | Suggested confidence | Why                                                        |
| ------------------------------------------------------------------------------------------- | -------------------: | ---------------------------------------------------------- |
| Wikidata QID has a non-deprecated Transfermarkt player ID and target entity type is player. |                `1.0` | Direct typed public bridge.                                |
| SportMonks player has `transfermarkt_id` that resolves to one live player.                  |                `1.0` | Provider-supplied direct bridge via a strong hub.          |
| FotMob player has exact DOB plus normalised full name and no competing candidates.          |               `0.95` | Strong biographical evidence, but no bridge.               |
| Team has exact normalised name plus country and founded year.                               |               `0.95` | Strong team signal when uniqueness holds.                  |
| FBref-to-Transfermarkt community bridge with known false positives but DOB agrees.          |               `0.95` | Derived bridge upgraded by independent biographical check. |
| Name plus nationality for a player with missing DOB.                                        |               `0.90` | Candidate evidence, not enough for automatic public write. |
| Name-only club match.                                                                       |               `0.80` | Candidate only; club names collide globally.               |
| Slug similarity or token overlap.                                                           |              `<0.80` | Search/discovery evidence, not identity evidence.          |

## Downgrade Rules

Downgrade or route to review when:

- the source bridge is derived rather than direct,
- the provider has a documented false-positive rate,
- the provider record lacks entity type,
- the candidate is one of several plausible matches,
- the source field is a slug or display label,
- the match depends on current-team context that may be stale.

## Upgrade Rules

Upgrade only when independent evidence agrees. For example, a derived bridge plus exact
DOB/name can become an auto-write candidate. Two weak name-only signals should not
automatically become strong evidence unless they are independent and disambiguating.
