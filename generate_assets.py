import os

def generate_all_assets():
    os.makedirs('assets/badges', exist_ok=True)
    os.makedirs('assets/cards', exist_ok=True)
    os.makedirs('assets/headers', exist_ok=True)

    # -------------------------------------------------------------
    # 1. SECTION HEADERS (Distinct visual hierarchy for every section)
    # -------------------------------------------------------------
    headers = [
        ("01_directive.svg", "01", "ARCHITECTURAL DIRECTIVE &amp; BIO", "#10B981", "#052e16", "PHILOSOPHY"),
        ("02_projects.svg", "02", "FEATURED ARTIFACTS &amp; BUILDS", "#22d3ee", "#083344", "PORTFOLIO"),
        ("03_techstack.svg", "03", "CORE TECH &amp; DIRECTIVE STACK", "#38bdf8", "#082f49", "CAPABILITIES"),
        ("04_roles.svg", "04", "COMMUNITY ENGAGEMENT &amp; ROLES", "#facc15", "#422006", "COMMUNITIES"),
        ("05_telemetry.svg", "05", "ARCADE TELEMETRY &amp; METRICS", "#34D399", "#064e3b", "TELEMETRY"),
    ]

    for filename, num, title, color, bg_pill, tag in headers:
        svg = f'''<svg width="900" height="50" viewBox="0 0 900 50" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hdrBg_{num}" x1="0" y1="0" x2="900" y2="50" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#141916"/>
      <stop offset="100%" stop-color="#0c110e"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="898" height="48" rx="10" fill="url(#hdrBg_{num})" stroke="{color}" stroke-opacity="0.3" stroke-width="1.2"/>
  
  <!-- Number Pill -->
  <g transform="translate(16, 12)">
    <rect width="36" height="26" rx="6" fill="{bg_pill}" stroke="{color}" stroke-opacity="0.6"/>
    <text x="18" y="17" text-anchor="middle" fill="{color}" font-family="'Inter', sans-serif" font-size="12" font-weight="900">{num}</text>
  </g>

  <!-- Title -->
  <text x="66" y="31" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="14" font-weight="800" letter-spacing="1">{title}</text>

  <!-- Accent Line -->
  <line x1="420" y1="25" x2="780" y2="25" stroke="{color}" stroke-opacity="0.2" stroke-width="1" stroke-dasharray="4 4"/>

  <!-- Right Tag -->
  <g transform="translate(800, 14)">
    <rect width="84" height="22" rx="11" fill="{bg_pill}" stroke="{color}" stroke-opacity="0.4"/>
    <text x="42" y="15" text-anchor="middle" fill="{color}" font-family="'Inter', sans-serif" font-size="9" font-weight="700" letter-spacing="0.8">{tag}</text>
  </g>
</svg>'''
        with open(os.path.join('assets/headers', filename), 'w') as f:
            f.write(svg)

    # -------------------------------------------------------------
    # 2. CONTACT BADGES (Official logos, clear spacing, high contrast)
    # -------------------------------------------------------------
    linkedin_svg = '''<svg width="130" height="34" viewBox="0 0 130 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="130" height="34" rx="8" fill="#0e241b" stroke="#10B981" stroke-width="1.2"/>
  <g transform="translate(12, 8)">
    <rect width="18" height="18" rx="3.5" fill="#10B981"/>
    <path d="M5 8H7.5V14.5H5V8Z" fill="#071b12"/>
    <circle cx="6.25" cy="5.5" r="1.25" fill="#071b12"/>
    <path d="M9 8H11.5V9C11.8 8.4 12.6 8 13.5 8C15 8 16 9 16 11V14.5H13.5V11.5C13.5 10.8 13.2 10.2 12.5 10.2C11.8 10.2 11.5 10.8 11.5 11.5V14.5H9V8Z" fill="#071b12"/>
  </g>
  <text x="38" y="22" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="12" font-weight="800" letter-spacing="0.5">LINKEDIN</text>
</svg>'''

    portfolio_svg = '''<svg width="140" height="34" viewBox="0 0 140 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="140" height="34" rx="8" fill="#0e241b" stroke="#10B981" stroke-width="1.2"/>
  <g transform="translate(12, 8)">
    <circle cx="9" cy="9" r="8" stroke="#10B981" stroke-width="1.5"/>
    <ellipse cx="9" cy="9" rx="3.5" ry="8" stroke="#10B981" stroke-width="1.2"/>
    <line x1="1" y1="9" x2="17" y2="9" stroke="#10B981" stroke-width="1.2"/>
  </g>
  <text x="38" y="22" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="12" font-weight="800" letter-spacing="0.5">PORTFOLIO</text>
</svg>'''

    email_svg = '''<svg width="115" height="34" viewBox="0 0 115 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="115" height="34" rx="8" fill="#0e241b" stroke="#10B981" stroke-width="1.2"/>
  <g transform="translate(12, 9)">
    <rect width="18" height="15" rx="2.5" stroke="#10B981" stroke-width="1.5"/>
    <path d="M1 3L9 9.5L17 3" stroke="#10B981" stroke-width="1.5" stroke-linecap="round"/>
  </g>
  <text x="38" y="22" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="12" font-weight="800" letter-spacing="0.5">EMAIL</text>
</svg>'''

    with open('assets/badges/linkedin.svg', 'w') as f:
        f.write(linkedin_svg)
    with open('assets/badges/portfolio.svg', 'w') as f:
        f.write(portfolio_svg)
    with open('assets/badges/email.svg', 'w') as f:
        f.write(email_svg)

    # -------------------------------------------------------------
    # 3. PICTURE-3 TACTILE PROJECT CARDS (Clean static category pills, zero dots)
    # -------------------------------------------------------------
    # Skloop
    skloop = '''<svg width="310" height="370" viewBox="0 0 310 370" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="skBg" x1="0" y1="0" x2="310" y2="370" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#141916"/>
      <stop offset="100%" stop-color="#0d120f"/>
    </linearGradient>
    <linearGradient id="skSlime" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4ade80"/>
      <stop offset="100%" stop-color="#16a34a"/>
    </linearGradient>
  </defs>

  <!-- Card Body -->
  <rect x="1" y="1" width="308" height="368" rx="20" fill="url(#skBg)" stroke="#1e2c24" stroke-width="1.5"/>

  <!-- 3D Folder Logo with Slime & Stickers -->
  <g transform="translate(24, 24)">
    <path d="M4 14C4 10.6863 6.68629 8 10 8H28L34 14H64C67.3137 14 70 16.6863 70 20V58C70 61.3137 67.3137 64 64 64H10C6.68629 64 4 61.3137 4 58V14Z" fill="#1b251f"/>
    <g transform="translate(18, -4)">
      <ellipse cx="20" cy="24" rx="16" ry="14" fill="url(#skSlime)"/>
      <ellipse cx="14" cy="18" rx="5" ry="2.5" transform="rotate(-30 14 18)" fill="#ffffff" opacity="0.6"/>
      <circle cx="15" cy="24" r="2" fill="#052e16"/>
      <circle cx="25" cy="24" r="2" fill="#052e16"/>
      <path d="M 18 28 Q 20 31, 22 28" stroke="#052e16" stroke-width="1.5" stroke-linecap="round" fill="none"/>
    </g>
    <path d="M2 24C2 20.6863 4.68629 18 8 18H66C69.3137 18 72 20.6863 72 24V60C72 63.3137 69.3137 66 66 66H8C4.68629 66 2 63.3137 2 60V24Z" fill="#24332a" stroke="#34483b" stroke-width="1"/>
    <rect x="8" y="28" width="36" height="18" rx="3" fill="#e2e8f0"/>
    <text x="12" y="37" fill="#0f172a" font-family="'Inter', sans-serif" font-size="6" font-weight="900">LEARN</text>
    <text x="12" y="43" fill="#0f172a" font-family="'Inter', sans-serif" font-size="6" font-weight="900">BUILD</text>
    <polygon points="54,34 56,38 60,38 57,41 58,45 54,42 50,45 51,41 48,38 52,38" fill="#facc15"/>
  </g>

  <!-- Clean Category Pill (No dot, No pulse, No fake active) -->
  <g transform="translate(180, 24)">
    <rect x="0" y="0" width="106" height="22" rx="11" fill="#0e2a1e" stroke="#10B981" stroke-opacity="0.6"/>
    <text x="53" y="15" text-anchor="middle" fill="#34D399" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" letter-spacing="0.5">EDTECH PLATFORM</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="24" y="145" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="28" font-weight="800" letter-spacing="-0.5">skloop</text>
  <text x="24" y="172" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Gamified EdTech Platform</text>

  <!-- Description -->
  <text x="24" y="210" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="12" font-weight="500">Turn lessons into levels.</text>
  <text x="24" y="230" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11.5">Build real skills, one streak at a time.</text>
  <text x="24" y="250" fill="#64748B" font-family="'Inter', sans-serif" font-size="11">Quizzes, XP loops &amp; Monaco editor.</text>

  <!-- Divider Line -->
  <line x1="24" y1="295" x2="286" y2="295" stroke="#FFFFFF" stroke-opacity="0.08"/>

  <!-- Bottom Row: Language + Link -->
  <g transform="translate(24, 325)">
    <circle cx="4" cy="0" r="4" fill="#38bdf8"/>
    <text x="14" y="4" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11">TypeScript</text>
    <text x="262" y="4" text-anchor="end" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="600">skloop.online ↗</text>
    <path d="M 185 10 Q 223 13, 262 10" stroke="#34D399" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  </g>
</svg>'''

    # Aether Reader
    aether = '''<svg width="310" height="370" viewBox="0 0 310 370" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="aeBg" x1="0" y1="0" x2="310" y2="370" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#141918"/>
      <stop offset="100%" stop-color="#0d1312"/>
    </linearGradient>
    <linearGradient id="mangaSpine" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="308" height="368" rx="20" fill="url(#aeBg)" stroke="#1e2c29" stroke-width="1.5"/>

  <!-- 3D Manga Volume / E-Reader Device -->
  <g transform="translate(24, 24)">
    <rect x="6" y="4" width="46" height="60" rx="4" fill="#0e2a30"/>
    <rect x="0" y="0" width="48" height="62" rx="4" fill="#153e47" stroke="#22d3ee" stroke-opacity="0.5" stroke-width="1"/>
    <rect x="0" y="0" width="8" height="62" rx="2" fill="url(#mangaSpine)"/>
    <line x1="14" y1="12" x2="40" y2="12" stroke="#22d3ee" stroke-width="1.5"/>
    <line x1="14" y1="20" x2="32" y2="20" stroke="#38bdf8" stroke-opacity="0.6" stroke-width="1.5"/>
    <circle cx="28" cy="38" r="10" fill="#083344" stroke="#22d3ee" stroke-width="1"/>
    <polygon points="28,32 34,42 22,42" fill="#22d3ee"/>
    <path d="M 40 54 Q 44 58, 48 62 L 40 62 Z" fill="#38bdf8" opacity="0.8"/>
  </g>

  <!-- Clean Category Pill -->
  <g transform="translate(196, 24)">
    <rect x="0" y="0" width="90" height="22" rx="11" fill="#0e282c" stroke="#22d3ee" stroke-opacity="0.6"/>
    <text x="45" y="15" text-anchor="middle" fill="#22d3ee" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" letter-spacing="0.5">MANGA ENGINE</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="24" y="145" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="28" font-weight="800" letter-spacing="-0.5">aether reader</text>
  <text x="24" y="172" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Manga &amp; Manhwa Engine</text>

  <!-- Description -->
  <text x="24" y="210" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="12" font-weight="500">Zero-distraction reading engine.</text>
  <text x="24" y="230" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11.5">Multi-source proxy adapters &amp; telemetry.</text>
  <text x="24" y="250" fill="#64748B" font-family="'Inter', sans-serif" font-size="11">MAL tracking, velocity &amp; offline PWA.</text>

  <!-- Divider Line -->
  <line x1="24" y1="295" x2="286" y2="295" stroke="#FFFFFF" stroke-opacity="0.08"/>

  <!-- Bottom Row -->
  <g transform="translate(24, 325)">
    <circle cx="4" cy="0" r="4" fill="#38bdf8"/>
    <text x="14" y="4" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11">TypeScript</text>
    <text x="262" y="4" text-anchor="end" fill="#22d3ee" font-family="'Inter', sans-serif" font-size="11" font-weight="600">aether-reader ↗</text>
    <path d="M 175 10 Q 218 13, 262 10" stroke="#22d3ee" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  </g>
</svg>'''

    # NAME Sandbox
    sandbox = '''<svg width="310" height="370" viewBox="0 0 310 370" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sbBg" x1="0" y1="0" x2="310" y2="370" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#141a16"/>
      <stop offset="100%" stop-color="#0d130f"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="308" height="368" rx="20" fill="url(#sbBg)" stroke="#1e2c24" stroke-width="1.5"/>

  <!-- 3D Isometric Tiles with Combat d20 -->
  <g transform="translate(24, 24)">
    <polygon points="28,4 52,16 28,28 4,16" fill="#1e4e37" stroke="#34D399" stroke-width="1"/>
    <polygon points="4,16 28,28 28,44 4,32" fill="#0d2c1e"/>
    <polygon points="52,16 28,28 28,44 52,32" fill="#143c2b"/>
    <polygon points="52,16 76,28 52,40 28,28" fill="#133d2a" stroke="#10B981" stroke-opacity="0.5" stroke-width="1"/>
    <g transform="translate(28, 6)">
      <polygon points="0,-14 12,-5 12,9 0,16 -12,9 -12,-5" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
      <text x="0" y="5" text-anchor="middle" fill="#0b2419" font-family="'Inter', sans-serif" font-size="9" font-weight="900">20</text>
    </g>
  </g>

  <!-- Clean Category Pill -->
  <g transform="translate(200, 24)">
    <rect x="0" y="0" width="86" height="22" rx="11" fill="#0e2a1e" stroke="#10B981" stroke-opacity="0.6"/>
    <text x="43" y="15" text-anchor="middle" fill="#34D399" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" letter-spacing="0.5">AST ENGINE</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="24" y="145" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="28" font-weight="800" letter-spacing="-0.5">name sandbox</text>
  <text x="24" y="172" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Board Game Platform</text>

  <!-- Description -->
  <text x="24" y="210" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="12" font-weight="500">Multiplayer tactical board games.</text>
  <text x="24" y="230" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11.5">Natural English-to-AST rule compiler.</text>
  <text x="24" y="250" fill="#64748B" font-family="'Inter', sans-serif" font-size="11">96% pass rate • Colyseus sync.</text>

  <!-- Divider Line -->
  <line x1="24" y1="295" x2="286" y2="295" stroke="#FFFFFF" stroke-opacity="0.08"/>

  <!-- Bottom Row -->
  <g transform="translate(24, 325)">
    <circle cx="4" cy="0" r="4" fill="#38bdf8"/>
    <text x="14" y="4" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11">TypeScript</text>
    <text x="262" y="4" text-anchor="end" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="600">name-sandbox ↗</text>
    <path d="M 175 10 Q 218 13, 262 10" stroke="#34D399" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  </g>
</svg>'''

    # Bounce Celestial
    bounce = '''<svg width="310" height="370" viewBox="0 0 310 370" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bcBg" x1="0" y1="0" x2="310" y2="370" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#14191a"/>
      <stop offset="100%" stop-color="#0c1214"/>
    </linearGradient>
    <linearGradient id="orbGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#312e81"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="308" height="368" rx="20" fill="url(#bcBg)" stroke="#1e2c24" stroke-width="1.5"/>

  <!-- 3D Celestial Sphere / Arcade Planet Logo -->
  <g transform="translate(24, 24)">
    <path d="M 2 56 Q 16 12, 38 18 Q 54 24, 68 56" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>
    <circle cx="38" cy="28" r="18" fill="url(#orbGrad)"/>
    <ellipse cx="32" cy="20" rx="6" ry="3" transform="rotate(-30 32 20)" fill="#ffffff" opacity="0.6"/>
    <ellipse cx="38" cy="30" rx="26" ry="8" transform="rotate(-20 38 30)" stroke="#22d3ee" stroke-width="2" fill="none"/>
  </g>

  <!-- Clean Category Pill -->
  <g transform="translate(196, 24)">
    <rect x="0" y="0" width="90" height="22" rx="11" fill="#0d242c" stroke="#38bdf8" stroke-opacity="0.6"/>
    <text x="45" y="15" text-anchor="middle" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" letter-spacing="0.5">3D PHYSICS</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="24" y="145" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="26" font-weight="800" letter-spacing="-0.5">bounce celestial</text>
  <text x="24" y="172" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12" font-weight="600">3D Arcade Celestial Physics</text>

  <!-- Description -->
  <text x="24" y="210" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="12" font-weight="500">Snappy orbital physics loops.</text>
  <text x="24" y="230" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11.5">Juicy Three.js shaders &amp; mechanics.</text>
  <text x="24" y="250" fill="#64748B" font-family="'Inter', sans-serif" font-size="11">Vite + Playwright + Supabase back.</text>

  <!-- Divider Line -->
  <line x1="24" y1="295" x2="286" y2="295" stroke="#FFFFFF" stroke-opacity="0.08"/>

  <!-- Bottom Row -->
  <g transform="translate(24, 325)">
    <circle cx="4" cy="0" r="4" fill="#38bdf8"/>
    <text x="14" y="4" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11">TypeScript</text>
    <text x="262" y="4" text-anchor="end" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="11" font-weight="600">bounce-celestial ↗</text>
    <path d="M 165 10 Q 213 13, 262 10" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  </g>
</svg>'''

    # Swaram
    swaram = '''<svg width="310" height="370" viewBox="0 0 310 370" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="swBg" x1="0" y1="0" x2="310" y2="370" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#191914"/>
      <stop offset="100%" stop-color="#12120e"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="308" height="368" rx="20" fill="url(#swBg)" stroke="#2c2c1e" stroke-width="1.5"/>

  <!-- 3D Acoustic Waveform & Voice Icon -->
  <g transform="translate(24, 24)">
    <rect x="4" y="24" width="4" height="20" rx="2" fill="#facc15"/>
    <rect x="12" y="14" width="4" height="40" rx="2" fill="#facc15"/>
    <rect x="20" y="8" width="4" height="52" rx="2" fill="#eab308"/>
    <rect x="28" y="18" width="4" height="32" rx="2" fill="#facc15"/>
    <rect x="36" y="2" width="4" height="64" rx="2" fill="#fde047"/>
    <rect x="44" y="14" width="4" height="40" rx="2" fill="#facc15"/>
    <rect x="52" y="22" width="4" height="24" rx="2" fill="#facc15"/>
  </g>

  <!-- Clean Category Pill -->
  <g transform="translate(202, 24)">
    <rect x="0" y="0" width="84" height="22" rx="11" fill="#29260d" stroke="#facc15" stroke-opacity="0.6"/>
    <text x="42" y="15" text-anchor="middle" fill="#facc15" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" letter-spacing="0.5">VOICE PWA</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="24" y="145" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="28" font-weight="800" letter-spacing="-0.5">swaram</text>
  <text x="24" y="172" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Voice Accessibility PWA</text>

  <!-- Description -->
  <text x="24" y="210" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="12" font-weight="500">Voice-first accessible form engine.</text>
  <text x="24" y="230" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11.5">Acoustic loops for low-vision users.</text>
  <text x="24" y="250" fill="#64748B" font-family="'Inter', sans-serif" font-size="11">Speech-to-intent field navigation.</text>

  <!-- Divider Line -->
  <line x1="24" y1="295" x2="286" y2="295" stroke="#FFFFFF" stroke-opacity="0.08"/>

  <!-- Bottom Row -->
  <g transform="translate(24, 325)">
    <circle cx="4" cy="0" r="4" fill="#facc15"/>
    <text x="14" y="4" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11">JavaScript</text>
    <text x="262" y="4" text-anchor="end" fill="#facc15" font-family="'Inter', sans-serif" font-size="11" font-weight="600">swaram-three ↗</text>
    <path d="M 175 10 Q 218 13, 262 10" stroke="#facc15" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  </g>
</svg>'''

    with open('assets/cards/skloop.svg', 'w') as f:
        f.write(skloop)
    with open('assets/cards/personal_reader.svg', 'w') as f:
        f.write(aether)
    with open('assets/cards/name_sandbox.svg', 'w') as f:
        f.write(sandbox)
    with open('assets/cards/bounce_celestial.svg', 'w') as f:
        f.write(bounce)
    with open('assets/cards/swaram.svg', 'w') as f:
        f.write(swaram)

    # -------------------------------------------------------------
    # 4. COMMUNITY ROLES VISUAL CARDS (CSI, µLearn, IEEE)
    # -------------------------------------------------------------
    try:
        from scripts.generate_roles import generate_community_roles_svg
        generate_community_roles_svg()
    except Exception as e:
        print(f"Error generating community roles: {e}")

    # -------------------------------------------------------------
    # 5. GAMIFIED ARCADE TELEMETRY STATION (Live Real-Time Metrics)
    # -------------------------------------------------------------
    try:
        from scripts.update_telemetry import update_hud
        update_hud()
    except Exception as e:
        print(f"Error calling live update_hud: {e}")

    # -------------------------------------------------------------
    # 6. BESPOKE SLIME ARCADE FOOTER (Crisp, zero generic vercel bloat)
    # -------------------------------------------------------------
    footer_svg = '''<svg width="900" height="130" viewBox="0 0 900 130" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ftGrad" x1="0" y1="0" x2="900" y2="130" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0a120e"/>
      <stop offset="50%" stop-color="#12251a"/>
      <stop offset="100%" stop-color="#07110c"/>
    </linearGradient>
    <linearGradient id="slimeWave" x1="0" y1="0" x2="900" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.2"/>
      <stop offset="50%" stop-color="#34D399" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.2"/>
    </linearGradient>
  </defs>

  <rect width="900" height="130" rx="16" fill="url(#ftGrad)" stroke="#1e382b" stroke-width="1.2"/>

  <!-- Slime Cyber Grid Horizon Lines -->
  <line x1="50" y1="110" x2="850" y2="110" stroke="#10B981" stroke-opacity="0.15" stroke-width="1"/>
  <line x1="100" y1="95" x2="800" y2="95" stroke="#10B981" stroke-opacity="0.1" stroke-width="1"/>
  <line x1="180" y1="82" x2="720" y2="82" stroke="#10B981" stroke-opacity="0.08" stroke-width="1"/>

  <!-- Glowing Slime Wave Curve -->
  <path d="M 50 45 Q 220 20, 450 40 T 850 35" stroke="url(#slimeWave)" stroke-width="3" fill="none"/>
  <path d="M 50 45 Q 220 20, 450 40 T 850 35 L 850 45 L 50 45 Z" fill="#10B981" fill-opacity="0.05"/>

  <!-- Main Motto -->
  <text x="450" y="58" text-anchor="middle" fill="#F8FAFC" font-family="'Inter', -apple-system, sans-serif" font-size="18" font-weight="900" letter-spacing="3">ABSORB • ADAPT • ARCHITECT</text>
  <text x="450" y="82" text-anchor="middle" fill="#34D399" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600" letter-spacing="0.5">Code is malleable. Systems architecture is permanent.</text>
  <text x="450" y="104" text-anchor="middle" fill="#64748B" font-family="'Inter', sans-serif" font-size="10" font-weight="500">Tejas K M (tejaskm-dev) • ASIET CSE • Class of 2029</text>
</svg>'''

    with open('assets/footer.svg', 'w') as f:
        f.write(footer_svg)

    print("Successfully generated all assets without blinking dots or pulses!")

if __name__ == '__main__':
    generate_all_assets()
