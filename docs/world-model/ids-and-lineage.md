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
matching_fields: [provider_id, alias, source_snapshot, matcher_version]
---

# IDs and Lineage

A register earns trust when its IDs remain stable.

## Stable Register IDs

A register assigns one stable ID per entity and preserves that ID across refreshes. The
exact format is a project choice. A typed prefix helps logs, exports, and support
tickets, but the format is less important than the invariant:

> Once an ID is published, it should continue to resolve to the same real-world entity.

If two register entities are later found to be the same real-world entity, prefer a
redirect or alias relationship over deleting a public ID.

## Provider IDs

Provider IDs are external identifiers attached to register entities.

Recommended columns:

| Field                       | Purpose                                                 |
| --------------------------- | ------------------------------------------------------- |
| `entity_id`                 | Stable register ID.                                     |
| `provider`                  | Canonical provider namespace, such as `transfermarkt`.  |
| `external_id`               | Provider-native ID.                                     |
| `entity_type`               | Optional denormalised guard for validation and exports. |
| `source`                    | How the mapping was created.                            |
| `confidence`                | Routing label for write/review policy.                  |
| `method`                    | Matcher or bridge method.                               |
| `source_snapshot`           | Exact upstream snapshot or version.                     |
| `matcher_version`           | Version of the matching logic.                          |
| `created_at` / `updated_at` | Audit timestamps.                                       |

## Derived Versus Curated Bridges

Some bridges are derived from a source that can be rebuilt, such as Wikidata external-ID
claims. Others are curated by matchers, operators, or review queues.

Keep these concepts distinguishable. A rebuildable derived bridge should not overwrite a
curated bridge unless policy explicitly allows it.

## Aliases

Aliases are names observed from provider records. They improve search and future
matching, but an alias is not identity proof by itself.

Store:

- alias text,
- provider,
- language if known,
- source snapshot,
- first seen timestamp.

## Redirects and Soft Deletes

When a public ID must be retired, retain a redirect:

```text
old_entity_id -> canonical_entity_id
reason: duplicate_merge
retired_at: 2026-04-29T00:00:00Z
```

Consumers can keep resolving old IDs while discovering the canonical entity.
