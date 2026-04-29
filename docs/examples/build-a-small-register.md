---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [player, team, match]
failure_mode: register_bootstrap
decision: [document]
search_tags: [small-register, schema, bootstrap]
---

# Build a Small Register

This example starts with a minimal SQLite register.

## 1. Create Core Tables

Use the reference schema in `schemas/reference-register.sql`, or create a smaller
subset:

```sql
CREATE TABLE entities (
  entity_id TEXT PRIMARY KEY,
  entity_type TEXT NOT NULL,
  name TEXT NOT NULL,
  date_of_birth TEXT,
  country TEXT,
  canonical_entity_id TEXT,
  deleted_at TEXT
);

CREATE TABLE provider_ids (
  entity_id TEXT NOT NULL,
  provider TEXT NOT NULL,
  external_id TEXT NOT NULL,
  confidence REAL NOT NULL,
  method TEXT NOT NULL,
  source_snapshot TEXT,
  matcher_version TEXT,
  PRIMARY KEY (entity_id, provider, external_id)
);
```

## 2. Seed Trusted Entities

Start from a source you can justify. For a public prototype, Wikidata plus a narrow
manually reviewed CSV is often safer than trying to ingest every provider at once.

## 3. Implement a Registry

Your registry only needs bridge and signal lookup methods. Keep ambiguity rejection
inside the registry.

## 4. Run Provider Matchers

Run matchers against snapshots, not live responses. Inspect unmatched and weak matches
before writing.

## 5. Export

Export stable IDs, provider bridges, aliases, and lineage. Do not export raw
paid-provider payloads unless your licence allows it.
