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
