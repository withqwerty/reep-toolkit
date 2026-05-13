---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: understat
entity_types: [player, team, competition, season, match]
access_tier: public_grey
source_kind: living
authority_role: corroborator
bridge_providers: [fpl, transfermarkt]
matching_fields: [understat_id, name, team, league_code, season, match_id]
confidence_floor: 0.90
private_dependencies: []
---

# Understat

Understat is a public xG and shot-data site for a limited league set. For identity
resolution, it is useful mainly as a match/player-stat corroborator after stronger
bridges have resolved people and teams.

## Entity Model

| Entity type | Understat term | ID shape             | Notes                                   |
| ----------- | -------------- | -------------------- | --------------------------------------- |
| Player      | player         | numeric              | Stable within Understat.                |
| Team        | team           | numeric/slug context | League-season scoped in many workflows. |
| Competition | league         | string code          | Small fixed league set.                 |
| Season      | season         | year                 | League-scoped.                          |
| Match       | match          | numeric              | Provider match key.                     |

## Matching Surface

| Field               | Use                           | Gotcha                                      |
| ------------------- | ----------------------------- | ------------------------------------------- |
| Player ID           | Provider bridge after review. | Standard public shape lacks DOB.            |
| Player name         | Candidate signal.             | Name-only is weak.                          |
| Team and season     | Context.                      | Team is not a person identity attribute.    |
| League code         | Competition context.          | Provider-specific and limited scope.        |
| Match ID/date/teams | Match candidate.              | Confirm against a canonical fixture source. |

## Reep-Style Linking Advice

- Use Understat player IDs as enrichment/corroboration, not automatic person bridges.
- For Premier League, use FPL/Transfermarkt bridges where available before accepting
  Understat player matches.
- Route non-PL player matches through review unless another DOB/bridge source confirms.
- Do not extrapolate coverage outside the provider's league scope.

## Gotchas

- Standard player fields do not supply DOB or nationality.
- League coverage is narrow by design.
- Team and player names are display labels, not authority labels.
- Historical xG values can change if the provider updates its model.

## References

- [Understat](https://understat.com/)
- [FPL](fpl.md)
