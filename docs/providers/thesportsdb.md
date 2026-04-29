---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: thesportsdb
entity_types: [player, team, coach, competition, season, match]
access_tier: public_api
source_kind: living
authority_role: metadata_source
bridge_providers: [wikidata, transfermarkt, espn, api_football]
matching_fields:
  [
    thesportsdb_id,
    wikipedia_url,
    wikidata_id,
    transfermarkt_id,
    name,
    date_of_birth,
    nationality,
    country,
  ]
confidence_floor: 1.0
private_dependencies: []
---

# TheSportsDB

TheSportsDB is a community-maintained multi-sport API. Its strongest football identity
feature is the Wikipedia URL field, which can resolve to Wikidata through sitelinks.

## Why It Matters Before You Start

TheSportsDB can turn a community record into a strong public bridge if `strWikipedia`
points to the correct article. It can also carry sibling provider IDs in some payloads.
The tradeoff is community-curated quality and multi-sport noise.

## Entity Model

| Entity type | TheSportsDB term | ID shape       | Notes                           |
| ----------- | ---------------- | -------------- | ------------------------------- |
| Player      | player           | numeric        | Community-maintained.           |
| Team        | team             | numeric        | Often includes Wikipedia link.  |
| Coach       | manager          | numeric/sparse | Coverage is thinner.            |
| Competition | league           | numeric        | Multi-sport; filter football.   |
| Season      | season string    | label          | Usually not a stable entity ID. |
| Match       | event            | numeric        | Multi-sport event model.        |

## Matching Surface

| Field                              | Use                                               | Gotcha                                                  |
| ---------------------------------- | ------------------------------------------------- | ------------------------------------------------------- |
| `strWikipedia`                     | Strong bridge via Wikipedia sitelink to Wikidata. | Validate redirects and disambiguation pages.            |
| Wikidata/Transfermarkt-like fields | Bonus bridges where present.                      | Coverage varies by record.                              |
| DOB/name/nationality               | Fallback player matching.                         | Community fields can be missing or inconsistent.        |
| Team and league names              | Context.                                          | League names may be country-prefixed.                   |
| Sport field                        | Filtering.                                        | Always filter to football/soccer to avoid other sports. |

## Reep-Style Linking Advice

- Resolve `strWikipedia` to a QID and use that as the primary bridge when valid.
- Write sibling provider IDs only when the source field is explicit.
- Treat TheSportsDB as a bridge and metadata source, not an automatic mint source.
- Preserve community-source lineage because records can change.

## Gotchas

- Some Wikipedia URLs point to deleted, redirected, or disambiguation pages.
- Multi-sport data requires explicit filtering.
- Heights and other measurements can mix units.
- Top-flight entries are usually cleaner than long-tail entries.

## References

- [TheSportsDB](https://www.thesportsdb.com/)
- [TheSportsDB API](https://www.thesportsdb.com/api.php)
- [Wikidata sitelinks](https://www.wikidata.org/wiki/Wikidata:Sitelinks)
