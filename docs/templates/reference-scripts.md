---
doc_type: reference_scripts
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: templates
stance: descriptive
contribution_model: example_patch
---

# Reference Scripts

The `reference-scripts/` directory contains copy-paste Python examples for working with
the synthetic fixtures in this repo. They are not an installable package and they do not
contain provider adapters, private register clients, credentials, or write machinery.

## Included Scripts

| Script                                   | Purpose                                                                 |
| ---------------------------------------- | ----------------------------------------------------------------------- |
| `reference-scripts/evidence_payloads.py` | Validates candidate, evidence, relationship, blocker, and residue JSON. |
| `reference-scripts/templates.py`         | Builds non-mutating candidate and review-residue payloads.              |

## Smoke Test

The repo check runs:

```bash
npm run reference-scripts:check
```

That command validates every synthetic payload fixture and checks that the template
builders regenerate the template fixtures exactly.

## Boundary

Reference scripts may show:

- JSON payload validation;
- simple normalisation helpers;
- non-mutating candidate builders;
- deterministic fixture comparison.

They must not become a framework, package API, provider adapter library, or register
writer. If a workflow needs credentials, private mirrors, or a target-register client,
it belongs in the consuming project's codebase.
