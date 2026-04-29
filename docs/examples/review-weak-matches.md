---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
confidence_floor: 0.90
entity_types: [player, team, match]
failure_mode: weak_match_candidates
decision: [review, reject]
search_tags: [review-queue, confidence, residue]
---

# Review Weak Matches

Weak matches are valuable, but they should not silently enter a public register.

## Review Packet

Each candidate should include:

- provider record,
- proposed target entity,
- candidate method,
- confidence label,
- conflicting candidates,
- source snapshot,
- previous decisions,
- reviewer decision.

## Decisions

| Decision             | Meaning                                             |
| -------------------- | --------------------------------------------------- |
| Accept               | Write the mapping with reviewer lineage.            |
| Reject               | Persist rejection so reruns suppress the candidate. |
| Needs more evidence  | Keep pending and request another source.            |
| New entity candidate | Route to entity-creation policy.                    |

## Reproducibility

A reviewer should be able to reconstruct why a candidate appeared. If the source record
cannot be shown publicly, include only the fields that the project is allowed to
disclose.
