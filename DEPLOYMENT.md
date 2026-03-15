# Deployment Path (Links AI Site)

**Status:** GitHub repo created ✓  
**Created:** 2026-03-15  
**Updated:** 2026-03-15  
**Owner:** Carl (Engineering)

## Current State

- Site workspace: `/home/ubuntu/.openclaw/workspace/links-ai-site`
- GitHub repo: https://github.com/willag-trey/links-ai-site
- Framework: Astro 4.16.0
- Build output: `dist/` (static files)
- Domain: `linksaisolutions.com`
- Sitemap: Auto-generated via `@astrojs/sitemap`

## Deployment Options

### Option 1: GitHub + Vercel/Netlify (Recommended)

**Prerequisites:**
- GitHub repo created (pending GitHub auth)
- Vercel or Netlify account connected

**Flow:**
1. Push site code to GitHub repo
2. Connect Vercel/Netlify to repo
3. Set domain `linksaisolutions.com`
4. Auto-deploy on push to main

**Pros:**
- CI/CD built-in
- Preview deployments for PRs
- Easy rollbacks
- HTTPS auto-configured

### Option 2: GitHub + Cloudflare Pages

**Flow:**
1. Push to GitHub
2. Connect Cloudflare Pages
3. Set custom domain
4. Auto-deploy on push

**Pros:**
- Fast global CDN
- Good for SEO performance
- Integrated with Cloudflare DNS

### Option 3: VPS Direct Deploy (Current Fallback)

**Flow:**
1. Build locally: `npm run build`
2. SCP/rsync `dist/` to VPS web root
3. Serve via nginx

**Pros:**
- No external dependencies
- Full control

**Cons:**
- Manual or scripted deploys
- No preview environments

## Recommended Next Steps

1. ~~**Complete GitHub auth** (Rico/Trey) to create `links-ai-site` repo~~ ✓ Done
2. **Choose platform:** Vercel (fastest setup) or Cloudflare Pages (best performance)
3. **Configure DNS:** Point `linksaisolutions.com` to chosen platform
4. **Set up branch protection:** Require PRs for main branch
5. **Add deploy hooks:** Optional - trigger rebuild from Paperclip on content approval

## Repository

- **URL:** https://github.com/willag-trey/links-ai-site
- **Local:** `/home/ubuntu/.openclaw/workspace/links-ai-site`
- **Remote:** `origin` → `https://github.com/willag-trey/links-ai-site.git`
- **Default branch:** `main`

## Environment Variables

None currently required. If adding forms/API later:
- `PUBLIC_API_ENDPOINT` (if needed for client-side JS)

## Build Verification

```bash
cd /home/ubuntu/.openclaw/workspace/links-ai-site
npm install
npm run build
# Output in dist/ ready for deployment
```

Build verified working on 2026-03-15.
