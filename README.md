# 🌙 Nappy · Baby Nap Planner

**Free, science-backed baby nap planner. No sign-up, no subscription.**

Live at → [nappy.digital](https://nappy.digital)

---

## What it does

Nappy builds a full-day nap schedule based on your baby's age, tracks sleep in real time, and tells you exactly when the next nap window opens. Awake windows and sleep totals are sourced from board-certified pediatricians and AASM/AAP consensus guidelines.

**Three tabs:**
- **⚡ Right Now** — live countdown to the next nap window, with a sleeping tracker and reminders
- **📋 Plan Day** — full day schedule with nap times, awake windows, and sleep budget tracking
- **📅 This Week** — sleep history saved on your device

**Key features:**
- Age-adaptive awake windows (0–36 months, 14 age bands)
- Sleep budget tracking — logs actual nap times and adjusts remaining nap durations
- Dark mode + auto-detects OS preference
- Export as JPG, PDF, TXT, or Email
- PWA installable — add to Home Screen for native app experience + reminders
- Privacy-first — all data stays in `localStorage` on your device, zero server calls

---

## Tech stack

Single-file HTML app (`index.html`). No framework, no build step, no backend.

- Vanilla JS + CSS
- [html2canvas](https://html2canvas.hertzen.com/) for JPG/PDF export
- [jsPDF](https://parall.ax/products/jspdf) for PDF generation
- [Plausible](https://plausible.io) for privacy-first analytics
- Deployed on [Vercel](https://vercel.com) via GitHub

---

## Sleep science sources

- **Total sleep goals:** AASM/AAP consensus (Paruthi et al., *J Clin Sleep Med* 2016) — reviewed 864 studies, endorsed by the American Academy of Pediatrics
- **Awake windows:** Clinical practice guidelines cross-referenced across multiple board-certified pediatricians and pediatric sleep medicine practitioners
- **Pre-bedtime sleep pressure:** babysleepscience.com, sleep.com, mattressmiracle.ca

> Nappy is for educational purposes only and is not a substitute for professional medical advice. Always follow your baby's individual cues and consult your pediatrician with any concerns.

---

## Running locally

No build step needed. Just open `index.html` in a browser.

```bash
open index.html
```

---

## Deployment

Pushes to `main` auto-deploy via Vercel.

```bash
git add .
git commit -m "your message"
git push origin main
```

---

## About

Built by [Patrick Lee](https://github.com/patleezy).

*Parents need rest. Not another subscription.*
