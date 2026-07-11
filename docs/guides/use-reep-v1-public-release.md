---
doc_type: practice_guide
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-07-11
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, stage, match]
matching_fields: [provider_id, namespace, release_stamp, bridge_role]
confidence_floor: 0.95
---

# Consume The Reep Register

The Reep Register will be published as complete, dated snapshots. Its CSV files are the
canonical public artefact. The DuckDB bundle is a convenient copy derived only from
those files.

This guide describes the launch contract. The complete Bridge Register release and the
production `/api/v1` service are still staged, so do not build production jobs against
these URLs until Reep announces that they are live.

## Start With The Manifest

After launch, fetch the latest release pointer:

```bash
curl -L https://data.reep.football/releases/latest.json
```

The manifest identifies the release stamp, schema version, files, checksums, row counts
and redaction policy. Record the stamp with any analysis you run and verify downloaded
files against their listed SHA-256 checksums. If two results cite different stamps, they
come from different snapshots.

## Choose The Right Surface

| Need                                    | Use                                                     |
| --------------------------------------- | ------------------------------------------------------- |
| Bulk analysis, joins or local ingestion | CSV files from the release manifest                     |
| Local SQL exploration                   | `duckdb/reep-register-v1.duckdb` from the same release  |
| One-off provider ID lookup              | Keyed `/api/v1/resolve/{provider}/{external_id}` access |
| Entity detail by Reep ID                | Keyed `/api/v1/entities/{reep_id}` access               |
| Coverage analysis without provider IDs  | The separately published Open Census snapshot           |

Use the bulk release when you need the register or a substantial part of it. Do not
scrape the website, repeatedly page through the API or treat API access as a fresher
edition of the data.

## Resolve A Provider ID

Provider IDs are namespace-scoped. A bare integer is not enough context. For example,
Transfermarkt can use the same numeric form in its `spieler` and `trainer` namespaces,
where the identifiers refer to different kinds of record.

Once `/api/v1` is live and you have been issued a key, a bounded lookup will look like
this:

```bash
curl -H "Authorization: Bearer $REEP_API_KEY" \
  "https://reep.football/api/v1/resolve/transfermarkt/568177?namespace=spieler&type=player"
```

Initial API access is intended for named data partners and Loom consultancy engagements.
Keys, small batch bounds and rate limits protect service reliability. They do not unlock
more data than the public snapshot. Bulk ingestion belongs on the CSV or DuckDB path.

## Inspect The Bridge CSV

The complete Bridge Register publishes the provider crosswalk in `csv/bridges.csv.gz`.
Use the stamped file URL listed in the manifest:

```bash
curl -L -o bridges.csv.gz \
  "https://data.reep.football/releases/<stamp>/csv/bridges.csv.gz"
python3 - <<'PY'
import csv
import gzip

target = ("transfermarkt", "spieler", "568177")
with gzip.open("bridges.csv.gz", "rt", newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        key = (row["provider"], row["namespace"], row["external_id"])
        if key == target:
            print(row["reep_id"])
            break
PY
```

The bridge table contains `provider`, `namespace`, `external_id` and `reep_id`. Always
join on the full `(provider, namespace, external_id)` triple. Evidence payloads, local
source paths, dates of birth, scorelines and private review notes are not part of the
public contract.

## Query The DuckDB Bundle

The DuckDB file contains tables rebuilt from the same public CSVs:

```sql
SELECT e.reep_id, e.label
FROM bridges b
JOIN entities e USING (reep_id)
WHERE b.provider = 'transfermarkt'
  AND b.namespace = 'spieler'
  AND b.external_id = '568177';
```

Use DuckDB for convenient local joins. Use the CSVs and their checksums as the long-term
ingestion contract and source of truth if the two ever differ.

## Understand The Two Snapshots

The public surfaces have different purposes:

| Snapshot        | Contents                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bridge Register | Complete admitted entities, provider bridges, safe aliases, redirects, structural relationships, coverage metadata and labelled public overlays. |
| Open Census     | Entities, safe labels, relationships and coverage, without provider identifiers or overlay links.                                                |

The Bridge Register is not a sample or a paid tier. It is the complete dated public
crosswalk after the release filters have removed material that should not be published.
Reep may publish later snapshots as the living register changes.

## Interpret Bridges And Overlays

A bridge answers which Reep entity carries a provider identifier. It does not mean that
every provider has equal authority to create or merge identities, and it does not
include the private evidence used to justify the mapping.

Overlay aliases and links are labelled discovery or display conveniences. Treat them as
overlay data, not as canonical provider bridges or independent evidence that two records
describe the same entity.

## Keep The Legacy Service Separate

The existing RapidAPI service uses legacy IDs such as `reep_p2804f5db`. It remains a
separate supported surface for current customers during migration. Reep Register IDs and
its release contract are different.

Do not mix the two ID systems in one column. Store the register generation or source
alongside each identifier, and migrate through namespace-scoped provider IDs rather than
assuming a one-to-one mapping between legacy and Reep Register IDs.

At launch, the current links and migration status will be published at:

- [Reep API](https://reep.football/api)
- [Downloads](https://reep.football/downloads)
- [RapidAPI migration guide](https://reep.football/api/migration)
