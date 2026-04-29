---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [player]
matching_fields: [name, alias, date_of_birth, provider_id, source_snapshot]
confidence_floor: 0.95
failure_mode: alias_variant_duplicate
decision: [auto_write, alias_harvest]
search_tags: [alias, duplicate-prevention, dob]
---

# Alias Variant Duplicate Prevention

This example shows how a register avoids minting a duplicate when two sources use
different versions of the same player's name.

## Situation

The register already has this player:

| entity_id | name           | date_of_birth | provider      | external_id |
| --------- | -------------- | ------------- | ------------- | ----------- |
| `p_101`   | Daniel Seaward | 1987-03-05    | wikidata      | Q100101     |
| `p_101`   | Daniel Seaward | 1987-03-05    | transfermarkt | 90101       |

A new provider snapshot contains:

```json
{
  "provider": "sportmonks",
  "source_snapshot": "sportmonks-players-2026-04-29",
  "external_id": "55501",
  "name": "Danny Seaward",
  "date_of_birth": "1987-03-05",
  "nationality": "England"
}
```

Exact normalised-name matching fails because `daniel seaward` and `danny seaward` are
not identical.

## Bad Outcome

A naive minter creates:

| entity_id | name          | date_of_birth | provider   | external_id |
| --------- | ------------- | ------------- | ---------- | ----------- |
| `p_202`   | Danny Seaward | 1987-03-05    | sportmonks | 55501       |

The register now has two live player entities for the same person.

## Better Duplicate Check

Before minting, run a duplicate candidate check:

| Check                             | Result             | Effect                            |
| --------------------------------- | ------------------ | --------------------------------- |
| Same date of birth                | yes                | candidate survives                |
| Same surname after normalisation  | yes, `seaward`     | candidate survives                |
| Compatible first-name initial     | yes, `d`           | candidate survives                |
| Existing strong provider bridge   | yes, Transfermarkt | do not mint                       |
| Name variant explainable as alias | yes, Daniel/Danny  | attach alias and bridge if unique |
| Other same-DOB Seaward candidates | none               | eligible for high-confidence link |

## Correct Write Set

```text
entity_id: p_101
provider: sportmonks
external_id: 55501
confidence: 0.95
method: dob+surname+first-initial+alias-review
source_snapshot: sportmonks-players-2026-04-29
```

Add the provider display name as an alias:

```text
entity_id: p_101
alias: Danny Seaward
source_provider: sportmonks
source_snapshot: sportmonks-players-2026-04-29
```

## When This Should Still Route To Review

Do not auto-write if:

- there are two same-DOB, same-surname candidates,
- the first-name variant is not explainable,
- one candidate already has a conflicting SportMonks ID,
- the new source lacks date of birth,
- the new record belongs to a different entity type.

## Doctrine Demonstrated

- Duplicate prevention belongs before minting.
- Exact-name matching is too strict for real football names.
- Alias harvesting is safer than minting a second entity.
- Strong biographical evidence can support a bridge, but ambiguity still blocks
  auto-write.
