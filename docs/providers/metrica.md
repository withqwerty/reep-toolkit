---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: metrica
entity_types: [player, team, match]
access_tier: mixed
source_kind: living
authority_role: coverage_probe
bridge_providers: []
matching_fields: [sample_game_id, player_number, team_label]
confidence_floor: 0.0
private_dependencies: []
---

# Metrica Sports

Metrica Sports publishes a small anonymised tracking sample and offers commercial
tracking/video products. The public sample is valuable for learning tracking formats,
but it is not an entity-resolution source because people and teams are anonymised.

## Entity Model

| Entity type | Metrica public sample term | ID shape         | Notes                            |
| ----------- | -------------------------- | ---------------- | -------------------------------- |
| Player      | Player_ID                  | per-match number | Anonymised; not a person bridge. |
| Team        | Home/Away                  | sample label     | Anonymised; not a team bridge.   |
| Match       | Game_ID                    | sample key       | Sample dataset key only.         |

## Matching Surface

| Field            | Use                | Gotcha                                 |
| ---------------- | ------------------ | -------------------------------------- |
| Player_ID        | Format example.    | Not stable across real-world identity. |
| Home/Away labels | Format example.    | No club identity.                      |
| Game_ID          | Sample reference.  | Not a public match bridge.             |
| Tracking frames  | Analytics context. | Never identity evidence.               |

## Reep-Style Linking Advice

- Do not use the public Metrica sample for player, team, or match bridges.
- Use it only as a parser/format reference.
- If a commercial Metrica feed supplies real roster metadata, apply the normal provider
  identity gates rather than reusing the public-sample assumptions.

## Gotchas

- Open sample rows are deliberately anonymised.
- Player numbers are sample-local, not provider identity.
- Multiple tracking formats exist; keep parser assumptions separate from identity logic.

## References

- [Metrica Sports](https://metrica-sports.com/)
- [Metrica sample data](https://github.com/metrica-sports/sample-data)
- [kloppy](https://github.com/PySport/kloppy)
