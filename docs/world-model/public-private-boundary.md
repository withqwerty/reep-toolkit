---
doc_type: world_model
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
---

# Public and Private Boundary

This toolkit is valuable because it shares hard-earned matching judgement. It must not
publish private operational machinery.

## Public-Safe

| Area            | Public-safe treatment                                                              |
| --------------- | ---------------------------------------------------------------------------------- |
| Provider quirks | Document observed behaviour, cite public examples, describe matching consequences. |
| Register design | Explain stable IDs, bridges, aliases, provenance, redirects, and validation.       |
| Pipelines       | Describe stages and provide public-safe code examples.                             |
| Reep            | Use as a case study when the lesson is general.                                    |
| Paid providers  | Document shapes and matching concepts without redistributing data or credentials.  |

## Keep Private

| Area                 | Keep private                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------- |
| Local paths          | Machine-specific storage, scratch files, snapshots, and mirrors.                            |
| Internal scripts     | Private pipeline names, runbooks, promotion paths, and one-off operators.                   |
| Licensed data        | Raw payloads, paid snapshots, derived exports that cannot be shared.                        |
| Operational doctrine | Exact private phase plans, cutover procedures, credentials, alerts, and project tickets.    |
| Unreleased decisions | Temporary source choices or active migration details that may change before public release. |

## Rewrite Pattern

Private wording:

> Reep-custom script X reads private file Y and writes table Z.

Public wording:

> A register can implement this as a snapshot reader that emits provider-shaped records,
> then applies a matcher that writes provider bridges with source snapshot and matcher
> version.

## Adjacent Repository Map

| Surface                    | Role                                                                              | Boundary                                                                                                                                                        |
| -------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `reep-toolkit`             | Public docs, examples, schemas, and reference scripts for football identity work. | Explains reusable judgement and small implementation patterns; does not ship private Reep operations.                                                           |
| `reep-scripts`             | Legacy migration input.                                                           | Useful docs, examples, schemas, fixtures, and small patterns should be folded into the toolkit; package promises should be dropped.                             |
| `football-docs`            | Source/provenance research backend.                                               | Provider facts can inform toolkit pages, but toolkit is the public authority at launch. Non-identity or access-heavy material can stay out of the public site.  |
| `reep-matching-logic-pack` | Private partner pack.                                                             | Shows source-authority playbooks, review behaviour, validator logic, and sample write sets without exposing credentials, raw paid data, or production commands. |
| `reep-register-next`       | Private Reep Next control plane.                                                  | Owns actual doctrine artefacts, canonical-feed assignments, mint salts, action ledgers, review DB state, projections, and publish gates.                        |

If a contribution is public explanation, provider knowledge, a schema, a fixture, or a
copyable reference script, keep it here. If it needs partner context or operating-model
depth, keep it in the logic pack. If it depends on private Reep state, it stays in
`reep-register-next`.
