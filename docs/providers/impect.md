---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: impect
entity_types: [player, team, coach, competition, season, match]
access_tier: paid_or_private
source_kind: mixed
authority_role: corroborator
bridge_providers: [wyscout, skillcorner, worldfootball]
matching_fields:
  [
    impect_id,
    wyscout_id,
    skillcorner_id,
    heimspiel_id,
    name,
    date_of_birth,
    nationality,
    current_team,
  ]
confidence_floor: 0.95
private_dependencies: []
---

# Impect Ecosystem

Impect is most useful for identity work when it arrives as a bundled provider surface:
Impect IDs alongside Wyscout, SkillCorner, and heim:spiel / WorldFootball-style IDs. The
public lesson is not the private export itself; it is the pattern of one
well-corroborated person row yielding several provider-scoped bridges.

## Why It Matters Before You Start

Bundled provider exports are powerful and risky. They can collapse several bridge
backfills into one pass, but only if the bundle's identity row is trustworthy and every
provider column is written with clear source provenance.

## Entity Model

| Provider family            | Main identity surface                               | Notes                                                             |
| -------------------------- | --------------------------------------------------- | ----------------------------------------------------------------- |
| Impect                     | Player and match/event keys in licensed deliveries. | Treat keys as provider-scoped and delivery-scoped until audited.  |
| Wyscout                    | Player, team, competition, season, match IDs.       | Strong provider keys, but ontology can differ from your register. |
| SkillCorner                | Tracking player/team/match keys.                    | Strong match/roster relationship evidence.                        |
| heim:spiel / WorldFootball | Person/team/competition/match IDs or URL keys.      | Legacy slug and newer numeric forms can coexist.                  |

## Matching Surface

| Field                         | Use                              | Gotcha                                             |
| ----------------------------- | -------------------------------- | -------------------------------------------------- |
| Impect person key             | Provider bridge candidate.       | Confirm stability across deliveries.               |
| Wyscout ID                    | Additional provider bridge.      | Carry entity type; numeric IDs can be type-scoped. |
| SkillCorner ID                | Tracking-provider bridge.        | Roster evidence still needs person corroboration.  |
| heim:spiel / WorldFootball ID | Public-history bridge candidate. | Legacy slug and numeric forms differ.              |
| DOB + name + nationality      | Bundle acceptance gate.          | Do not trust a multi-ID row on name alone.         |
| Current team                  | Weak context.                    | Point-in-time and free-text in some exports.       |

## Bridge Surface

| Bridge route                                  | Use                                                | Caution                                                       |
| --------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------- |
| Impect bundle row → multiple provider bridges | Efficient bridge fan-out after person gate passes. | Write each provider bridge separately with bundle provenance. |
| Wyscout standalone → register                 | Strong provider keys plus DOB/name/team evidence.  | Country and area codes may be provider-specific.              |
| SkillCorner standalone → register             | Match/roster relationship evidence.                | Not enough for person identity without attributes.            |
| WorldFootball-style IDs → register            | Public history and alias evidence.                 | Legacy and newer ID schemes need separate handling.           |

## Reep-Style Linking Advice

- Treat the bundle row as evidence, not as a magic merge instruction.
- Gate person matches on DOB plus normalised name before writing the fan-out bridges.
- Write one bridge row per provider namespace with the bundle as source provenance.
- Keep Wyscout, SkillCorner, and heim:spiel IDs distinct even when they arrive together.
- Do not turn current-team text into a membership edge without date and source context.

## Gotchas

- Bundled exports can be customer-shaped; confirm key stability before using as durable
  bridges.
- Wyscout IDs are provider-scoped and entity-type-scoped.
- Wyscout country/area codes can be provider-specific rather than ISO/FIFA.
- SkillCorner relationship evidence is match/roster-grain unless another source says
  otherwise.
- WorldFootball-style identifiers can have legacy slug and newer numeric forms.

## References

- [Impect](https://www.impect.com/)
- [Wyscout](https://wyscout.com/)
- [SkillCorner](skillcorner.md)
- [WorldFootball.net](https://www.worldfootball.net/)
- [Wikidata P2020](https://www.wikidata.org/wiki/Property:P2020)
- [kloppy](https://github.com/PySport/kloppy)
