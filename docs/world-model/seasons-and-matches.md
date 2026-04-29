---
doc_type: world_model
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: world-model
stance: descriptive
contribution_model: maintainer_doctrine
entity_types: [competition, season, match, team]
matching_fields: [provider_id, match_date, home_team, away_team, competition, season]
---

# Seasons and Matches

Season and match modelling is where provider world models diverge most sharply.

## Competition Versus Season

A competition is the continuing tournament identity. A season is a concrete edition,
stage, or cycle of that competition.

Examples:

- Competition: Premier League.
- Parent season: 2024-25 Premier League.
- Leaf season or stage: regular season, play-off, apertura, clausura, group stage,
  knockout stage.

Not every provider has all levels. Provider docs should state the level their IDs
identify.

## Parent and Leaf Seasons

A register can support both:

```text
competition
  -> parent season
      -> leaf season / stage
```

This handles competitions where providers disagree about whether a season means the
whole cycle or a stage inside it.

## Match Identity

A match record should carry the minimum fields needed to resolve the same real-world
fixture across providers:

- match date,
- kickoff time when known,
- home team register ID,
- away team register ID,
- competition register ID when known,
- season register ID when known,
- provider bridges.

Raw event, tracking, shot, odds, and box-score payloads should live outside the identity
register and reference the match ID.

## Postponements and Replays

Do not rely on kickoff time alone. Dates and times can move, and providers can report
local time, UTC, or stale scheduled time. Store both scheduled and observed values when
a provider makes that distinction.

## Cup Edge Cases

Cup competitions need extra care:

- neutral venues can make home/away semantics provider-specific,
- two-legged ties are not the same as aggregate ties,
- replays and abandoned matches can share teams and round labels,
- preliminary rounds can have different provider coverage from main rounds.
