---
doc_type: world_model
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: world-model
stance: descriptive
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, match]
confidence_floor: 0.95
matching_fields: [provider_id, name, date_of_birth, nationality, country]
---

# Confidence and Validation

Confidence should be treated as a routing label, not as a mathematically calibrated
probability. This page defines the model; the opinionated Reep-style write policy lives
in [matching thresholds](../guides/matching-thresholds.md).

## Routing Bands

| Confidence | Meaning                                                                           | Default action                            |
| ---------- | --------------------------------------------------------------------------------- | ----------------------------------------- |
| `1.0`      | Direct bridge from a trusted source or exact same provider namespace.             | Auto-write if uniqueness checks pass.     |
| `0.95`     | Strong identity match, usually provider ID plus DOB/name or unambiguous DOB/name. | Auto-write if ambiguity is rejected.      |
| `0.90`     | Useful bridge or signal with known caveats.                                       | Review unless independently corroborated. |
| `0.80`     | Weak signal such as name-only or loose derived mapping.                           | Candidate only. Never auto-write.         |
| `<0.80`    | Discovery or search signal.                                                       | Do not write.                             |

## Ambiguity Rejection

A matcher should prefer no match over a wrong match. If a lookup returns two plausible
candidates, return no automatic match and route the record to review.

Examples:

- Two players with same normalised name and DOB.
- Two clubs with same name in the same country.
- A match found by date and teams, but with multiple competitions on that date.

## Strong Signals

Strong signals usually include:

- direct provider bridge,
- Wikidata QID plus corroborating entity type,
- Transfermarkt player ID plus DOB/name agreement,
- date of birth plus normalised full name for players,
- name plus country plus founded year for teams,
- date plus resolved home and away teams for matches.

## Weak Signals

Weak signals include:

- name-only matches,
- initials or single-token names,
- nationality-only corroboration,
- provider slugs without a documented stability guarantee,
- fan-maintained bridge datasets with known false positives,
- fuzzy string matches without independent evidence.

## Human Review

Review queues should preserve the evidence bundle:

- source record,
- proposed target,
- match method,
- confidence label,
- conflicting candidates,
- source snapshot,
- reviewer decision,
- reviewer notes.

Rejected candidates are data. Keep them so future reruns do not re-propose the same bad
match.
