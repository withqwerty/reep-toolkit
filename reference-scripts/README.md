---
doc_type: reference_scripts
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: reference_scripts
stance: descriptive
contribution_model: example_patch
---

# Reference Scripts

These scripts are copy-paste examples for small identity-resolution workflows. They are
not an installable Python package and they do not contain adapters, credentials, private
register clients, or write machinery.

## Included Scripts

| Script                 | Purpose                                                                 |
| ---------------------- | ----------------------------------------------------------------------- |
| `evidence_payloads.py` | Validates candidate, evidence, relationship, blocker, and residue JSON. |
| `templates.py`         | Builds non-mutating candidate and review-residue payloads.              |

Use them with the synthetic fixtures under `fixtures/`. Projects should copy the parts
that match their own register shape, then keep acceptance policy and writes in their own
codebase.
