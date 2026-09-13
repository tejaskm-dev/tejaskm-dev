# Setup & Customization Guide

This repository (`tejaskm-dev/tejaskm-dev`) powers your GitHub Profile README.

---

## Social Badges Quick Reference

To link your personal socials, update the placeholders in `README.md`:

| Badge | Current Link | What to Replace |
| :--- | :--- | :--- |
| **LinkedIn** | `https://linkedin.com/in/YOUR_LINKEDIN` | Replace `YOUR_LINKEDIN` with your LinkedIn username |
| **X (Twitter)** | `https://x.com/YOUR_TWITTER` | Replace `YOUR_TWITTER` with your X handle |
| **Portfolio** | `https://YOUR_PORTFOLIO_URL` | Replace `YOUR_PORTFOLIO_URL` with your portfolio domain |
| **Email** | `mailto:YOUR_EMAIL@example.com` | Replace `YOUR_EMAIL@example.com` with your address |

---

## Visual Assets & Project Cards

All visual project cards and headers are rendered via local SVGs stored in the `assets/` directory:
- `assets/slime-hud.svg` — Animated pulsing cyber-slime telemetry terminal with scanning beam
- `assets/cards/skloop.svg` — Visual card for Skloop (In Active Development)
- `assets/cards/aether.svg` — Visual card for Aether Reader PWA
- `assets/cards/name-sandbox.svg` — Visual card for NAME Sandbox & AST rule compiler
- `assets/cards/academic-engine.svg` — Visual card for the Academic Integrity Engine
- `assets/cards/side-quests.svg` — Visual dual card for Swaram and Operation Vault
- `assets/headers/` — Custom neon section dividers (`header-about.svg`, `header-projects.svg`, etc.)

To re-generate or adjust any card text or styling, edit `generate_assets.py` and execute:
```bash
python3 generate_assets.py
git add assets/
git commit -m "chore: update visual cards"
git push origin main
```

---

## Contribution Snake Workflow

The `.github/workflows/snake.yml` workflow automatically runs daily at `00:00 UTC` and deploys SVGs to the `output` branch.

- **Output Branch Status:** Active and populated with `github-contribution-grid-snake-dark.svg` and `github-contribution-grid-snake.svg`.
- **Permissions:** If you ever reconfigure your GitHub repository permissions, ensure **Settings → Actions → General → Workflow permissions** is set to **Read and write permissions**.
