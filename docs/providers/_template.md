---
doc_type: provider_template
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: providers
provider: example_provider
entity_types: []
access_tier: unknown
source_kind: unknown
authority_role: metadata_source
bridge_providers: []
matching_fields: []
confidence_floor: 0.90
stance: descriptive
contribution_model: evidence_required
private_dependencies: []
---

# Provider Name

One-paragraph summary of the provider, owner, product family, and why it matters for
identity matching.

## Entities Identified

| Entity type | Provider ID field | Stable? | Notes |
| ----------- | ----------------- | ------- | ----- |
| player      |                   | unknown |       |
| team        |                   | unknown |       |
| competition |                   | unknown |       |
| season      |                   | unknown |       |
| match       |                   | unknown |       |

## ID Namespaces

Describe every relevant ID namespace. Say whether IDs are numeric, UUID, slug,
composite, edition-specific, or undocumented.

## Matching Surface

### Players

| Field         | Available? | Format | Matching value |
| ------------- | ---------- | ------ | -------------- |
| provider ID   |            |        |                |
| name          |            |        |                |
| date of birth |            |        |                |
| nationality   |            |        |                |
| team context  |            |        |                |

### Teams

| Field               | Available? | Format | Matching value |
| ------------------- | ---------- | ------ | -------------- |
| provider ID         |            |        |                |
| name                |            |        |                |
| country             |            |        |                |
| founded             |            |        |                |
| competition context |            |        |                |

### Matches

| Field             | Available? | Format | Matching value |
| ----------------- | ---------- | ------ | -------------- |
| provider match ID |            |        |                |
| date              |            |        |                |
| kickoff           |            |        |                |
| home team ID      |            |        |                |
| away team ID      |            |        |                |
| competition ID    |            |        |                |
| season ID         |            |        |                |

## Bridge Data

List direct bridges to other providers and their reliability.

| Bridge               | Source field | Confidence floor | Notes |
| -------------------- | ------------ | ---------------- | ----- |
| provider -> wikidata |              |                  |       |

## Acquisition

Describe public, grey, paid, or private access. Do not publish credentials or data the
project cannot redistribute.

## Quirks and Risks

- Known ID scheme changes.
- Known duplicate or retired IDs.
- Localisation issues.
- Women's football coverage differences.
- Youth/reserve/team-category collisions.

## Recommended Linking Strategy

State which matches can be written directly, which require review, and which are only
useful as candidates.

## References

- Link to primary docs, public examples, or reproducible evidence.
