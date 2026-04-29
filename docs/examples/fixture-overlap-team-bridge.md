---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [team, match]
matching_fields: [team_name, fixture_date, opponent, provider_id, overlap_ratio]
confidence_floor: 0.95
failure_mode: missing_direct_team_bridge
decision: [auto_write_if_unique, review_if_ambiguous]
search_tags: [team, fixture-overlap, corroboration]
---

# Fixture-Overlap Team Bridge

This example shows how fixture behaviour can corroborate a team bridge when direct
cross-provider IDs are missing and name-only matching is not acceptable.

## Situation

The register has a team with strong evidence from two sources:

| entity_id | name        | provider | external_id |
| --------- | ----------- | -------- | ----------- |
| `t_001`   | Northbridge | opta     | opta_team_1 |
| `t_001`   | Northbridge | wikidata | Q1001       |

The team has no Transfermarkt bridge. A Transfermarkt-like fixture source has a possible
team:

| candidate_provider_id | candidate_name |
| --------------------- | -------------- |
| `tm_501`              | Northbridge FC |

Name similarity alone is not enough to write the bridge.

## Fixture Evidence

Compare known register fixtures against the candidate provider's fixture list:

| date       | register fixture             | candidate fixture             | Match? |
| ---------- | ---------------------------- | ----------------------------- | ------ |
| 2026-08-10 | Northbridge v East City      | Northbridge FC v East City    | yes    |
| 2026-08-17 | South Town v Northbridge     | South Town v Northbridge FC   | yes    |
| 2026-08-24 | Northbridge v West Athletic  | Northbridge FC v West Ath.    | yes    |
| 2026-08-31 | River County v Northbridge   | River County v Northbridge FC | yes    |
| 2026-09-07 | Northbridge v Central United | Northbridge FC v Central Utd  | yes    |

The overlap is high, date-aligned, and unique among candidate teams.

## Decision Rule

Write only if:

- the candidate team name is compatible,
- fixture overlap exceeds the configured threshold,
- opponents resolve to the same register teams,
- home/away roles are consistent enough for the provider,
- no other candidate team has comparable overlap,
- the provider ID is not already attached to another same-type entity.

## Write Set

```text
entity_id: t_001
provider: transfermarkt
external_id: tm_501
confidence: 0.95
method: fixture-list-overlap
overlap_ratio: 1.00
source_snapshot: transfermarkt-fixtures-2026-04-29
```

## Review Route

Route to review instead when:

- overlap is high but two teams share the same fixture pattern,
- opponents are unresolved,
- only one or two fixtures overlap,
- the provider fixture list is incomplete,
- the candidate provider ID already belongs to another team.

## Doctrine Demonstrated

- Behavioural evidence can corroborate identity without weakening name-only doctrine.
- Fixture overlap is strongest when opponents also resolve.
- A team bridge should not be written from display name alone.
- The final provider-ID collision check still gates the write.
