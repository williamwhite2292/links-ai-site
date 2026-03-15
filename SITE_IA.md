# Links AI site — information architecture

This document defines the site structure and Astro framework layout used for the rebuild.

## Pages

| Route | Purpose |
|-------|--------|
| `/` | Home — positioning, what we do, process, primary CTA |
| `/how-it-works` | Process: exploratory call → opportunity map → build → support |
| `/services` | Commercial ladder in buyer language |
| `/insights` | Blog index; links to individual posts at `/insights/[slug]` |
| `/contact` | Lead form and contact CTA |

## Framework structure

- **Layout:** `src/layouts/BaseLayout.astro` — shared head, nav, footer, hero slot.
- **Styles:** `src/styles/global.css` — ported from original site; imported in layout.
- **Pages:** `src/pages/*.astro` — one file per route; insights use `src/pages/insights/index.astro` and (Phase 2) `src/pages/insights/[...slug].astro` for posts.
- **Content:** `src/content/blog/` — blog posts as Markdown with frontmatter (Phase 2).
- **Static assets:** `public/` — favicon, images; copied as-is.

## Navigation

- Header: Home (brand), How it works, Services, Insights, Get in touch.
- Footer: brand link, email, copyright.
- All CTAs point to `/contact` or in-page `#contact` where relevant.

## Content workflow (agents)

- **Arlo** → briefs in shared workspace.
- **Dante** → drafts in shared workspace.
- **Abby** → approves in shared workspace.
- **Carl** → copies approved post into `src/content/blog/` in this repo and builds.
- **Rico** → monitors indexing and performance post-publish.
