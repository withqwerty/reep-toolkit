---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [match, team, competition, season]
matching_fields: [match_date, home_team, away_team, competition, season, provider_id]
confidence_floor: 0.95
failure_mode: event_payload_without_identity
decision: [match_by_fixture_signals]
search_tags: [match, fixture, teams-date]
---

# Match Fixture Identity

A match identity row is not an event payload. It is the stable fixture object that
event, odds, line-up, and stats feeds can all reference.

## Source Fixture

```json
{
  "provider": "example_events",
  "match_id": "evt-7788",
  "date": "2026-02-14",
  "home_team_provider_id": "home-10",
  "away_team_provider_id": "away-20",
  "competition": "Premier League"
}
```

## Resolve Teams First

| Provider team ID | Register team | Method |
| ---------------- | ------------- | ------ |
| `home-10`        | `t_arsenal`   | bridge |
| `away-20`        | `t_chelsea`   | bridge |

## Match Lookup

Search:

```text
match_date = 2026-02-14
home_team_id = t_arsenal
away_team_id = t_chelsea
competition_id = c_premier_league
```

Candidate:

| match_id | date       | home        | away        | competition        |
| -------- | ---------- | ----------- | ----------- | ------------------ |
| `m_001`  | 2026-02-14 | `t_arsenal` | `t_chelsea` | `c_premier_league` |

## Decision

| Method                   | Outcome                                     | Confidence | Write? |
| ------------------------ | ------------------------------------------- | ---------: | ------ |
| `date+teams+competition` | attach `example_events:evt-7788` to `m_001` |     `0.95` | yes    |

## Bad Shortcut

Do not mint a new match only because an event payload has a new `match_id`. First check
whether the fixture already exists by date and resolved teams.

## Reep-Style Lesson

Match matching composes registries: provider teams resolve to register teams, then the
fixture resolves to a register match. Raw events attach after identity is settled.
