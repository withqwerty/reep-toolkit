---
doc_type: practice_guide
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, match]
matching_fields:
  [provider_id, name, date_of_birth, country, competition, season, match_date]
confidence_floor: 0.95
---

# Before You Ingest a Provider

Most register damage happens before the matcher runs. The usual cause is not bad string
similarity. It is a wrong assumption about the provider's world model.

Before ingesting a provider, answer these questions.

## 1. What Entity Level Does Each ID Represent?

Do not assume a provider's `league_id`, `season_id`, or `team_id` means the same thing
your register means.

| Provider field | Could mean                                                   | Question to answer                            |
| -------------- | ------------------------------------------------------------ | --------------------------------------------- |
| `league_id`    | competition, division, season, stage, product bucket         | Is this the family or a specific edition?     |
| `season_id`    | parent season, stage, calendar year, provider product cycle  | Does it map one-to-one to your season entity? |
| `team_id`      | club, senior team, women's team, reserve team, national team | What category of team is identified?          |
| `player_id`    | player identity, person identity, season roster row          | Does it persist across transfers and seasons? |
| `match_id`     | fixture, event feed, leg, aggregate tie, replay              | What real-world object is this ID naming?     |

If the answer is unclear, document the uncertainty and defer writes.

## 2. Is the Provider a Creation Source?

A provider can be excellent for matching without being allowed to mint new register
entities.

| Source role     | What it can do                                                   |
| --------------- | ---------------------------------------------------------------- |
| Creation source | Mint entities under documented rules.                            |
| Bridge source   | Attach provider IDs to existing entities.                        |
| Metadata source | Add aliases, DOB, positions, country, or context.                |
| Coverage probe  | Show that an entity probably exists but needs stronger evidence. |

The safest default: new providers attach bridges and produce candidates first. Minting
is a later policy decision.

## 3. Are IDs Stable?

Check whether IDs are:

- permanent profile IDs,
- per-season roster IDs,
- URL slugs,
- legacy IDs that redirect,
- numeric IDs that live in separate namespaces,
- IDs reused across entity types.

Stable-looking integers are not automatically stable identities.

## 4. What Bridges Exist?

Strong bridge fields radically change the matcher design.

Ask:

- Does the provider expose Wikidata, Transfermarkt, FBref, Opta numeric, Soccerdonna, or
  another external ID?
- Is that bridge direct or derived?
- Is it typed by entity?
- Is it complete or sparse?
- Can it conflict with existing bridges?

Direct bridges run before biographical matching unless the provider card documents a
reason to distrust them.

## 5. What Fields Are Matchable?

Separate identity fields from display fields.

| Good matching fields        | Weak or contextual fields |
| --------------------------- | ------------------------- |
| provider ID                 | shirt number              |
| date of birth               | current squad number      |
| full name                   | position-only             |
| native name / aliases       | current team without date |
| country/nationality         | market value              |
| founded year                | competition display label |
| match date + resolved teams | round name alone          |

Stats are almost never identity evidence.

## 6. What Is the Failure Mode?

Every provider has a predictable way to create bad matches:

- name-only team collisions,
- player/coach namespace confusion,
- parent club versus team-section confusion,
- league versus season confusion,
- legacy ID redirects,
- multi-sport contamination,
- women's and men's team conflation,
- youth/reserve/senior team conflation,
- date format swaps,
- stale current-team fields.

Write the failure mode down before writing the matcher.

## 7. What Should Be Reviewed?

Do not wait until after ingestion to design review routing.

Route to review when:

- the match uses weak evidence,
- a bridge conflicts with existing data,
- the provider ID is new but the entity probably exists,
- the entity level is unclear,
- a provider field is known to be stale or derived,
- a mint would create a public ID from insufficient evidence.

## Reep-Style Summary

Provider ingestion should begin with a provider card, not a script. Once the provider's
world model is clear, implementation is usually straightforward. When the world model is
wrong, even clean code produces bad register data.

## Worked Example

See [Provider ingest walkthrough](../examples/provider-ingest-walkthrough.md) for a full
provider-card-to-write-set example using a signal-only provider.
