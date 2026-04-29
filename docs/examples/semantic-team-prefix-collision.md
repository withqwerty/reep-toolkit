---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [team]
matching_fields: [name, provider_id, country, semantic_prefix, source_snapshot]
confidence_floor: 0.95
failure_mode: semantic_prefix_stripped
decision: [reject_candidate]
search_tags: [team, name-normalisation, collision]
---

# Semantic Team Prefix Collision

This example shows why team-name normalisation must distinguish removable corporate
forms from semantic club-name prefixes.

## Situation

A provider snapshot contains two teams in the same country:

| provider_id | provider_name      | country |
| ----------- | ------------------ | ------- |
| `tm_13`     | Real Riverside CF  | Spain   |
| `tm_22`     | Atletico Riverside | Spain   |

The register already has:

| entity_id | name               | country | provider      | external_id |
| --------- | ------------------ | ------- | ------------- | ----------- |
| `t_001`   | Real Riverside CF  | Spain   | transfermarkt | `tm_13`     |
| `t_002`   | Atletico Riverside | Spain   | transfermarkt | `tm_22`     |

## Bad Normalisation

A naive normaliser strips every prefix it recognises:

```text
Real Riverside CF  -> riverside
Atletico Riverside -> riverside
```

Both clubs now collapse to the same key. If the matcher then accepts the first
candidate, it can bind the wrong provider ID to the wrong club.

## Better Prefix Policy

Separate corporate forms from semantic identity tokens:

| Token type      | Examples                                   | Treatment                                      |
| --------------- | ------------------------------------------ | ---------------------------------------------- |
| Corporate form  | `FC`, `CF`, `SC`, `Club`                   | May be stripped or downweighted by locale.     |
| Semantic prefix | `Real`, `Atletico`, `Sporting`, `Athletic` | Preserve unless provider docs prove otherwise. |

The normalised keys become:

```text
Real Riverside CF  -> real riverside
Atletico Riverside -> atletico riverside
```

## Collision Guard

Before writing a provider bridge, scan for same-provider same-type collisions:

| Proposed write                 | Existing row                    | Action                       |
| ------------------------------ | ------------------------------- | ---------------------------- |
| `t_002 -> transfermarkt:tm_13` | `t_001 -> transfermarkt:tm_13`  | block                        |
| `t_001 -> transfermarkt:tm_13` | same entity already has the row | ignore or refresh provenance |

## Review Record

```text
review_type: team_name_collision
provider: transfermarkt
proposed_entity_id: t_002
proposed_external_id: tm_13
current_entity_for_external_id: t_001
normalised_key: riverside
reason: semantic prefix stripped during matching
decision: reject_candidate
```

## Doctrine Demonstrated

- Team-name normalisation is locale-sensitive.
- Some prefixes are part of club identity, not decoration.
- Provider-ID collision checks are a final guard against bad normalisation.
- A name match cannot override an existing same-provider bridge.
