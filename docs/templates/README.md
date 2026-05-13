---
doc_type: template_index
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: templates
stance: descriptive
contribution_model: example_patch
---

# Portable Templates

Templates are public-safe shapes for entity-resolution work. They are not Reep
control-plane recipes and they do not allocate register IDs, apply writes, or encode
private doctrine.

Use these artefacts when you want a stable output shape for candidates, evidence,
blockers, and review residue in your own register or notebook.

For the field-level shape, see [Evidence Payload Schema](evidence-schema.md). For
copy-paste validation and template-builder examples, see
[Reference Scripts](reference-scripts.md).

## Included Fixtures

| Fixture                                                                                                                          | Pattern                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [`fixtures/evidence/example-match-candidate.json`](../../fixtures/evidence/example-match-candidate.json)                         | Match candidate with fixture tuple, competition relationship evidence, and a blocking unresolved competition. |
| [`fixtures/evidence/review-residue.json`](../../fixtures/evidence/review-residue.json)                                           | Review residue created from a blocked candidate.                                                              |
| [`fixtures/evidence/source-constraints.json`](../../fixtures/evidence/source-constraints.json)                                   | Source-role constraints for canonical feeds and corroborators.                                                |
| [`fixtures/templates/match-bridge-candidate.json`](../../fixtures/templates/match-bridge-candidate.json)                         | Provider match ID plus fixture tuple and relationship context.                                                |
| [`fixtures/templates/relationship-constrained-candidate.json`](../../fixtures/templates/relationship-constrained-candidate.json) | Candidate narrowed by relationship evidence such as lineup, squad, team, or competition membership.           |
| [`fixtures/templates/split-season-stage-candidates.json`](../../fixtures/templates/split-season-stage-candidates.json)           | Parent season plus stage candidates for split phases or playoff stages.                                       |
| [`fixtures/templates/candidate-recovery-residue.json`](../../fixtures/templates/candidate-recovery-residue.json)                 | Review hand-off when candidate recovery needs more evidence.                                                  |

## Boundary

Templates may:

- preserve provider, method, confidence, snapshot, and relationship metadata;
- describe blockers without forcing a write;
- provide synthetic JSON fixtures for tests and documentation;
- point readers to provider cards for identity-surface facts.

Templates must not:

- allocate Reep IDs or any target-register IDs;
- read private mirrors or local register files;
- encode private Reep doctrine matrix thresholds;
- apply writes, tombstones, redirects, or review decisions;
- publish private provider payloads or credentials.

## Usage Pattern

Treat a template payload as evidence to be consumed by your own pipeline:

```text
provider-shaped record -> candidate payload -> review/write decision -> register-specific write
```

The payload should carry enough method, confidence, blocker, and relationship evidence
for a human or downstream policy engine to understand why it was accepted, deferred, or
rejected.
