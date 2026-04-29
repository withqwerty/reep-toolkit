---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
provider: fotmob
entity_types: [player]
matching_fields: [fotmob_id, name, date_of_birth, nationality]
confidence_floor: 0.95
failure_mode: signal_only_provider
decision: [auto_write_if_unique, review_residue]
search_tags: [fotmob, signal-match, dob]
---

# FotMob Signal-Only Player Match

FotMob exposes no direct cross-provider bridge. The safe path is biographical matching,
with strict ambiguity rejection.

## Source Record

```json
{
  "id": 292462,
  "name": "Cole Palmer",
  "birthDate": "2002-05-06",
  "nationality": "England",
  "team_id": 8455
}
```

## Candidate Lookup

The registry searches by DOB first, then normalised name.

| candidate | name        | date_of_birth | nationality | existing bridges                    |
| --------- | ----------- | ------------- | ----------- | ----------------------------------- |
| `p_001`   | Cole Palmer | 2002-05-06    | England     | transfermarkt:568177, wikidata:Q123 |

Only one candidate survives.

## Decision

| Method                | Outcome                              | Confidence | Write? |
| --------------------- | ------------------------------------ | ---------: | ------ |
| `dob+normalised-name` | attach FotMob ID `292462` to `p_001` |     `0.95` | yes    |

## Counterexample

If the DOB were missing:

```json
{
  "id": 292462,
  "name": "Cole Palmer",
  "birthDate": null,
  "nationality": "England"
}
```

the outcome changes:

| Method             | Outcome               | Confidence | Write?              |
| ------------------ | --------------------- | ---------: | ------------------- |
| `name+nationality` | candidate for `p_001` |     `0.90` | no, route to review |

## Reep-Style Lesson

Signal-only providers can still produce strong mappings, but the write threshold depends
on the missing fields. Exact name plus DOB is a different class of evidence from name
plus nationality.
