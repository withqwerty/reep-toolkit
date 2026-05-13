---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: providers
stance: descriptive
contribution_model: evidence_required
entity_types: [player, team, coach, competition, season, match]
access_tier: unknown
source_kind: mixed
authority_role: coverage_probe
bridge_providers: []
matching_fields: [provider_id, name, date_of_birth, country, bridge_provider]
confidence_floor: 0.90
private_dependencies: []
---

# Provider Catalogue

This catalogue tracks provider coverage for the guide site. A provider belongs here
before it has a full card when its world model, bridge surface, or ingestion risks
affect register maintenance.

## Full Cards in This Draft

| Provider               | Status       | Role                        | Main value                                                    | Card                                             |
| ---------------------- | ------------ | --------------------------- | ------------------------------------------------------------- | ------------------------------------------------ |
| Wikidata               | review-ready | Bridge spine                | Public QID hub plus external-ID properties.                   | [wikidata.md](wikidata.md)                       |
| Transfermarkt          | review-ready | Bridge spine                | De facto football identity hub.                               | [transfermarkt.md](transfermarkt.md)             |
| Opta / Stats Perform   | review-ready | Commercial authority        | Modern event-data IDs and multiple Opta namespaces.           | [opta.md](opta.md)                               |
| StatsBomb              | review-ready | Event-data corroborator     | Open-data IDs, matches, lineups, teams, and players.          | [statsbomb.md](statsbomb.md)                     |
| SportMonks             | review-ready | Paid API bridge source      | Transfermarkt bridges on many player/team records.            | [sportmonks.md](sportmonks.md)                   |
| WhoScored              | review-ready | Stats-site structure source | Region/tournament/stage/match IDs and Opta-adjacent data.     | [whoscored.md](whoscored.md)                     |
| API-Football           | draft        | Commercial metadata API     | Broad metadata surface without public cross-provider bridges. | [api-football.md](api-football.md)               |
| Capology               | draft        | Salary metadata source      | Salary/contract facts with thin identity evidence.            | [capology.md](capology.md)                       |
| Club Elo               | draft        | Team rating source          | Team-only ratings and historical result context.              | [clubelo.md](clubelo.md)                         |
| FotMob                 | review-ready | Signal-rich app source      | Broad active coverage; no direct bridge IDs.                  | [fotmob.md](fotmob.md)                           |
| FBref                  | review-ready | Public stats bridge         | Stable Sports Reference IDs plus community TM bridge.         | [fbref.md](fbref.md)                             |
| Football-Data.co.uk    | draft        | Results corroborator        | Long-running CSV result and odds archives.                    | [football-data-co-uk.md](football-data-co-uk.md) |
| Fantasy Premier League | draft        | Public PL bridge source     | `code` and `team_code` Opta numeric surfaces.                 | [fpl.md](fpl.md)                                 |
| Livesport ecosystem    | draft        | Public bridge ecosystem     | Soccerway, Flashscore, and BeSoccer identity surfaces.        | [livesport.md](livesport.md)                     |
| TheSportsDB            | review-ready | Community API               | Wikipedia-to-Wikidata bridge and multi-provider fields.       | [thesportsdb.md](thesportsdb.md)                 |
| Soccerdonna            | review-ready | Women's-football specialist | Dedicated women's football player/team/coach IDs.             | [soccerdonna.md](soccerdonna.md)                 |
| SoFIFA                 | draft        | Game metadata source        | Rich player attributes with edition-scoped identity caveats.  | [sofifa.md](sofifa.md)                           |
| Understat              | draft        | xG/stat corroborator        | Match/player-stat context for limited league coverage.        | [understat.md](understat.md)                     |
| SkillCorner            | draft        | Tracking corroborator       | Match/team/player tracking IDs and roster evidence.           | [skillcorner.md](skillcorner.md)                 |
| Impect ecosystem       | draft        | Multi-provider bundle       | Impect, Wyscout, SkillCorner, and heim:spiel bridge fan-out.  | [impect.md](impect.md)                           |

## Queued Cards

| Provider        | Why it matters                   | Likely card focus                                          |
| --------------- | -------------------------------- | ---------------------------------------------------------- |
| Sportec         | Bundesliga/open-data research.   | Match/event/tracking identifiers and competition scope.    |
| PFF FC          | Public tracking/research data.   | Player/team coverage and entity exposure.                  |
| Metrica         | Open tracking samples.           | Anonymous/sample identity limitations.                     |
| Tracab          | Commercial tracking.             | Coverage notes only, limited public identity value.        |
| Second Spectrum | Commercial tracking.             | Coverage notes only, limited public identity value.        |
| Hawk-Eye        | Officiating/tracking ecosystem.  | Mostly ecosystem context.                                  |
| DataFactory     | South American commercial data.  | Regional provider context and access model.                |
| Sportradar      | Commercial multi-sport provider. | Public/private boundary and provider IDs where documented. |

## Card Promotion Criteria

A queued provider becomes a full card when we can document:

- entity types and ID shapes,
- access tier,
- matching-relevant fields,
- bridge paths,
- known failure modes,
- recommended confidence floor,
- public evidence or a redacted maintainer-approved source shape.
