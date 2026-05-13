---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: pff
entity_types: [player, team, match]
access_tier: mixed
source_kind: living
authority_role: corroborator
bridge_providers: []
matching_fields: [pff_id, name, date_of_birth, nationality, team_id, match_id, position]
confidence_floor: 0.95
private_dependencies: []
---

# PFF FC

PFF FC is a football data and analysis provider with a notable public 2022 World Cup
tracking dataset. For identity work, it is useful only when provider IDs arrive with
enough roster metadata to satisfy normal person and match gates.

## Entity Model

| Entity type | PFF term       | ID shape             | Notes                                                    |
| ----------- | -------------- | -------------------- | -------------------------------------------------------- |
| Player      | player         | numeric/provider key | Strongest when paired with DOB or national-team context. |
| Team        | team           | numeric/provider key | Delivery-scoped team key.                                |
| Match       | game/match     | numeric/provider key | Provider match key.                                      |
| Competition | delivery scope | provider context     | Secondary to match metadata.                             |

## Matching Surface

| Field              | Use                        | Gotcha                                             |
| ------------------ | -------------------------- | -------------------------------------------------- |
| Player ID          | Provider bridge candidate. | Not a public cross-provider bridge.                |
| Name and DOB       | Person evidence.           | DOB may be absent in some public metadata shapes.  |
| Nationality        | Corroboration.             | Nationality alone is weak.                         |
| Team and match IDs | Relationship context.      | Do not infer career membership from tracking rows. |
| Position           | Weak corroboration.        | Position labels need mapping.                      |

## Reep-Style Linking Advice

- Use DOB/name/nationality when present before accepting a PFF player bridge.
- Treat tracking rows as matchday relationship evidence, not person identity proof.
- Keep the provider match/team/player namespaces separate.
- Route name-only player rows to review.

## Gotchas

- The public open-data footprint is not the same as commercial coverage.
- Position labels and role codes should be normalised before comparison.
- Ball/player tracking attributes are not identity evidence.

## References

- [PFF FC](https://www.pff.com/fc)
- [PFF 2022 World Cup open dataset](https://www.blog.fc.pff.com/blog/enhanced-2022-world-cup-dataset)
- [kloppy](https://github.com/PySport/kloppy)
