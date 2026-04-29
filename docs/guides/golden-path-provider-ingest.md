---
doc_type: practice_guide
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, match]
matching_fields: [provider_id, name, date_of_birth, source_snapshot, confidence]
confidence_floor: 0.95
---

# Golden Path Provider Ingest

This is the recommended first route through a provider ingest. It is deliberately
conservative: understand the provider world model, produce explainable candidates, and
write fewer high-quality bridges before expanding coverage.

## 1. Read The Provider Card

Start with the provider page, not the payload.

Answer:

| Question                                   | Why it matters                                          |
| ------------------------------------------ | ------------------------------------------------------- |
| Which entity types does the provider have? | Prevents player/team/coach/season namespace errors.     |
| Which IDs are stable?                      | Determines whether the provider can bridge or mint.     |
| Which fields are identity evidence?        | Separates match signals from decorative metadata.       |
| Which fields are context only?             | Prevents current-team or display labels becoming proof. |
| Which provider quirks are known?           | Avoids known namespace, stage, or category mistakes.    |

If the provider card is thin, improve it before writing matching logic.

## 2. Capture A Snapshot

Treat the source record as evidence. Every candidate should be traceable to:

- provider,
- endpoint or source kind,
- snapshot date,
- source record ID,
- source payload version or parser version,
- fields used for identity.

The snapshot does not have to be a private operational artefact in this toolkit. The
public principle is that matching should be replayable against a fixed source state.

## 3. Load Into A Provider-Native Shape

Create a small normalised shape that preserves provider semantics:

```text
provider_record:
  provider: fotmob
  entity_type: player
  external_id: 292462
  name: Cole Palmer
  date_of_birth: 2002-05-06
  nationality: England
  current_team_id: 8455
  source_snapshot: fotmob-squad-2026-04-29
```

Do not flatten ambiguous fields too early. If the provider has `season_id` and
`stage_id`, keep both. If the provider has numeric player and coach IDs, keep the entity
type.

## 4. Resolve Direct Bridges First

Direct bridges are the cleanest route:

| Bridge shape                                  | Default route                                              |
| --------------------------------------------- | ---------------------------------------------------------- |
| Provider record carries a Transfermarkt ID.   | Check namespace and existing bridge, then write if unique. |
| Provider record carries a Wikidata QID.       | Check entity type, DOB/context, and QID status.            |
| Provider record carries another provider ID.  | Confirm the ID namespace and target entity type.           |
| Provider record carries only a display label. | Do not write as a direct bridge.                           |

Before writing, always check whether the same provider/external ID already exists on a
different live entity of the same type.

## 5. Run Signal Matching

When no direct bridge exists, use the strictest useful signals:

| Entity type | Strong signal                                                            | Weak signal              |
| ----------- | ------------------------------------------------------------------------ | ------------------------ |
| Player      | DOB plus normalised name, unique after candidate search.                 | Name plus nationality.   |
| Coach       | DOB plus name or role-specific provider ID.                              | Staff display name only. |
| Team        | Provider ID plus country/category; fixture overlap when IDs are missing. | Name-only.               |
| Season      | Competition plus provider season/stage model.                            | Bare year.               |
| Match       | Date plus resolved home/away teams plus season/competition.              | Event payload alone.     |

Weak signals should create review candidates, not accepted writes.

## 6. Route By Confidence

Use the matching thresholds guide as the gate:

| Confidence | Route                                                             |
| ---------- | ----------------------------------------------------------------- |
| `1.0`      | Direct stable bridge, auto-write if unique.                       |
| `0.95`     | Strong signal match, auto-write only when ambiguity is ruled out. |
| `0.90`     | Candidate or review item.                                         |
| `0.80`     | Discovery only.                                                   |
| `<0.80`    | Reject or ignore unless useful for search.                        |

The write set should be smaller than the candidate set.

## 7. Write With Lineage

Every accepted bridge should carry:

- entity ID,
- provider,
- external ID,
- entity type,
- method,
- confidence,
- source snapshot,
- matcher version or rule name,
- review status if applicable.

Do not write anonymous key-value pairs. Future maintainers need to know why a bridge
exists.

## 8. Keep Residue

Unmatched records are useful if they are structured:

```text
review_candidate:
  provider: fotmob
  external_id: 777777
  entity_type: player
  name: J. Silva
  reason: missing DOB and abbreviated name
  confidence: 0.90
```

Residue should explain the blocker: missing DOB, duplicate candidates, namespace
mismatch, provider conflict, source-prior conflict, or unsupported entity model.

## 9. Run Maintenance Checks

After the write set:

- check duplicate provider IDs by entity type,
- check accepted writes below the confidence floor,
- check writes to tombstoned entities,
- compare row counts against the previous snapshot,
- inspect drift in provider fields used for identity,
- refresh or mark stale any read mirror used by the matcher.

## 10. Document The Lesson

If the ingest teaches a reusable lesson, add either:

- a provider-card gotcha,
- a practice-guide note,
- a worked example,
- an entry in the examples catalogue.

## Worked Example Path

Read these in order for a concrete walkthrough:

1. [Provider ingest walkthrough](../examples/provider-ingest-walkthrough.md).
2. [FotMob signal-only player match](../examples/fotmob-signal-only-player.md).
3. [Bridge conflict case study](../examples/bridge-conflict-case-study.md).
4. [Snapshot drift report](../examples/snapshot-drift-report.md).
