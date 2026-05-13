---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: skillcorner
entity_types: [player, team, match]
access_tier: mixed
source_kind: living
authority_role: corroborator
bridge_providers: [impect]
matching_fields: [skillcorner_id, name, team_id, match_id, position, shirt_number]
confidence_floor: 0.95
private_dependencies: []
---

# SkillCorner

SkillCorner provides tracking and physical-data products built from football video. For
identity resolution, its provider IDs are most useful when they arrive with match, team,
roster, and delivery metadata that can be linked back to an existing register.

## Why It Matters Before You Start

Tracking providers often expose strong match and roster context without enough
biographical detail to identify a person safely on their own. SkillCorner rows should
usually be treated as relationship evidence or provider-scoped bridges, then
corroborated with another attribute authority.

## Entity Model

| Entity type | SkillCorner term        | ID shape                   | Notes                                                               |
| ----------- | ----------------------- | -------------------------- | ------------------------------------------------------------------- |
| Player      | player                  | provider key               | Strongest when paired with roster attributes and delivery snapshot. |
| Team        | team                    | provider key               | Usually match-contextual.                                           |
| Match       | match                   | provider key               | Strong bridge when fixture metadata agrees.                         |
| Competition | competition             | provider key where present | Secondary to delivery scope; audit before using structurally.       |
| Season      | season/delivery context | provider-scoped            | Keep scoped to snapshot until audited.                              |

## Matching Surface

| Field                     | Use                        | Gotcha                                                        |
| ------------------------- | -------------------------- | ------------------------------------------------------------- |
| Provider player key       | Provider bridge candidate. | Needs name/team/shirt/position and external attributes.       |
| Provider match key        | Match bridge candidate.    | Confirm date, competition, teams, and delivery snapshot.      |
| Provider team key         | Team context.              | Match-level team IDs may not be enough for season membership. |
| Shirt number and position | Relationship evidence.     | Helpful but not person identity proof.                        |
| Tracking samples          | Context.                   | Not an identity attribute.                                    |

## Bridge Surface

| Bridge route                             | Use                                                                   | Caution                                                     |
| ---------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------- |
| SkillCorner via Impect bundle            | Efficient multi-provider player bridge where the bundle is available. | Keep Impect-derived provenance explicit.                    |
| SkillCorner standalone player → register | Provider key plus roster and external person attributes.              | Review if DOB or stronger person attribute is absent.       |
| SkillCorner match → register match       | Fixture metadata plus match key.                                      | Delivery metadata can be more reliable than display labels. |

## Reep-Style Linking Advice

- Treat SkillCorner player IDs as provider-scoped.
- Do not mint people from tracking roster rows without a person attribute authority.
- Preserve delivery snapshot metadata with every candidate.
- Use match and team context to narrow candidates, not to replace DOB/name evidence.
- Keep matchday roster evidence separate from season membership.

## Gotchas

- Tracking rosters can be strong relationship evidence but weak person evidence.
- Match-level delivery data is not proof of a season-long membership edge.
- Position can be frame-, phase-, or role-derived depending on product.
- Open samples are useful for format familiarity, not coverage claims.

## References

- [SkillCorner](https://www.skillcorner.com/)
- [SkillCorner Open Data](https://github.com/SkillCorner/opendata)
- [kloppy](https://github.com/PySport/kloppy)
- [Impect ecosystem](impect.md)
