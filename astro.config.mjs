import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  integrations: [
    starlight({
      title: "Reep Toolkit",
      description:
        "Public football identity-resolution docs, provider reference, worked examples, and reference scripts.",
      customCss: ["./src/styles/custom.css"],
      sidebar: [
        {
          label: "Start Here",
          items: [
            { label: "Overview", slug: "index" },
            { label: "Docs Index", slug: "docs-index" },
            { label: "Guide Site Model", slug: "site-model" },
          ],
        },
        {
          label: "World Model",
          items: [{ autogenerate: { directory: "world-model" } }],
        },
        {
          label: "Provider Reference",
          items: [
            { label: "Provider Overview", slug: "providers/index" },
            { label: "Provider Catalogue", slug: "providers/catalogue" },
            { label: "Source Taxonomy", slug: "providers/sources" },
            { label: "Transfermarkt", slug: "providers/transfermarkt" },
            { label: "Opta / Stats Perform", slug: "providers/opta" },
            { label: "StatsBomb", slug: "providers/statsbomb" },
            { label: "SportMonks", slug: "providers/sportmonks" },
            { label: "WhoScored", slug: "providers/whoscored" },
            { label: "API-Football", slug: "providers/api-football" },
            { label: "Capology", slug: "providers/capology" },
            { label: "Club Elo", slug: "providers/clubelo" },
            { label: "FBref", slug: "providers/fbref" },
            {
              label: "Football-Data.co.uk",
              slug: "providers/football-data-co-uk",
            },
            { label: "FotMob", slug: "providers/fotmob" },
            { label: "Fantasy Premier League", slug: "providers/fpl" },
            { label: "Livesport Ecosystem", slug: "providers/livesport" },
            { label: "Soccerdonna", slug: "providers/soccerdonna" },
            { label: "SoFIFA", slug: "providers/sofifa" },
            { label: "TheSportsDB", slug: "providers/thesportsdb" },
            { label: "Understat", slug: "providers/understat" },
            { label: "SkillCorner", slug: "providers/skillcorner" },
            { label: "Impect Ecosystem", slug: "providers/impect" },
            { label: "Wikidata", slug: "providers/wikidata" },
          ],
        },
        {
          label: "Practice Guides",
          items: [{ autogenerate: { directory: "guides" } }],
        },
        {
          label: "Pipeline Patterns",
          items: [{ autogenerate: { directory: "pipelines" } }],
        },
        {
          label: "Worked Examples",
          items: [{ autogenerate: { directory: "examples" } }],
        },
        {
          label: "Contributing",
          items: [
            { label: "Contributing", slug: "contributing" },
            { label: "Editorial Standard", slug: "editorial" },
            { label: "Front Matter", slug: "frontmatter" },
          ],
        },
      ],
    }),
  ],
});
