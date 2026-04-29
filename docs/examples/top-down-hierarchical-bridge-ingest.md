---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
provider: hierarchical_fixture_provider
entity_types: [competition, season, stage, team, match, player]
matching_fields: [provider_id, season, stage, team_id, match_date, alias]
confidence_floor: 0.95
failure_mode: parent_blocked_downstream_deferrals
decision: [apply_level_order, rerun_audit]
search_tags: [hierarchy, deferrals, competitions, seasons, teams, matches]
---

# Top-Down Hierarchical Bridge Ingest

This example shows why a provider with competitions, seasons, stages, teams, matches,
and players should be ingested top-down instead of as one flat bridge pass.

## Situation

A provider exposes this hierarchy:

```text
competition -> season -> stage -> team participation -> match -> player
```

The first audit finds strong rows at every level, but also finds a small number of
competition reviews.

| Entity type | Strong | Review | Reject |   Defer |
| ----------- | -----: | -----: | -----: | ------: |
| competition |     45 |     15 |      4 |       0 |
| season      |    820 |     42 |    129 |     395 |
| stage       |  1,469 |      0 |      0 |   1,548 |
| team        |    535 |    203 |  1,260 |       0 |
| match       | 52,037 |      0 | 14,706 | 292,195 |
| player      |  1,448 |     51 |      0 |   8,118 |

The tempting mistake is to apply every strong row and then start weakening match or
player logic to reduce the downstream deferrals.

## Diagnosis

The largest deferral buckets are not independent failures:

| Deferral bucket          | What it really means                                      |
| ------------------------ | --------------------------------------------------------- |
| Season defer             | Parent competition bridge is still review or missing.     |
| Stage defer              | Parent season bridge is not strong yet.                   |
| Team review/reject noise | Season/stage overlap evidence is incomplete.              |
| Match defer              | Home or away team is not strongly bridged yet.            |
| Player defer             | Team-season context is weak, and name-only is not enough. |

The matcher is behaving correctly. The workflow has not settled parent authority.

## Correct Workflow

Apply one level, then rerun the audit:

```text
1. Resolve competition reviews.
2. Apply competition bridges.
3. Rerun audit.
4. Apply season bridges once season review/reject split is clean.
5. Rerun audit.
6. Apply stage bridges.
7. Rerun audit.
8. Apply team bridges with full season/stage context.
9. Rerun audit.
10. Apply match bridges.
11. Rerun audit.
12. Expand player bridges only where another safe identity gate exists.
```

## Bad Fix

```text
if match teams are unresolved:
  try fuzzy team name

if player has no DOB:
  try name + current team
```

This hides a workflow error by weakening identity gates.

## Better Fix

```text
if match teams are unresolved:
  resolve parent competition/season/stage/team bridges first
  rerun match audit

if player has no safe identity gate:
  keep deferred until another provider bridge or carried alias exists
```

## Outcome

After top-level reviews are resolved, many downstream rows change category without any
looser matching:

- seasons stop deferring behind missing competition context;
- stages can attach to strong parent seasons;
- teams gain reliable season-overlap evidence;
- matches can use bridged home and away teams;
- player rows stay conservative rather than falling back to name-only matching.

## Doctrine Demonstrated

- Hierarchical provider ingest is a dependency-ordered graph problem.
- Parent bridges are evidence for child matches.
- Rerun audits between levels.
- Keep parent-blocked deferrals separate from genuine rejects.
- Do not relax lower-level gates to compensate for missing parent context.
