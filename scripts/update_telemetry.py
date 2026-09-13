import os
import sys
import json
import urllib.request
import subprocess

def get_github_token():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        res = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception:
        return None

def fetch_live_metrics(username="tejaskm-dev"):
    token = get_github_token()
    if not token:
        print("No GitHub token available; using fallback metrics.")
        return {
            "contributions": 731,
            "prs": 68,
            "top_lang": "74% TS",
            "rank": "S+ RANK"
        }

    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          totalCommitContributions
          restrictedContributionsCount
          totalPullRequestContributions
          contributionCalendar {
            totalContributions
          }
        }
        pullRequests(states: MERGED) {
          totalCount
        }
        repositories(ownerAffiliations: OWNER, first: 100, isFork: false) {
          nodes {
            languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
              edges {
                size
                node {
                  name
                }
              }
            }
          }
        }
      }
    }
    """

    req_data = json.dumps({"query": query, "variables": {"login": username}}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=req_data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "ArcadeTelemetry-Updater"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))

        user_data = result.get("data", {}).get("user", {})
        calendar = user_data.get("contributionsCollection", {}).get("contributionCalendar", {})
        total_contributions = calendar.get("totalContributions", 731)
        total_prs = user_data.get("pullRequests", {}).get("totalCount", 68)

        # Calculate programming language percentages (excluding markup/data files)
        excluded_langs = {"HTML", "CSS", "TeX", "MDX", "Markdown", "Dockerfile", "JSON", "YAML", "Plain Text"}
        lang_sizes = {}
        total_code_bytes = 0
        repos = user_data.get("repositories", {}).get("nodes", [])
        for r in repos:
            edges = r.get("languages", {}).get("edges", [])
            for e in edges:
                name = e.get("node", {}).get("name")
                if name not in excluded_langs:
                    size = e.get("size", 0)
                    lang_sizes[name] = lang_sizes.get(name, 0) + size
                    total_code_bytes += size

        # Top language calculation
        ts_size = lang_sizes.get("TypeScript", 0)
        ts_percent = int(round((ts_size / total_code_bytes) * 100)) if total_code_bytes > 0 else 74
        top_lang = f"{ts_percent}% TS"

        # Calculate system rank
        rank = "S+ RANK" if total_contributions >= 500 else "A+ RANK"

        return {
            "contributions": total_contributions,
            "prs": total_prs,
            "top_lang": top_lang,
            "rank": rank
        }
    except Exception as e:
        print(f"Error querying GitHub GraphQL API: {e}; using fallback metrics.")
        return {
            "contributions": 731,
            "prs": 68,
            "top_lang": "74% TS",
            "rank": "S+ RANK"
        }

def render_arcade_hud(metrics):
    contributions = f"{metrics['contributions']}+"
    prs = f"{metrics['prs']}+"
    top_lang = metrics['top_lang']
    rank = metrics['rank']

    svg = f'''<svg width="900" height="260" viewBox="0 0 900 260" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="stationBg" x1="0" y1="0" x2="900" y2="260" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#141a16"/>
      <stop offset="100%" stop-color="#0b110e"/>
    </linearGradient>
    <linearGradient id="slimeGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>
  </defs>

  <!-- Main Chassis -->
  <rect x="2" y="2" width="896" height="256" rx="20" fill="url(#stationBg)" stroke="#1e2c24" stroke-width="1.5"/>

  <!-- Left: Game Station Player Card -->
  <g transform="translate(28, 26)">
    <!-- Game Controller Icon -->
    <rect x="0" y="4" width="56" height="36" rx="18" fill="#18271e" stroke="#10B981" stroke-width="1.5"/>
    <path d="M 16 22 H 24 M 20 18 V 26" stroke="#34D399" stroke-width="2" stroke-linecap="round"/>
    <circle cx="38" cy="24" r="2.5" fill="#38bdf8"/>
    <circle cx="44" cy="19" r="2.5" fill="#facc15"/>
    <circle cx="38" cy="15" r="2.5" fill="#34D399"/>

    <text x="68" y="22" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="16" font-weight="900" letter-spacing="-0.3">ARCADE TELEMETRY STATION</text>
    <text x="68" y="38" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500">Player: tejaskm-dev • Level 01 Architect • ASIET CSE (2025-2029)</text>

    <!-- Directive Focus Bar (No fake dots, no blinking) -->
    <g transform="translate(0, 54)">
      <rect width="470" height="34" rx="8" fill="#10251c" stroke="#10B981" stroke-opacity="0.4" stroke-width="1"/>
      <text x="16" y="21" fill="#34D399" font-family="'Inter', sans-serif" font-size="10" font-weight="900" letter-spacing="0.5">DIRECTIVE:</text>
      <text x="88" y="21" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="11" font-weight="600">Building Skloop • Directing AI Engines • AST Sandbox</text>
    </g>

    <!-- Telemetry Meters / Score Tickers -->
    <g transform="translate(0, 102)">
      <!-- Box 1: Commits / Contributions -->
      <rect x="0" y="0" width="110" height="56" rx="10" fill="#152119" stroke="#1e3226"/>
      <text x="55" y="26" text-anchor="middle" fill="#34D399" font-family="'Inter', sans-serif" font-size="18" font-weight="900">{contributions}</text>
      <text x="55" y="44" text-anchor="middle" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="9" font-weight="600">CONTRIBUTIONS</text>

      <!-- Box 2: PRs -->
      <rect x="120" y="0" width="110" height="56" rx="10" fill="#152119" stroke="#1e3226"/>
      <text x="175" y="26" text-anchor="middle" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="18" font-weight="900">{prs}</text>
      <text x="175" y="44" text-anchor="middle" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="9" font-weight="600">PRS MERGED</text>

      <!-- Box 3: Code Rank -->
      <rect x="240" y="0" width="110" height="56" rx="10" fill="#152119" stroke="#1e3226"/>
      <text x="295" y="26" text-anchor="middle" fill="#facc15" font-family="'Inter', sans-serif" font-size="18" font-weight="900">{rank}</text>
      <text x="295" y="44" text-anchor="middle" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="9" font-weight="600">SYSTEM HEALTH</text>

      <!-- Box 4: Top Syntax -->
      <rect x="360" y="0" width="110" height="56" rx="10" fill="#152119" stroke="#1e3226"/>
      <text x="415" y="26" text-anchor="middle" fill="#34D399" font-family="'Inter', sans-serif" font-size="16" font-weight="900">{top_lang}</text>
      <text x="415" y="44" text-anchor="middle" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="9" font-weight="600">CORE SYNTAX</text>
    </g>

    <!-- Slime Fluidity Bar -->
    <g transform="translate(0, 172)">
      <text x="0" y="12" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="10" font-weight="700" letter-spacing="0.5">SLIME FLUIDITY INDEX</text>
      <text x="470" y="12" text-anchor="end" fill="#34D399" font-family="'Inter', sans-serif" font-size="10" font-weight="800">100% MAXIMUM ADAPTIVITY</text>
      <rect x="0" y="18" width="470" height="8" rx="4" fill="#0d1b13"/>
      <rect x="0" y="18" width="470" height="8" rx="4" fill="url(#slimeGrad)"/>
    </g>
  </g>

  <!-- Vertical Divider -->
  <line x1="525" y1="24" x2="525" y2="236" stroke="#ffffff" stroke-opacity="0.08"/>

  <!-- Right: Tactile Doodles & Fun Stickers (Directly from Picture 3!) -->
  <g transform="translate(545, 24)">
    <!-- Sticky Note 1 (Yellow Post-It tilted with tape) -->
    <g transform="rotate(-3, 60, 50)">
      <rect x="3" y="3" width="135" height="95" rx="3" fill="#05150d" opacity="0.4"/>
      <rect x="0" y="0" width="135" height="95" rx="3" fill="#fef08a"/>
      <rect x="42" y="-7" width="50" height="16" rx="2" fill="#ffffff" opacity="0.6" stroke="#e2e8f0" stroke-width="0.5"/>
      <text x="16" y="28" fill="#854d0e" font-family="'Inter', sans-serif" font-size="11" font-weight="900" letter-spacing="0.5">SMALL</text>
      <text x="16" y="44" fill="#854d0e" font-family="'Inter', sans-serif" font-size="11" font-weight="900" letter-spacing="0.5">PROJECTS</text>
      <text x="16" y="60" fill="#854d0e" font-family="'Inter', sans-serif" font-size="11" font-weight="900" letter-spacing="0.5">BIG IMPACT</text>
      <!-- Smile Doodle -->
      <path d="M 16 75 Q 24 82, 32 75" stroke="#854d0e" stroke-width="2" stroke-linecap="round" fill="none"/>
      <circle cx="19" cy="71" r="1.5" fill="#854d0e"/>
      <circle cx="29" cy="71" r="1.5" fill="#854d0e"/>
    </g>

    <!-- Doodle: Green Crown + PLAY LEARN REPEAT -->
    <g transform="translate(160, 8)">
      <polygon points="10,20 18,8 26,18 34,8 42,20 38,24 14,24" fill="none" stroke="#34D399" stroke-width="2" stroke-linejoin="round"/>
      <text x="10" y="42" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="900" letter-spacing="1">PLAY</text>
      <text x="10" y="56" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="900" letter-spacing="1">LEARN</text>
      <text x="10" y="70" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="900" letter-spacing="1">REPEAT</text>
    </g>

    <!-- Sticky Note 2 (Warm Kraft note tilted) -->
    <g transform="translate(125, 120) rotate(2)">
      <rect x="2" y="2" width="165" height="78" rx="3" fill="#05150d" opacity="0.4"/>
      <rect x="0" y="0" width="165" height="78" rx="3" fill="#fed7aa"/>
      <rect x="58" y="-6" width="48" height="15" rx="2" fill="#ffffff" opacity="0.5"/>
      <text x="16" y="28" fill="#7c2d12" font-family="'Inter', sans-serif" font-size="11" font-weight="800">good ideas</text>
      <text x="16" y="44" fill="#7c2d12" font-family="'Inter', sans-serif" font-size="11" font-weight="800">later... :)</text>
      <text x="16" y="62" fill="#9a3412" font-family="'Inter', sans-serif" font-size="9" font-weight="600">better devs • brighter</text>
    </g>
  </g>
</svg>'''
    return svg

def update_hud():
    print("Fetching live metrics for tejaskm-dev...")
    metrics = fetch_live_metrics("tejaskm-dev")
    print(f"Live Metrics: {metrics}")
    svg_content = render_arcade_hud(metrics)
    os.makedirs("assets", exist_ok=True)
    with open("assets/arcade_hud.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Updated assets/arcade_hud.svg successfully with live metrics!")

if __name__ == "__main__":
    update_hud()
