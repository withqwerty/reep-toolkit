---
doc_type: practice_guide
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-05-19
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, match]
matching_fields:
  [provider_id, name, date_of_birth, country, match_date, home_team, away_team]
confidence_floor: 0.95
---

# Minting and Entity Creation

Minting is the act of creating a new register entity. It is more sensitive than
attaching a bridge because a minted entity becomes part of the world model.

## Reep-Style Rule

Do not let every provider create entities. Each entity type should have documented
creation sources. Other providers attach bridges, aliases, or review candidates.

## Why This Matters

If every provider can mint, the register accumulates duplicates:

- one player from a stats provider,
- one player from a salary provider,
- one player from a game-ratings provider,
- one player from a transfer database,
- all representing the same person.

The cleanup cost is higher than the initial matching cost.

## Creation Policy by Entity Type

Each register should document, for each entity type:

- which providers can create entities,
- which providers can only attach bridges,
- which signals are required before creation,
- which records must be deferred,
- how to handle pre-existing unmatched records.

## Creation Source Matrix

A practical policy table looks like this:

| Entity type | Can mint from                                                      | Bridge-only sources                                                            | Never mint from                              |
| ----------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------ | -------------------------------------------- |
| Player      | Sources with stable player ID plus DOB/name coverage.              | Signal-only apps, salary/game-rating providers, weak community bridges.        | Name-only records.                           |
| Team        | Sources with stable team ID plus country/category context.         | Event/stats providers with team IDs but unclear parent/team-section semantics. | Display labels alone.                        |
| Coach       | Sources with coach-specific ID plus DOB or strong role context.    | Player-profile sources that mention coaching role.                             | Staff names without identity fields.         |
| Competition | Sources with stable competition family IDs and documented level.   | Providers whose "league" actually means product bucket or stage.               | Free-text league labels.                     |
| Season      | Sources with documented season/stage model.                        | Providers with display year only.                                              | Labels that cannot be tied to a competition. |
| Match       | Fixture sources with stable match IDs plus resolved tuple context. | Event providers, odds feeds, box-score sources.                                | Raw event rows without fixture identity.     |

This is deliberately stricter than "the provider has an ID". An ID can identify the
wrong level of the world model.

## Mint Versus Defer

Mint when:

- the source is authorised for that entity type,
- the record has enough identity fields,
- duplicate checks find no existing entity,
- the source snapshot is recorded,
- the entity can be explained later.

Defer when:

- the provider lacks stable IDs,
- the record has name-only evidence,
- the same name appears in multiple contexts,
- the upstream entity level is unclear,
- a likely match exists but needs review.

## Coverage Floors

Sometimes a missing corroborator is not a temporary gap. For lower tiers, women's
competitions, youth football, or cup-only entrants, the strongest available provider may
be the only provider that covers the team at all.

If you choose to mint below that coverage floor, make the exception explicit:

- define the country, gender, tier, or competition band covered by the rule,
- keep the source that may mint narrow,
- keep duplicate checks and category checks in place,
- record why the ordinary corroborator requirement was waived,
- revisit the rule if another provider later covers that level.

Do not turn a coverage floor into a general shortcut. Above the documented floor, normal
corroboration still applies.

## Matches Are Special

Match identity is best created from a fixture source with a stable provider match ID.
Date, home team, away team, competition, and season are still required, but they are the
resolution and corroboration gate, not the only identity key. Event providers and odds
providers can then attach as bridges.

The public rule is the important part: choose a match spine and make other sources
corroborate it. The private implementation path is not part of the toolkit.

## Minting Audit Packet

Every mint should be explainable later:

- source provider,
- source snapshot,
- source entity ID,
- entity type,
- fields used to prove uniqueness,
- duplicate checks performed,
- creation policy that allowed the mint,
- created timestamp,
- reviewer or automated policy version.

If you cannot reconstruct why an entity was created, later duplicate resolution becomes
guesswork.
