# CLAUDE.md — Nappy Context

This file gives Claude context for working on Nappy across sessions.

---

## What this project is

Nappy is a single-file HTML baby nap planner at `index.html`. No framework, no build system, no backend. Everything — HTML, CSS, JS — lives in one file. Deployed on Vercel via GitHub (`github.com/patleeazy/nappy`), live at `nappy.digital`.

---

## Architecture

**Single file:** `index.html` (~1600 lines)
- All CSS in `<style>` block in `<head>`
- All JS in `<script>` block before `</body>`
- No npm, no node_modules, no build step

**Key JS functions:**
- `getSleep(wks)` — returns age-appropriate sleep data (awake windows, nap count, bedtime buffer, totals)
- `buildPlan()` — constructs the full day nap schedule with sleep budget tracking
- `calc()` — main Plan Day calculator, renders the timeline
- `predict()` — Right Now tab live countdown logic
- `napSt(n)` — determines live status of each nap (past/now/window/future)
- `isPlanningToday()` — gates live time logic to today's date only

**External dependencies (CDN):**
- html2canvas 1.4.1 (JPG/PDF export)
- jsPDF 2.5.1 (PDF generation)
- Plausible analytics (privacy-first, no cookies)
- Google Fonts: Cormorant Garamond + Nunito

**Storage:** `localStorage` only. Keys:
- `nappy_dark` — dark mode preference
- `nappy_h` — sleep history (last 14 days)
- `nappy_install_dismissed` — PWA banner state

---

## Design system

**Light mode:** warm cream palette (`#FAF7F2` bg, `#4A3828` text)
**Dark mode:** deep navy (`#111820` bg, `#E5D8CC` text)

CSS variables: `--bg`, `--card`, `--text`, `--muted`, `--border`, `--inp`, plus semantic colors `--rose`, `--green`, `--purple`, `--blue`, `--amber` each with `-bg` and `-lt` variants.

Font stack: Cormorant Garamond (serif, headings/numbers), Nunito (sans, body)

---

## Sleep science

Awake windows sourced from:
1. Cleveland Clinic / Dr. Kristin Barrett MD (Apr 2024)
2. Huckleberry / Dr. Gina Jansheski MD FAAP (Dec 2025)
3. care.com / Dr. Jenelle Ferry, neonatologist (2024)

Total sleep goals: AASM/AAP consensus (Paruthi et al., J Clin Sleep Med 2016).

`bedBuf` — minimum wake time before bedtime per age band (60–300 min). Prevents naps ending too close to bedtime, which reduces sleep pressure for overnight.

---

## Deploy workflow

```bash
# After editing index.html locally:
git add index.html
git commit -m "description"
git push origin main
# Vercel auto-deploys in ~20 seconds
```

Other files in repo: `manifest.json`, `og-image.png`, `icon-192.png`, `icon-512.png`, `icon-180.png`, `vercel.json` (security headers).

---

## Known decisions & tradeoffs

- **No AI features yet** — intentional. Adding an "Ask Nappy" AI chat is scoped as a future paid feature using a Vercel serverless proxy pattern (API key never touches client).
- **No shareable plan links** — URL encoding was considered but rejected due to fragility with long URLs in messaging apps.
- **SVG favicon** — inline data URI, no extra file needed.
- **OG image is PNG** — SVG was tried first but most social crawlers (iMessage, WhatsApp) don't render SVG og:images.
- **Notifications on iOS** — only available when installed as PWA (Home Screen). The menu has install instructions and a clipboard fallback for Safari tabs.
- **Single file** — deliberate. Keeps deployment trivial and removes all build complexity. Only reconsider if AI backend or auth is added.

---

## Security

- No API keys in frontend (nothing to expose)
- Baby name sanitized via `san()` before `innerHTML` (XSS prevention)
- SRI integrity hashes on CDN scripts
- Security headers via `vercel.json` (CSP, X-Frame-Options, Referrer-Policy, Permissions-Policy)
- OWASP Top 10 audited — clean as of April 2026
