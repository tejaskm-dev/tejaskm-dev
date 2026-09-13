import os
from PIL import Image, ImageDraw, ImageFont

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

def create_ascii_portrait():
    if not os.path.exists('picture.txt'):
        return

    with open('picture.txt') as f:
        lines = [l.rstrip('\n\r') for l in f.readlines()]

    font_path = '/System/Library/Fonts/Menlo.ttc'
    if not os.path.exists(font_path):
        font_path = '/System/Library/Fonts/Monaco.dfont'
    if not os.path.exists(font_path):
        font_path = '/System/Library/Fonts/Courier.dfont'

    font_size = 11
    font = ImageFont.truetype(font_path, font_size)

    char_w = font.getlength('M')
    line_h = 12.2

    content_w = int(180 * char_w)
    content_h = int(len(lines) * line_h)

    pad_x = 24
    pad_top = 44
    pad_bot = 20

    total_w = content_w + pad_x * 2
    total_h = content_h + pad_top + pad_bot

    img = Image.new('RGBA', (total_w, total_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, total_w - 1, total_h - 1], radius=14, fill='#07120e', outline='#10B981', width=2)
    draw.rounded_rectangle([0, 0, total_w - 1, 38], radius=14, fill='#0d261b', outline='#10B981', width=2)
    draw.rectangle([0, 24, total_w - 1, 38], fill='#0d261b')
    draw.line([(0, 38), (total_w - 1, 38)], fill='#10B981', width=1)

    draw.ellipse([18, 13, 28, 23], fill='#ef4444')
    draw.ellipse([34, 13, 44, 23], fill='#eab308')
    draw.ellipse([50, 13, 60, 23], fill='#22c55e')

    title_font = ImageFont.truetype(font_path, 11)
    draw.text((76, 12), 'tejaskm-dev ~ cat picture.txt', font=title_font, fill='#94A3B8')

    matrix_text = '180 x 101 MATRIX'
    m_len = title_font.getlength(matrix_text)
    draw.rounded_rectangle([total_w - m_len - 36, 9, total_w - 18, 29], radius=4, fill='#05150e', outline='#10B981', width=1)
    draw.text((total_w - m_len - 27, 12), matrix_text, font=title_font, fill='#34D399')

    for i, l in enumerate(lines):
        y = int(pad_top + i * line_h)
        draw.text((pad_x, y), l, font=font, fill='#22c55e')

    img.save('assets/ascii_portrait.png', 'PNG')
    print('Generated assets/ascii_portrait.png')

if __name__ == '__main__':
    create_proper_cards()
    create_ascii_portrait()
