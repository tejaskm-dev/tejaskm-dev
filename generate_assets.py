import os

def create_proper_cards():
    os.makedirs('assets/cards', exist_ok=True)

    cards = [
        {
            'filename': 'skloop',
            'repo': 'skloop',
            'title': 'Gamified EdTech Platform',
            'badge': 'ACTIVE BUILD',
            'd1': 'Interactive narrative coding worlds featuring the Loopy AI companion,',
            'd2': 'Monaco Editor integration, quest progression trees, and item shop.',
            'lang': 'TypeScript',
            'lang_color': '#3178C6',
            'live': 'skloop.online'
        },
        {
            'filename': 'personal_reader',
            'repo': 'personal_reader',
            'title': 'Aether Reader PWA',
            'badge': 'MANGA PWA',
            'd1': 'Full-stack manga and manhwa reader PWA with multi-source proxy scrapers,',
            'd2': 'MAL-style reading tracking, velocity analytics, and offline caching.',
            'lang': 'TypeScript',
            'lang_color': '#3178C6',
            'live': 'aether-reader.vercel.app'
        },
        {
            'filename': 'name_sandbox',
            'repo': 'NAME-sandbox',
            'title': 'Multiplayer Board Game Platform',
            'badge': 'AST ENGINE',
            'd1': 'Tile-based multiplayer creation engine with real-time Colyseus WebSockets,',
            'd2': 'custom natural English-to-AST parser (96% pass rate across 386 tests).',
            'lang': 'TypeScript',
            'lang_color': '#3178C6',
            'live': 'name-sandbox.vercel.app'
        },
        {
            'filename': 'bounce_celestial',
            'repo': 'bounce_celestial',
            'title': 'Bounce Arcade 3D',
            'badge': 'THREE.JS GAME',
            'd1': '3D arcade celestial physics game built with Three.js, TypeScript, and Vite,',
            'd2': 'featuring custom shaders, snappy physics loops, and Supabase backend.',
            'lang': 'TypeScript',
            'lang_color': '#3178C6',
            'live': 'bounce-celestial.vercel.app'
        },
        {
            'filename': 'swaram',
            'repo': 'swaram',
            'title': 'Swaram Accessibility PWA',
            'badge': 'VOICE PWA',
            'd1': 'Voice-first accessible form-filling PWA designed for blind and low-vision',
            'd2': 'users with real-time acoustic feedback and speech recognition.',
            'lang': 'JavaScript',
            'lang_color': '#F7DF1E',
            'live': 'swaram-three.vercel.app'
        }
    ]

    for c in cards:
        svg = f'''<svg width="440" height="165" viewBox="0 0 440 165" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg_{c['filename']}" x1="0" y1="0" x2="440" y2="165" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0c1410"/>
      <stop offset="100%" stop-color="#070d0a"/>
    </linearGradient>
    <linearGradient id="cardBorder_{c['filename']}" x1="0" y1="0" x2="440" y2="165" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#34D399" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.5"/>
    </linearGradient>
  </defs>

  <!-- Card Frame -->
  <rect x="1" y="1" width="438" height="163" rx="10" fill="url(#cardBg_{c['filename']})" stroke="url(#cardBorder_{c['filename']})" stroke-width="1.5"/>

  <!-- Top Row: Repo Title -->
  <g transform="translate(18, 18)">
    <path d="M2 4C2 2.89543 2.89543 2 4 2H8.58579C9.11622 2 9.62493 2.21071 10 2.58579L12.4142 5H20C21.1046 5 22 5.89543 22 7V16C22 17.1046 21.1046 18 20 18H4C2.89543 18 2 17.1046 2 16V4Z" fill="#10B981" fill-opacity="0.2" stroke="#10B981" stroke-width="1.5" stroke-linejoin="round"/>
    <text x="30" y="15" fill="#FFFFFF" font-family="'Inter', -apple-system, sans-serif" font-size="15" font-weight="700">{c['repo']}</text>
  </g>

  <!-- Top Row: Badge -->
  <g transform="translate(422, 18)">
    <rect x="-114" y="0" width="114" height="20" rx="10" fill="#0c261b" stroke="#10B981" stroke-opacity="0.4"/>
    <text x="-57" y="14" text-anchor="middle" fill="#34D399" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" letter-spacing="0.5">{c['badge']}</text>
  </g>

  <!-- Project Title & Description -->
  <text x="18" y="66" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="12" font-weight="600">{c['title']}</text>
  <text x="18" y="86" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11">{c['d1']}</text>
  <text x="18" y="104" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11">{c['d2']}</text>

  <!-- Divider Line -->
  <line x1="18" y1="122" x2="422" y2="122" stroke="#10B981" stroke-opacity="0.15" stroke-width="1"/>

  <!-- Bottom Row: Tech + Live URL -->
  <g transform="translate(18, 142)">
    <circle cx="5" cy="0" r="4" fill="{c['lang_color']}"/>
    <text x="15" y="4" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="11">{c['lang']}</text>

    <text x="404" y="4" text-anchor="end" fill="#10B981" font-family="'Inter', sans-serif" font-size="11" font-weight="600">{c['live']} ↗</text>
  </g>
</svg>'''
        with open(f"assets/cards/{c['filename']}.svg", 'w') as f:
            f.write(svg)
        print(f"Generated assets/cards/{c['filename']}.svg")

if __name__ == '__main__':
    create_proper_cards()
