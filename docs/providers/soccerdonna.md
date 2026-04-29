---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: soccerdonna
entity_types: [player, team, coach, competition, match]
access_tier: public_grey
source_kind: living
authority_role: bridge_spine
bridge_providers: [wikidata, transfermarkt]
matching_fields:
  [soccerdonna_id, name, date_of_birth, nationality, country, competition_code, team_id]
confidence_floor: 1.0
private_dependencies: []
---

# Soccerdonna

Soccerdonna is a women's-football specialist with Transfermarkt-like concepts: players,
coaches, clubs, competitions, transfers, and match reports. It is one of the
highest-value sources for women's football identity work.

## Why It Matters Before You Start

Many generic football providers are thinner for women's football. Soccerdonna often has
the dedicated IDs, squad context, and competition coverage needed to resolve players and
teams safely.

It is also a strong scope signal: a Soccerdonna player/team bridge usually means the
entity belongs to women's football, but coach gender must not be inferred from
Soccerdonna alone.

## Entity Model

| Entity type | Soccerdonna term             | ID shape  | Notes                                         |
| ----------- | ---------------------------- | --------- | --------------------------------------------- |
| Player      | Spielerin                    | numeric   | Women's player profile.                       |
| Coach       | TrainerIn                    | numeric   | Separate from player namespace.               |
| Club/team   | Verein / Mannschaft          | numeric   | Parent club and team-section concepts matter. |
| Competition | Wettbewerb / Pokalwettbewerb | code      | Codes are provider-specific.                  |
| Match       | Spielbericht                 | numeric   | Match report ID.                              |
| Season      | URL/form parameter           | year-like | Endpoint shape differs for leagues and cups.  |

## Matching Surface

| Field            | Use                                      | Gotcha                                               |
| ---------------- | ---------------------------------------- | ---------------------------------------------------- |
| Soccerdonna ID   | Strong bridge when entity type is clear. | Separate player and coach namespaces.                |
| Name             | Display and alias evidence.              | Accents and localisation matter.                     |
| Date of birth    | Strong player/coach signal.              | Often only present on profile detail pages.          |
| Nationality      | Corroboration.                           | Translate/normalise country labels.                  |
| Team/club IDs    | Team context.                            | Parent club and sub-team IDs need careful modelling. |
| Competition code | Competition bridge.                      | Codes are not reliably derivable from country/name.  |

## Reep-Style Linking Advice

- Treat Soccerdonna IDs as first-class women's-football bridges.
- Use Soccerdonna as a women-only prior for players and teams, but do not infer coach
  gender from it.
- Fetch profile-level DOB before relying on biographical matching.
- Model club/team sections explicitly enough to avoid merging senior, youth, and
  parent-club entities.
- Verify competition codes from source pages rather than guessing them.

## Gotchas

- DOB is not always present on squad listings; profile pages matter.
- League and cup endpoints can have different historical-season mechanics.
- Country names and labels may be German even on English paths.
- Parent club and team-section concepts are distinct.
- Coach gender is absent; recover through another reliable source.

## References

- [Soccerdonna](https://www.soccerdonna.de/)
- Wikidata [P4381](https://www.wikidata.org/wiki/Property:P4381),
  [P8134](https://www.wikidata.org/wiki/Property:P8134),
  [P7878](https://www.wikidata.org/wiki/Property:P7878)
- [Transfermarkt](transfermarkt.md)
