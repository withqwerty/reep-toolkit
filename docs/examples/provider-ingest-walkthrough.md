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
entity_types: [player, team]
matching_fields:
  [provider_id, name, date_of_birth, nationality, country, source_snapshot]
confidence_floor: 0.95
failure_mode: signal_provider_ingest
decision: [auto_write, review_residue]
search_tags: [golden-path, fotmob, write-set]
---

# Provider Ingest Walkthrough

This walkthrough shows the full path from provider card to write set for a signal-only
provider. The example uses FotMob-shaped records because there is no direct bridge: the
provider card matters before the matcher exists.

## 1. Provider Card Decisions

From [FotMob](../providers/fotmob.md):

| Question                               | Answer                                    | Ingest consequence                           |
| -------------------------------------- | ----------------------------------------- | -------------------------------------------- |
| Does FotMob expose cross-provider IDs? | no                                        | Use signal matching; no direct bridge path.  |
| Which player fields matter?            | ID, name, DOB, nationality, team context. | DOB/name is the main write path.             |
| Can FotMob mint new players?           | no, not by default.                       | Unmatched records become candidates/residue. |
| What is the main failure mode?         | false positives from name-only matching.  | DOB-less records route to review.            |
| What should be stored after a match?   | FotMob ID and aliases.                    | Write bridge plus alias evidence.            |

## 2. Snapshot

```text
provider: fotmob
snapshot: fotmob-squad-2026-04-29
source_kind: cached-json
entity_type: player
```

Rows:

```json
[
  {
    "id": 292462,
    "name": "Cole Palmer",
    "birthDate": "2002-05-06",
    "nationality": "England",
    "team_id": 8455
  },
  {
    "id": 123456,
    "name": "Alex Morgan",
    "birthDate": "1989-07-02",
    "nationality": "United States",
    "team_id": 100
  },
  {
    "id": 777777,
    "name": "J. Silva",
    "birthDate": null,
    "nationality": "Brazil",
    "team_id": 200
  }
]
```

## 3. Existing Register

| entity_id | name        | date_of_birth | nationality   | existing bridges     |
| --------- | ----------- | ------------- | ------------- | -------------------- |
| `p_001`   | Cole Palmer | 2002-05-06    | England       | transfermarkt:568177 |
| `p_002`   | Alex Morgan | 1989-07-02    | United States | wikidata:Q233        |
| `p_003`   | Joao Silva  | 1998-01-01    | Brazil        | transfermarkt:444    |
| `p_004`   | Jonas Silva | 1998-01-01    | Brazil        | transfermarkt:555    |

## 4. Matcher Output

| FotMob ID | Method                | Candidate | Confidence | Status         |
| --------- | --------------------- | --------- | ---------: | -------------- |
| `292462`  | `dob+normalised-name` | `p_001`   |       0.95 | auto-write     |
| `123456`  | `dob+normalised-name` | `p_002`   |       0.95 | auto-write     |
| `777777`  | `name+nationality`    | none      |       0.90 | review/residue |

Why `777777` is not written:

- DOB is missing,
- name is abbreviated,
- nationality is not enough,
- multiple Brazilian players could plausibly match.

## 5. Write Set

Accepted bridges:

```text
entity_id: p_001
provider: fotmob
external_id: 292462
confidence: 0.95
method: dob+normalised-name
source_snapshot: fotmob-squad-2026-04-29
matcher_version: fotmob-player-v1
```

```text
entity_id: p_002
provider: fotmob
external_id: 123456
confidence: 0.95
method: dob+normalised-name
source_snapshot: fotmob-squad-2026-04-29
matcher_version: fotmob-player-v1
```

Review candidate:

```text
provider: fotmob
external_id: 777777
name: J. Silva
nationality: Brazil
confidence: 0.90
method: name+nationality
review_status: needs_more_evidence
reason: missing DOB and abbreviated name
```

## 6. Post-Write Checks

Run checks for:

- duplicate FotMob IDs across live players,
- FotMob IDs attached to tombstoned entities,
- accepted writes below confidence floor,
- unresolved review candidates older than the configured threshold,
- row-count changes versus previous snapshot.

## 7. What Not To Do

Do not:

- mint `J. Silva` as a new player,
- attach `J. Silva` to the first Brazilian Silva,
- treat current `team_id` as enough to override missing DOB,
- discard the review candidate.

## Doctrine Demonstrated

- Provider cards define the matcher's safe behaviour.
- Signal-only providers can write strong matches when DOB/name is unambiguous.
- Weak candidates are retained, not forced.
- The write set is smaller than the matcher's candidate output by design.
