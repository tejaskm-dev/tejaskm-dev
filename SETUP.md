# Setup & Customization Guide

This repository (`tejaskm-dev/tejaskm-dev`) powers your GitHub Profile README.

---

## Social Badges Quick Reference

To link your personal socials, update the placeholders in `README.md`:

| Badge | Destination |
| :--- | :--- |
| **LinkedIn** | `https://www.linkedin.com/in/tejas-km-73436237b/` |
| **Portfolio** | `https://tejaskm-dev.vercel.app/` |
| **Email** | `mailto:tejaskm2508@gmail.com` |

---

## Featured Project Cards

The 5 featured project cards are located in `assets/cards/` as clean, modular 440 × 165 SVGs:
- `assets/cards/skloop.svg` → [github.com/tejaskm-dev/skloop](https://github.com/tejaskm-dev/skloop) (Live: [skloop.online](https://skloop.online))
- `assets/cards/personal_reader.svg` → [github.com/tejaskm-dev/personal_reader](https://github.com/tejaskm-dev/personal_reader) (Live: [aether-reader-murex.vercel.app](https://aether-reader-murex.vercel.app))
- `assets/cards/name_sandbox.svg` → [github.com/tejaskm-dev/NAME-sandbox](https://github.com/tejaskm-dev/NAME-sandbox) (Live: [name-sandbox-client.vercel.app](https://name-sandbox-client.vercel.app))
- `assets/cards/bounce_celestial.svg` → [github.com/tejaskm-dev/bounce_celestial](https://github.com/tejaskm-dev/bounce_celestial) (Live: [bounce-celestial.vercel.app](https://bounce-celestial.vercel.app))
- `assets/cards/swaram.svg` → [github.com/Chai-T-ORG/swaram](https://github.com/Chai-T-ORG/swaram) (Live: [swaram-three.vercel.app](https://swaram-three.vercel.app))

To re-generate or modify card details, edit `generate_assets.py` and run:
```bash
python3 generate_assets.py
git add assets/cards/
git commit -m "chore: update cards"
git push origin main
```

---

## Contribution Snake Workflow

The `.github/workflows/snake.yml` workflow automatically runs daily at `00:00 UTC` and deploys SVGs to the `output` branch.

- **Output Branch Status:** Active and generating `github-contribution-grid-snake-dark.svg` and `github-contribution-grid-snake.svg`.
