---
doc_type: taxonomy
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: providers
stance: descriptive
contribution_model: evidence_required
---

# Source Taxonomy

Provider data should be described across four axes. This keeps docs precise enough to
drive matching decisions.

## 1. Living Versus Static

| Kind   | Meaning                            | Operational consequence                             |
| ------ | ---------------------------------- | --------------------------------------------------- |
| Living | Provider records change over time. | Snapshot, version, and revalidate.                  |
| Static | Fixed historical dataset.          | Preserve citation and dataset version.              |
| Mixed  | IDs stable, metadata evolving.     | Refresh metadata without assuming identity changes. |

## 2. Authoritative Versus Derived

| Kind          | Meaning                                                     | Operational consequence                          |
| ------------- | ----------------------------------------------------------- | ------------------------------------------------ |
| Authoritative | Provider owns or directly maintains the identity namespace. | Candidate source for creation or strong bridges. |
| Derived       | Provider republishes or infers IDs from another source.     | Useful citation, but authority belongs upstream. |

## 3. Bridge Versus Metadata

| Kind            | Meaning                                                   | Operational consequence                           |
| --------------- | --------------------------------------------------------- | ------------------------------------------------- |
| Bridge source   | Carries external provider IDs.                            | Strong for linkage if entity type is correct.     |
| Metadata source | Carries DOB, names, nationalities, country, aliases, etc. | Useful for matching and disambiguation.           |
| Both            | Carries IDs and matching metadata.                        | Strongest provider type for register maintenance. |

## 4. Append-Only Versus Evolving

| Kind        | Meaning                                        | Operational consequence         |
| ----------- | ---------------------------------------------- | ------------------------------- |
| Append-only | Old records rarely mutate.                     | Simple reruns are usually safe. |
| Evolving    | Existing records can change, merge, or retire. | Need drift checks and lineage.  |

## Acquisition Tiers

| Tier         | Examples                                           | Public toolkit policy                                                          |
| ------------ | -------------------------------------------------- | ------------------------------------------------------------------------------ |
| Public bulk  | Wikidata dumps, open GitHub datasets.              | Ship fetchers when licence allows.                                             |
| Public API   | Official public endpoints with compatible terms.   | Ship fetchers carefully.                                                       |
| Public grey  | Public endpoints with unclear programmatic re-use. | Document shape, prefer established third-party libraries, avoid live fetchers. |
| Paid/private | Vendor feeds and customer exports.                 | Document abstract shapes, ship loaders for user-supplied files only.           |
