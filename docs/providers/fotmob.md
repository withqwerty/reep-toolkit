---
doc_type: provider_card
content_lane: reference
status: review_ready
public_safe: true
last_verified: 2026-04-29
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: fotmob
entity_types: [player, team, coach, competition, match]
access_tier: public_grey
source_kind: living
authority_role: metadata_source
bridge_providers: []
matching_fields:
  [fotmob_id, name, date_of_birth, nationality, country, team_id, league_id, match_id]
confidence_floor: 0.95
private_dependencies: []
---

# FotMob

FotMob is a consumer football app with broad active coverage. It reaches teams and
leagues that are awkward elsewhere, but it exposes no cross-provider bridge IDs.

## Why It Matters Before You Start

FotMob matching is signal-based. That makes DOB, name, nationality, team, and country
context the difference between a strong candidate and a false positive.

## Entity Model

| Entity type | ID shape          | Notes                                                      |
| ----------- | ----------------- | ---------------------------------------------------------- |
| Player      | numeric           | Stable app/site player ID.                                 |
| Team        | numeric           | Stable team ID.                                            |
| Coach       | numeric           | Separate namespace from player despite same numeric shape. |
| League      | numeric           | Competition-like entity.                                   |
| Match       | numeric           | Match URL includes slug plus numeric ID.                   |
| Season      | label/year in URL | Not usually a first-class entity ID.                       |

## Matching Surface

| Field           | Use                           | Gotcha                                                  |
| --------------- | ----------------------------- | ------------------------------------------------------- |
| FotMob ID       | Provider bridge once matched. | No public Wikidata property at time of draft.           |
| Name            | Primary player/team signal.   | Non-Latin primary names can appear.                     |
| Date of birth   | Strong player signal.         | Missing for some lower-tier players.                    |
| Nationality     | Corroboration.                | Usually primary nationality only.                       |
| Team/league IDs | Context.                      | Current-team data can drift during loans and transfers. |

## Reep-Style Linking Advice

- Use DOB plus normalised name for players when available.
- Use name plus country for teams.
- Route DOB-less player matches to review unless another strong source corroborates
  them.
- Store FotMob aliases; they preserve transliterations and improve later matching.
- Do not mint from name-only FotMob records.

## Safe Use Matrix

| Task             | Recommended use                                       | Review trigger                                      |
| ---------------- | ----------------------------------------------------- | --------------------------------------------------- |
| Player bridge    | DOB plus normalised name, with uniqueness check.      | Missing DOB, abbreviated name, or multiple matches. |
| Team bridge      | Name plus country/category and provider team ID.      | Same display name in multiple countries or levels.  |
| Coach bridge     | Coach-specific ID plus DOB or strong role context.    | Player/coach numeric namespace confusion.           |
| Match bridge     | Numeric match ID after teams/date resolve.            | Event page without resolved fixture identity.       |
| Alias harvesting | Store provider names and transliterations as aliases. | Alias conflicts with stronger known name.           |

## Do Not Do

- Do not mint from a name-only FotMob record.
- Do not use current team as a replacement for DOB.
- Do not assume FotMob exposes cross-provider IDs.
- Do not merge coach and player IDs just because both are numeric.

## Useful Examples

- [FotMob signal-only player match](../examples/fotmob-signal-only-player.md).
- [Provider ingest walkthrough](../examples/provider-ingest-walkthrough.md).
- [Review weak matches](../examples/review-weak-matches.md).

## Gotchas

- No deterministic bridge path means false positives are the main risk.
- Position labels can differ between endpoints.
- Coach IDs and player IDs are separate even if both are numeric.
- API shape is public but not formally documented as a stable ingestion surface.

## References

- [FotMob](https://www.fotmob.com/)
- [worldfootballR](https://github.com/JaseZiv/worldfootballR)
