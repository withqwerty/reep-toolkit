---
doc_type: practice_guide
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-30
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
entity_types: [competition, season, stage, team, match, player]
matching_fields: [provider_id, source_key, match, team, season, alias, date_of_birth]
confidence_floor: 0.95
---

# Relationship-Constrained Provider Matching

Provider football data is a graph. A player row, a team row, a match row, and a line-up
row should not be treated as independent matching problems when they point at each
other.

Relationship-constrained matching uses those links as evidence, but never as a shortcut
around identity doctrine. It is useful for event, tracking, scouting, line-up, and
fixture-rich providers such as StatsBomb, Wyscout, Impect, SkillCorner, WhoScored, and
similar sources.

## Core Rule

A provider player ID can become a strong bridge only when both the relationship context
and the identity guard are clean:

1. The provider competition, season, stage, team, or match context is already strongly
   bridged.
2. The provider player appears in that mapped team, match, or team-season context.
3. The candidate register player appears in the same mapped context.
4. The identity guard is clean: exact normalised name or alias, plus DOB when the source
   has DOB.
5. No second plausible candidate remains after the relationship gate.

Relationship-only is not enough. A player named "Alex Silva" who appears for the right
team is still review if the register has two plausible Alex Silvas in the same
team-season or match context.

## Dependency Order

Ingest relationship-rich providers top-down:

```text
competition -> season -> stage -> team -> match -> relationship evidence -> player
```

Do not weaken lower-level player gates because a parent bridge is missing. Resolve the
parent layer, rerun the audit, then reclassify child rows.

## Evidence To Store

Keep final bridges separate from relationship evidence.

| Evidence shape                 | Purpose                                                                |
| ------------------------------ | ---------------------------------------------------------------------- |
| Team-season participation      | Proves a team belongs to a competition season.                         |
| Player-team-season membership  | Proves a player is evidenced with a team in a season.                  |
| Match line-up or appearance    | Proves a player appeared for a team in a mapped match.                 |
| Provider relationship evidence | Stores provider-native row, decision, method, and review/defer reason. |

The final bridge table should still only say "provider ID X resolves to entity Y".
Relationship evidence explains why that statement was safe, or why it stayed in review.

## Provider Source Keys

Provider ID alone is often too small a key. If a source has raw and processed datasets,
competition files, editions, or source variants, keep that discriminator as part of the
relationship evidence key.

Good:

```text
provider = event_source
provider_source_key = processed_2024
provider_match_id = match_123
provider_team_id = team_7
provider_player_id = player_9
```

Risky:

```text
provider = event_source
provider_match_id = match_123
provider_team_id = team_7
provider_player_id = player_9
```

The risky shape collapses evidence when the same upstream match appears in two source
variants with different semantics.

## Strong, Review, Defer, Reject

| Route  | Use when                                                                                        |
| ------ | ----------------------------------------------------------------------------------------------- |
| Strong | Parent context is strong, identity guard is exact, and exactly one candidate survives.          |
| Review | Relationship context is strong but identity is ambiguous, legacy-only, broad, or name-only.     |
| Defer  | A parent bridge is missing, so the child row cannot be judged yet.                              |
| Reject | The local evidence contradicts the candidate, such as DOB mismatch or wrong match/team context. |

Deferral is not negative evidence. It says the provider row is blocked by missing parent
context.

## Alias Handling

Alias parsing should match the register's real storage shape. If historical rows use
pipe-separated aliases and newer rows use comma-separated aliases, split both. Missing
this detail creates false misses and tempts maintainers to add fuzzy matching where
exact alias matching would have worked.

## Legacy Carry-Forward

A legacy bridge is evidence, not authority. It may have been accepted under an older
trust model.

Treat carry-forward-only rows as review unless current local evidence corroborates them:

- target entity type is correct;
- provider row still exists in the current source;
- exact name or alias agrees;
- DOB agrees when available;
- relationship context agrees; and
- same-provider same-type duplicate checks stay clean.

## Duplicate Candidate Surface

Relationship matching can reveal duplicate register entities. For example, a full-name
row and a short-name row can represent the same player if they came from separate mint
paths.

Do not let the provider bridge process pick one by guesswork. Route the row to duplicate
review or merge workflow, then rerun the relationship audit after the canonical row is
settled.

## Validator Rules

Add validators for relationship evidence, not just final bridge rows:

- every referenced register player/team/match/season exists and has the right type;
- a line-up team is one of the match's home or away teams;
- evidence season and competition agree with the mapped match;
- duplicate provider evidence keys are rejected;
- provider source key is part of the uniqueness model when source variants exist;
- accepted rows do not rely on legacy carry-forward alone.

## Public-Safe Example

```text
provider match:
  match_id: ev_match_100
  source_key: open_edition_a
  home_team_id: ev_team_1
  away_team_id: ev_team_2

provider line-up row:
  match_id: ev_match_100
  team_id: ev_team_1
  player_id: ev_player_44
  player_name: Jamie North
  date_of_birth: 2001-04-12

register context:
  ev_team_1 -> team_aaa
  ev_match_100 -> match_bbb
  Jamie North + 2001-04-12 -> one candidate, player_ccc

decision:
  write provider bridge ev_player_44 -> player_ccc
  write line-up evidence with source_key open_edition_a
```

If another `Jamie North` with the same DOB also survives in the same match context, the
decision changes to review. The relationship narrows the search; it does not override
ambiguity.
