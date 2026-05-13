---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: clubelo
entity_types: [team, match]
access_tier: public_bulk
source_kind: living
authority_role: metadata_source
bridge_providers: []
matching_fields: [clubelo_name, country_code, level, date, home_team, away_team]
confidence_floor: 0.90
private_dependencies: []
---

# Club Elo

Club Elo is a team-only football rating source. For identity work, the important point
is that the team name is effectively the provider key: there is no separate numeric team
ID.

## Entity Model

| Entity type      | Club Elo term | ID shape        | Notes                                          |
| ---------------- | ------------- | --------------- | ---------------------------------------------- |
| Team             | Club          | normalised name | Team name acts as the provider identifier.     |
| Competition/tier | Level         | integer         | Tier within country, not a competition ID.     |
| Fixture          | fixture row   | tuple           | No stable match ID; date/home/away tuple only. |

## Matching Surface

| Field         | Use                | Gotcha                                                      |
| ------------- | ------------------ | ----------------------------------------------------------- |
| `Club`        | Team candidate.    | It is a normalised display name, not a durable numeric key. |
| Country code  | Disambiguation.    | FIFA-style home-nation codes may not equal ISO.             |
| Level         | Team context.      | Useful for tier disambiguation, not a competition bridge.   |
| From/To dates | Snapshot validity. | Ratings are time-series rows.                               |

## Reep-Style Linking Advice

- Use Club Elo for team rating enrichment after team identity is resolved.
- Match teams by exact normalised name plus country first.
- Route same-name or abbreviation cases to review.
- Do not mint matches from fixture tuples unless another source supplies stronger match
  identity.

## Gotchas

- Name-based matching has unavoidable ambiguity.
- Country codes need mapping before comparison with ISO-coded providers.
- Fixture rows have no match ID.
- Ratings update frequently; use snapshot dates for reproducibility.

## References

- [Club Elo](http://clubelo.com/)
- [Club Elo API notes](http://clubelo.com/API)
