---
doc_type: practice_guide
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-06-19
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, stage, match]
matching_fields: [provider_id, namespace, release_stamp, bridge_role]
confidence_floor: 0.95
---

# Use The Reep V1 Public Release

Reep v1 is a release-backed bridge register. Treat the published files as the canonical
public artefact and the API as a convenient lookup layer over the same release.

## Start With The Manifest

Fetch the latest release pointer:

```bash
curl -L https://downloads.reep.football/releases/latest.json
```

The manifest tells you the release stamp, schema version, files, checksums, row counts,
and the redaction policy. Record the release stamp with any analysis you run. If an API
response cites a different release stamp, you are comparing different snapshots.

## Choose The Right Surface

| Need                                      | Use                                            |
| ----------------------------------------- | ---------------------------------------------- |
| Bulk analysis, joins, reproducible checks | CSV files from the release manifest            |
| Local SQL exploration                     | DuckDB bundle from the same release            |
| One-off provider ID lookup                | `/api/v1/resolve/{provider}/{external_id}`     |
| Entity detail by Reep Next ID             | `/api/v1/entities/{reep_id}`                   |
| Public-safe release coverage              | `coverage.csv.gz`, `release.json`, `/coverage` |

Do not scrape the website to build datasets. Use the release files or API.

## Resolve A Provider ID

Provider IDs are namespace-scoped. A bare integer is not enough context: a Transfermarkt
player ID and a Transfermarkt club ID can share the same numeric shape.

```bash
curl -H "Authorization: Bearer $REEP_API_KEY" \
  "https://reep.football/api/v1/resolve/transfermarkt/568177?namespace=spieler&type=player"
```

The response returns Reep Next entity IDs, not v0 `reep_...` IDs. Do not mix v0 IDs and
v1 IDs in the same database table without a migration column that names which register
the ID came from.

## Inspect The Bridge CSV

For bulk work, prefer `csv/bridges.csv.gz`:

```bash
curl -L -o bridges.csv.gz "https://downloads.reep.football/releases/<stamp>/csv/bridges.csv.gz"
python3 - <<'PY'
import csv
import gzip

target = ("transfermarkt", "spieler", "568177")
with gzip.open("bridges.csv.gz", "rt", newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        if (row["provider"], row["namespace"], row["external_id"]) == target:
            print(row["reep_id"])
            break
PY
```

The public bridge file is deliberately narrow: `provider`, `namespace`, `external_id`,
and `reep_id`. Evidence payloads, local source paths, dates of birth, scorelines and
review notes are not part of the public contract.

## Query The DuckDB Bundle

The DuckDB file is a convenience copy of the same CSV contract:

```sql
SELECT e.reep_id, e.label
FROM bridges b
JOIN entities e USING (reep_id)
WHERE b.provider = 'transfermarkt'
  AND b.namespace = 'spieler'
  AND b.external_id = '568177';
```

Use DuckDB when you want local joins without writing a loader. Use the CSV files when
you need the simplest long-term ingestion contract.

## Understand Provider Roles

The v1 public API and manifest distinguish provider roles:

| Role             | Meaning                                                                                                             | How to use it                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Canonical bridge | A provider ID that may identify a Reep entity in the public bridge table.                                           | Safe for lookup within its provider namespace and entity type.               |
| Bridge-only      | Useful cross-provider ID carried for interoperability, but not a source that raises public corroboration by itself. | Use as an outbound/enrichment ID, not as proof that two people are the same. |
| Overlay-only     | Convenience enrichment from a discovery layer, such as Wikidata-originated names.                                   | Useful for display/search enrichment; never treat as a canonical bridge.     |

The distinction matters most when you copy Reep outputs into your own entity-resolution
system. A bridge row can answer "which Reep entity carries this provider ID?" It does
not mean every provider has equal authority to create or merge identities.

## Keep V0 Separate

The old public repo and RapidAPI service use v0 IDs such as `reep_p2804f5db`. Reep v1
uses Reep Next IDs and a different public file contract. Migrate by provider IDs or
release files, not by assuming v0 IDs map one-to-one to v1 IDs.

See:

- [Reep API](https://reep.football/api)
- [Downloads](https://reep.football/downloads)
- [RapidAPI migration guide](https://reep.football/api/migration)
