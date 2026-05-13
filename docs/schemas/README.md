---
doc_type: schema_reference
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: schemas
stance: descriptive
contribution_model: maintainer_doctrine
---

# Reference Register Schema

The SQL file at [`schemas/reference-register.sql`](../../schemas/reference-register.sql)
is an optional SQLite-shaped reference schema for examples and small deployments. It is
not the Reep Next storage model, not a public release export contract, and not an ID
allocator.

Use it when you want a compact schema for trying the toolkit's matching, provenance, and
review patterns. If you already have your own player, team, match, or provider-ID
tables, keep them and map the toolkit concepts onto your own storage model.

## Tables

| Table             | Purpose                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------- |
| `entities`        | Canonical register entities: player, team, coach, competition, season, and match.       |
| `provider_ids`    | Provider bridges with source, confidence, method, snapshot, matcher, and review status. |
| `aliases`         | Provider-sourced name variants with language and snapshot provenance.                   |
| `matches`         | Match identity fields used for fixture-level resolution.                                |
| `match_decisions` | Review outcomes for proposed match/provider links.                                      |

## Identity Boundary

The schema deliberately uses neutral `entity_id` names rather than Reep-specific ID
allocation. A project can mint IDs however it wants, as long as references remain stable
and retired/merged entities preserve lineage through `canonical_entity_id` and
`deleted_at`.

Provider IDs are stored separately from entity rows because a provider bridge is
evidence, not the entity itself. This also makes duplicate-provider-ID checks and
confidence-aware updates easier to run.

## Lineage Fields

Provider bridge rows should record:

- `source`: where the bridge came from;
- `confidence`: the matching confidence at write time;
- `method`: the matcher or review path;
- `source_snapshot`: the source snapshot or export label;
- `matcher_version`: the matcher or template version;
- `review_status`: whether the row was auto-accepted, reviewed, deferred, or rejected.

These fields are intentionally plain text. Production systems may normalise them into
separate evidence and action-ledger tables, but the reference schema keeps the shape
small enough to understand and copy.

## Match Decisions

`match_decisions` captures the output of a review step before it becomes a bridge or is
rejected. It is useful for examples where a match candidate has enough evidence to
inspect but not enough to write automatically.

Valid decisions are:

- `accepted`
- `rejected`
- `needs_more_evidence`
- `new_entity_candidate`

## Smoke Test

The schema should load into SQLite without errors:

```bash
sqlite3 :memory: < schemas/reference-register.sql
```

Projects using Postgres, MySQL, DuckDB, or a document store should treat this file as a
conceptual model rather than a migration to run unchanged.
