# 🧪 Setup & Configuration Guide

This repository (`tejaskm-dev/tejaskm-dev`) powers your GitHub Profile README. Before pushing changes or after your initial push, replace the placeholders listed below.

---

## 🔍 Placeholders to Replace

Open `README.md` and use your editor's **Find and Replace** (`Cmd + F` or `Ctrl + H`):

| Placeholder | Where It Appears | Description / Example |
| :--- | :--- | :--- |
| `YOUR_GITHUB_USERNAME` | Snake SVG links, Stats cards, Trophies, Activity graph | Your GitHub handle (e.g. `tejaskm-dev`) |
| `YOUR_LINKEDIN` | Top contact badge | Your LinkedIn handle (e.g. `tejas-k-m`) |
| `YOUR_TWITTER` | Top contact badge | Your X/Twitter username (e.g. `shinz_dev`) |
| `YOUR_PORTFOLIO_URL` | Top contact badge | Your personal website/portfolio URL |
| `YOUR_EMAIL@example.com` | Top contact badge | Your contact email address |
| `YOUR_GITHUB_USERNAME/skloop` | Featured Project 01 | Link to Skloop repository or live product |
| `YOUR_GITHUB_USERNAME/aether-reader` | Featured Project 02 | Link to Aether Reader repository/docs |
| `YOUR_GITHUB_USERNAME/name-sandbox` | Featured Project 03 | Link to NAME Sandbox repository/demo |
| `YOUR_GITHUB_USERNAME/academic-integrity-engine` | Featured Project 04 | Link to Academic Integrity Engine repo |

> **Quick Tip:** If you want to do a fast global replacement for your username:
> Replace all instances of `YOUR_GITHUB_USERNAME` with your GitHub username (e.g. `tejaskm-dev`).

---

## 🐍 GitHub Action: Contribution Snake Setup

Your repo includes `.github/workflows/snake.yml`, which automatically builds an animated snake feeding on your contribution grid every 24 hours and deploys SVGs to an isolated `output` branch.

### 1. Enable GitHub Actions Write Permissions (Required)
GitHub Actions must have permission to write and create the `output` branch:
1. Go to your repository on GitHub: `https://github.com/YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME`
2. Navigate to **Settings** → **Actions** → **General**.
3. Scroll down to **Workflow permissions**.
4. Select **Read and write permissions**.
5. Click **Save**.

### 2. Trigger the Initial Run
1. Go to the **Actions** tab in your repository.
2. Under "Workflows" on the left, click **Generate Contribution Snake**.
3. Click the **Run workflow** dropdown on the right and select **Run workflow**.
4. Once completed (takes ~30–45 seconds), an `output` branch will automatically be created containing:
   - `github-contribution-grid-snake.svg`
   - `github-contribution-grid-snake-dark.svg`
5. The `<picture>` element in your `README.md` will instantly render the animated snake in both light and dark mode!

---

## 🎨 Slime Theme Customization (Optional)

The profile is themed around an adaptable, fluid bio-slime / cyber-slime aesthetic:
- **Banner**: Displays `banner.png` directly from the repo root.
- **Typing Header**: Configured in `https://readme-typing-svg.demolab.com` with `#00FF66` slime green.
- **Color Accents**: Widgets and telemetry use neon slime green (`#00FF66`, `#00FF7F`) on deep dark backdrops (`#0d1117`).
- **Footer**: Animated wave footer rendered by `capsule-render` with a multi-stop emerald/slime gradient.
