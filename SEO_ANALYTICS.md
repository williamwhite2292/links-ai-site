# SEO and analytics baseline

This doc specifies the technical SEO and analytics setup for the Links AI site. **Rico** uses it for monitoring and reporting.

## Metadata (per page)

- **Title:** Unique per page. Format: `Page Name | Links AI` for subpages; `Links AI` for home.
- **Description:** Meta description, 150–160 chars. Used in search results and OG/Twitter.
- **Canonical:** Every page has a canonical URL. Default: `https://linksaisolutions.com` + path. Override via layout prop when needed (e.g. syndication).
- **Robots:** No `noindex` unless explicitly set (e.g. draft or internal pages).

## Open Graph and Twitter

- **og:type:** `website` for site pages; article pages can use `article` if we add a dedicated blog layout later.
- **og:title, og:description, og:url, og:image:** Set from layout. Default image: `/og-default.png` (create and add to `public/`).
- **twitter:card:** `summary_large_image`.
- **twitter:title, twitter:description, twitter:image:** Mirror OG values.

## Structured data (JSON-LD)

- **Organization:** On every page via `BaseLayout`. Name, url, description, email.
- **Article:** On each blog post page. headline, description, datePublished, dateModified, author, publisher, mainEntityOfPage.

## Sitemap and robots

- **Sitemap:** Static `public/sitemap.xml` listing main pages and current insight posts. When adding new blog posts, append a `<url>` entry for `https://linksaisolutions.com/insights/{slug}/`. Optional: switch to `@astrojs/sitemap` when upgrading Astro if auto-generation is preferred.
- **robots.txt:** In `public/robots.txt`. Allows all user-agents and points to the sitemap.

## Google Analytics

- **Status:** Placeholder. To enable:
  1. Create a GA4 property for the site.
  2. Add the gtag snippet to `BaseLayout.astro` (e.g. in `<head>`) with the measurement ID, or use an Astro analytics integration.
  3. Set the ID via env (e.g. `PUBLIC_GA_ID`) so it can be toggled per environment.
- **Events to track (when implemented):** page_view (default), contact CTA clicks, lead form submissions.

## Search Console (Rico)

- **Setup:** Add and verify the property for `https://linksaisolutions.com` in Google Search Console.
- **Submit:** Submit the sitemap URL: `https://linksaisolutions.com/sitemap-index.xml`.
- **Monitor:** Index coverage, search performance (queries, clicks, impressions), and manual actions. Rico reports on indexing and rankings for target keywords.

## Internal linking

- **Services ↔ Insights:** Link from Services to relevant insight posts where useful. Link from insight posts back to Services or Contact.
- **Navigation:** Header and footer are consistent. Blog posts include “← Insights” back link.
