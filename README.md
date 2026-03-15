# Links AI Site

This directory is the independent workspace for the `Links AI` website.

It lives alongside the `paperclip` repo so the public site can be designed, built, hosted, and versioned independently from the internal operating system.

## Purpose

This site is the external credibility layer for `Links AI`.

It should:

- explain what `Links AI` is in buyer language
- show who it helps and how engagements work
- present practical first use cases without over-niching the brand
- create trust and legitimacy during outreach
- leave room for the deeper agent-infrastructure story to emerge over time

It should not:

- expose internal architecture jargon too early
- market `Links AI` as only an “agent company”
- force the public message to match every internal implementation detail

## Relationship to `paperclip`

- `paperclip/` is the internal operating system and design/provisioning repo
- `links-ai-site/` is the public-facing website workspace

The website should translate the business model from the `paperclip` repo into clear external messaging.
It should not become a duplicate system of record for internal operations.

## Initial files

- `SITE_STRATEGY.md` -- what the website is for, who it is for, and what it must communicate
- `HOMEPAGE_COPY.md` -- draft homepage structure and messaging blocks
- `BLOG_STRATEGY.md` -- proof/content strategy for the blog or insights section
- `index.html` -- homepage markup
- `styles.css` -- site styling
- `app.js` -- client-side lead form submission
- `server.py` -- local server and lead capture endpoint

## Working principle

Start simple.

First define:

1. positioning
2. homepage message
3. trust/proof structure
4. CTA path

Then choose the technical stack and build the actual site.

## Local preview

Run the site locally with the form backend enabled:

```bash
python3 server.py
```

Then open:

`http://127.0.0.1:4173`

Lead submissions are stored locally in `data/leads.db`.
