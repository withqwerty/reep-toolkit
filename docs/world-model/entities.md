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
matching_fields:
  [
    provider_id,
    name,
    date_of_birth,
    nationality,
    country,
    match_date,
    home_team,
    away_team,
  ]
---

# Entity Model

A football identity register should model only identity-bearing objects. Event payloads,
stats, odds, salaries, tracking samples, and standings can reference the register, but
they should not be part of the register itself.

## Core Entity Types

| Type          | Meaning                                               | Common identity signals                                                               |
| ------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `player`      | A person as a player identity.                        | Provider IDs, name, date of birth, nationality, position, current or historical team. |
| `coach`       | A person as a coach/manager identity.                 | Provider IDs, name, date of birth when available, nationality, team history.          |
| `team`        | A club, national team, academy side, or women's team. | Provider IDs, name, country, founded year, gender/competition context.                |
| `competition` | A tournament or league family.                        | Provider IDs, name, country/region, organiser, gender, level.                         |
| `season`      | A concrete competition edition, stage, or cycle.      | Provider IDs, competition, date span, stage label, parent season.                     |
| `match`       | A real-world fixture.                                 | Provider IDs, date, home team, away team, competition, season, kickoff time.          |

## Person Identities

Player and coach records can refer to the same human, but they are often separate
operational identities. A public register can either:

- keep player and coach as separate entity types with optional cross-links, or
- use a shared `person` table plus role-specific projections.

The first approach is simpler for provider matching because most providers expose player
IDs and coach IDs in separate namespaces.

## Team Identities

Team names collide constantly. A safe team identity normally needs at least one of:

- a provider bridge,
- name plus country,
- name plus competition context,
- name plus founded year,
- name plus gender/team-category context.

Do not assume a club name is globally unique.

## Competition Identities

Competition providers disagree about whether they identify:

- the competition family,
- the season edition,
- a stage,
- a draw group,
- a cup round,
- or a broadcast/product bucket.

Provider docs should say exactly which level the provider ID represents.

## Match Identities

A match is not the raw event feed. It is the fixture identity that event feeds, stats
feeds, odds feeds, and line-up feeds can all reference. The usual identity spine is:

```text
match_date + home_team_id + away_team_id [+ competition_id] [+ season_id]
```

Kickoff time helps, but it is not always stable across postponements, time-zone bugs,
and provider updates.
