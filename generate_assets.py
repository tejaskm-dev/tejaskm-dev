import os

def create_svg_hud():
    svg = '''<svg width="900" height="190" viewBox="0 0 900 190" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hudBg" x1="0" y1="0" x2="900" y2="190" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#050e0a"/>
      <stop offset="50%" stop-color="#091812"/>
      <stop offset="100%" stop-color="#040b08"/>
    </linearGradient>
    <linearGradient id="hudBorder" x1="0" y1="0" x2="900" y2="190" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#00F5D4" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="scanline" x1="0" y1="0" x2="0" y2="190" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00FF66" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      @keyframes pulseDot {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.3; transform: scale(0.8); }
      }
      @keyframes sweep {
        0% { transform: translateY(-190px); }
        100% { transform: translateY(190px); }
      }
      .pulsing-dot { animation: pulseDot 2s infinite ease-in-out; transform-origin: 28px 28px; }
      .sweep-line { animation: sweep 4s infinite linear; }
    </style>
  </defs>

  <!-- Background Card -->
  <rect x="1" y="1" width="898" height="188" rx="12" fill="url(#hudBg)" stroke="url(#hudBorder)" stroke-width="1.5"/>

  <!-- Subtle Scanline -->
  <g clip-path="url(#cardClip)">
    <rect class="sweep-line" x="1" y="1" width="898" height="60" fill="url(#scanline)"/>
  </g>

  <!-- Header Strip -->
  <path d="M 1 12 C 1 5.925 5.925 1 12 1 L 888 1 C 894.075 1 899 5.925 899 12 L 899 40 L 1 40 Z" fill="#0c2217" fill-opacity="0.6"/>
  <line x1="1" y1="40" x2="899" y2="40" stroke="#00FF66" stroke-opacity="0.25" stroke-width="1"/>

  <!-- Pulse Status Indicator -->
  <circle class="pulsing-dot" cx="28" cy="21" r="5" fill="#00FF66" filter="url(#glow)"/>
  <circle cx="28" cy="21" r="9" stroke="#00FF66" stroke-opacity="0.4" stroke-width="1"/>
  <text x="46" y="25" fill="#00FF66" font-family="'Fira Code', monospace" font-size="12" font-weight="700" letter-spacing="1.5">SLIME TELEMETRY // SHINZ-OS v2.6</text>
  
  <rect x="730" y="12" width="150" height="20" rx="4" fill="#04140c" stroke="#00FF66" stroke-opacity="0.4"/>
  <text x="805" y="26" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="1">STATE: TRANSLUCENT</text>

  <!-- Grid Items -->
  <!-- Col 1 -->
  <g transform="translate(30, 60)">
    <text x="0" y="0" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="1">[ IDENTITY ]</text>
    <text x="0" y="20" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="15" font-weight="700">Tejas K M ("Shinz")</text>
    <text x="0" y="38" fill="#8899A6" font-family="'Inter', sans-serif" font-size="12">Directing AI · Systems Architect</text>

    <text x="0" y="70" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="1">[ HABITAT &amp; BATCH ]</text>
    <text x="0" y="90" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600">ASIET CSE '29 · Kerala, India</text>
    <text x="0" y="108" fill="#00FF66" font-family="'Inter', sans-serif" font-size="12" font-weight="500">Batch Class Representative</text>
  </g>

  <!-- Divider Line 1 -->
  <line x1="280" y1="55" x2="280" y2="175" stroke="#00FF66" stroke-opacity="0.15" stroke-width="1" stroke-dasharray="4 4"/>

  <!-- Col 2 -->
  <g transform="translate(310, 60)">
    <text x="0" y="0" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="1">[ LEVERAGE VECTOR ]</text>
    <text x="0" y="20" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="600">AI-Directed Engineering</text>
    <text x="0" y="38" fill="#8899A6" font-family="'Inter', sans-serif" font-size="12">Claude Code · Antigravity · Groq / Llama</text>

    <text x="0" y="70" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="1">[ CORE SPECIALTY ]</text>
    <text x="0" y="90" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600">AST Engines · State Sync · PWAs</text>
    <text x="0" y="108" fill="#8899A6" font-family="'Inter', sans-serif" font-size="12">Code-literate debugging &amp; architecture</text>
  </g>

  <!-- Divider Line 2 -->
  <line x1="590" y1="55" x2="590" y2="175" stroke="#00FF66" stroke-opacity="0.15" stroke-width="1" stroke-dasharray="4 4"/>

  <!-- Col 3 -->
  <g transform="translate(620, 60)">
    <text x="0" y="0" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="1">[ NORTH STAR ]</text>
    <text x="0" y="20" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Technical Product Leadership</text>
    <text x="0" y="38" fill="#8899A6" font-family="'Inter', sans-serif" font-size="12">End-to-End Ownership &amp; Ventures</text>

    <text x="0" y="70" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="1">[ FLUIDITY INDEX ]</text>
    <!-- Progress Bar -->
    <rect x="0" y="80" width="240" height="12" rx="6" fill="#071810" stroke="#00FF66" stroke-opacity="0.3"/>
    <rect x="2" y="82" width="210" height="8" rx="4" fill="#00FF66" filter="url(#glow)"/>
    <text x="0" y="110" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">Absorbing Complexity // Rapid</text>
  </g>

  <!-- Corner Accents -->
  <path d="M 8 18 L 8 8 L 18 8" stroke="#00FF66" stroke-width="2" fill="none"/>
  <path d="M 892 18 L 892 8 L 882 8" stroke="#00FF66" stroke-width="2" fill="none"/>
  <path d="M 8 172 L 8 182 L 18 182" stroke="#00FF66" stroke-width="2" fill="none"/>
  <path d="M 892 172 L 892 182 L 882 182" stroke="#00FF66" stroke-width="2" fill="none"/>
</svg>'''
    with open('assets/slime-hud.svg', 'w') as f:
        f.write(svg)
    print("Created assets/slime-hud.svg")

def create_card_skloop():
    svg = '''<svg width="900" height="270" viewBox="0 0 900 270" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg1" x1="0" y1="0" x2="900" y2="270" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#06120d"/>
      <stop offset="60%" stop-color="#091b13"/>
      <stop offset="100%" stop-color="#040e09"/>
    </linearGradient>
    <linearGradient id="cardBorder1" x1="0" y1="0" x2="900" y2="270" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#00F5D4" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.8"/>
    </linearGradient>
    <filter id="glow1" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      @keyframes floatRing {
        0%, 100% { transform: rotate(0deg); }
        50% { transform: rotate(180deg); }
      }
      @keyframes pulseCore {
        0%, 100% { r: 24px; opacity: 0.8; }
        50% { r: 30px; opacity: 1; }
      }
      .ring-anim { transform-origin: 770px 135px; animation: floatRing 12s infinite linear; }
      .core-anim { animation: pulseCore 3s infinite ease-in-out; }
    </style>
  </defs>

  <rect x="1" y="1" width="898" height="268" rx="14" fill="url(#cardBg1)" stroke="url(#cardBorder1)" stroke-width="1.5"/>

  <!-- Top Bar / Index & Status -->
  <g transform="translate(30, 24)">
    <rect x="0" y="0" width="76" height="22" rx="4" fill="#041f12" stroke="#00FF66" stroke-opacity="0.6"/>
    <text x="38" y="15" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11" font-weight="700" letter-spacing="1">SYS::01</text>
    
    <rect x="88" y="0" width="180" height="22" rx="4" fill="#041f12" stroke="#00F5D4" stroke-opacity="0.5"/>
    <text x="178" y="15" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="0.5">IN ACTIVE DEVELOPMENT</text>
  </g>

  <!-- Project Title & Subtitle -->
  <text x="30" y="80" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="26" font-weight="800" letter-spacing="-0.5">Skloop</text>
  <text x="135" y="78" fill="#00FF66" font-family="'Fira Code', monospace" font-size="13" font-weight="600">// Gamified EdTech Platform</text>
  <text x="30" y="102" fill="#8899A6" font-family="'Inter', sans-serif" font-size="13">Architecting immersive narrative coding worlds with live execution and adaptive guidance.</text>

  <!-- Feature Points -->
  <g transform="translate(30, 130)">
    <text x="0" y="0" fill="#00FF66" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="0" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Loopverse &amp; Underlayer:</text>
    <text x="200" y="0" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Dual narrative worlds structuring curriculum &amp; hidden hacker puzzles</text>

    <text x="0" y="24" fill="#00FF66" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="24" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Loopy AI Companion:</text>
    <text x="180" y="24" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Dual-personality AI mentor dynamically balancing support &amp; challenge</text>

    <text x="0" y="48" fill="#00FF66" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="48" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Progression &amp; Monaco:</text>
    <text x="195" y="48" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">In-browser editor, XP economy, quest branches, and virtual gear shop</text>
  </g>

  <!-- Bottom Tech Stack Pills -->
  <g transform="translate(30, 218)">
    <rect x="0" y="0" width="70" height="24" rx="12" fill="#0c2518" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="35" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">Next.js</text>

    <rect x="78" y="0" width="94" height="24" rx="12" fill="#0c2518" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="125" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">TypeScript</text>

    <rect x="180" y="0" width="70" height="24" rx="12" fill="#0c2518" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="215" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">Monaco</text>

    <rect x="258" y="0" width="84" height="24" rx="12" fill="#0c2518" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="300" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">AI Agents</text>

    <rect x="350" y="0" width="80" height="24" rx="12" fill="#0c2518" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="390" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">Supabase</text>
  </g>

  <!-- Right Visual: Neon Loop Slime Node -->
  <g transform="translate(770, 135)">
    <circle class="ring-anim" cx="0" cy="0" r="60" stroke="#00FF66" stroke-opacity="0.2" stroke-width="1.5" stroke-dasharray="8 6"/>
    <circle class="ring-anim" cx="0" cy="0" r="42" stroke="#00F5D4" stroke-opacity="0.4" stroke-width="2" stroke-dasharray="16 10"/>
    <circle class="core-anim" cx="0" cy="0" r="24" fill="#00FF66" fill-opacity="0.2" filter="url(#glow1)"/>
    <circle cx="0" cy="0" r="14" fill="#00FF66" filter="url(#glow1)"/>
    <!-- Orbiting nodes -->
    <circle cx="42" cy="0" r="4" fill="#00F5D4"/>
    <circle cx="-42" cy="0" r="4" fill="#00FF66"/>
  </g>

  <!-- Role Stamp -->
  <text x="640" y="235" text-anchor="end" fill="#8899A6" font-family="'Fira Code', monospace" font-size="11">ROLE: ARCHITECTURE &amp; UI</text>
  <text x="655" y="235" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">-&gt;</text>
</svg>'''
    with open('assets/cards/skloop.svg', 'w') as f:
        f.write(svg)
    print("Created assets/cards/skloop.svg")

def create_card_aether():
    svg = '''<svg width="900" height="270" viewBox="0 0 900 270" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg2" x1="0" y1="0" x2="900" y2="270" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#051012"/>
      <stop offset="60%" stop-color="#08181c"/>
      <stop offset="100%" stop-color="#040e10"/>
    </linearGradient>
    <linearGradient id="cardBorder2" x1="0" y1="0" x2="900" y2="270" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00F5D4" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#00FF66" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.8"/>
    </linearGradient>
    <filter id="glow2" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect x="1" y="1" width="898" height="268" rx="14" fill="url(#cardBg2)" stroke="url(#cardBorder2)" stroke-width="1.5"/>

  <!-- Top Bar -->
  <g transform="translate(30, 24)">
    <rect x="0" y="0" width="76" height="22" rx="4" fill="#041f22" stroke="#00F5D4" stroke-opacity="0.6"/>
    <text x="38" y="15" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="11" font-weight="700" letter-spacing="1">SYS::02</text>
    
    <rect x="88" y="0" width="220" height="22" rx="4" fill="#041f22" stroke="#00FF66" stroke-opacity="0.5"/>
    <text x="198" y="15" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="0.5">SHIPPED // PRIVATE ARCHITECTURE</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="30" y="80" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="26" font-weight="800" letter-spacing="-0.5">Aether Reader</text>
  <text x="210" y="78" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="13" font-weight="600">// Full-Stack Manga &amp; Manhwa PWA</text>
  <text x="30" y="102" fill="#8899A6" font-family="'Inter', sans-serif" font-size="13">High-speed distraction-free reader engine aggregating multi-scanlation feeds with telemetry.</text>

  <!-- Feature Points -->
  <g transform="translate(30, 130)">
    <text x="0" y="0" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="0" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Source-Adapter Pattern:</text>
    <text x="210" y="0" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Decoupled Express scrapers abstracting multiple upstream scanlation sources</text>

    <text x="0" y="24" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="24" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">MAL-Style Tracking:</text>
    <text x="180" y="24" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Chapter bookmarking, reading velocity telemetry &amp; full analytics dashboard</text>

    <text x="0" y="48" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="48" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Offline Resilience:</text>
    <text x="175" y="48" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">PWA Service Worker caching + client-side IndexedDB with Supabase cloud sync</text>
  </g>

  <!-- Bottom Tech Stack Pills -->
  <g transform="translate(30, 218)">
    <rect x="0" y="0" width="86" height="24" rx="12" fill="#072328" stroke="#00F5D4" stroke-opacity="0.3"/>
    <text x="43" y="16" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="11">Next.js 15</text>

    <rect x="94" y="0" width="94" height="24" rx="12" fill="#072328" stroke="#00F5D4" stroke-opacity="0.3"/>
    <text x="141" y="16" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="11">TypeScript</text>

    <rect x="196" y="0" width="76" height="24" rx="12" fill="#072328" stroke="#00F5D4" stroke-opacity="0.3"/>
    <text x="234" y="16" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="11">Tailwind</text>

    <rect x="280" y="0" width="76" height="24" rx="12" fill="#072328" stroke="#00F5D4" stroke-opacity="0.3"/>
    <text x="318" y="16" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="11">Express</text>

    <rect x="364" y="0" width="80" height="24" rx="12" fill="#072328" stroke="#00F5D4" stroke-opacity="0.3"/>
    <text x="404" y="16" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="11">Supabase</text>
  </g>

  <!-- Right Visual: Layered Book/Reader Wireframe -->
  <g transform="translate(730, 85)">
    <rect x="0" y="0" width="100" height="120" rx="8" fill="#072328" stroke="#00F5D4" stroke-opacity="0.4" stroke-width="1.5"/>
    <rect x="15" y="-12" width="100" height="120" rx="8" fill="#0a3239" stroke="#00FF66" stroke-opacity="0.6" stroke-width="1.5"/>
    <line x1="30" y1="15" x2="95" y2="15" stroke="#00FF66" stroke-opacity="0.8" stroke-width="2"/>
    <line x1="30" y1="30" x2="80" y2="30" stroke="#00F5D4" stroke-opacity="0.5" stroke-width="1.5"/>
    <line x1="30" y1="45" x2="90" y2="45" stroke="#00F5D4" stroke-opacity="0.5" stroke-width="1.5"/>
    <line x1="30" y1="60" x2="70" y2="60" stroke="#00F5D4" stroke-opacity="0.5" stroke-width="1.5"/>
    <circle cx="85" cy="85" r="14" fill="#00FF66" fill-opacity="0.2" filter="url(#glow2)"/>
    <circle cx="85" cy="85" r="7" fill="#00F5D4"/>
  </g>

  <!-- Role Stamp -->
  <text x="640" y="235" text-anchor="end" fill="#8899A6" font-family="'Fira Code', monospace" font-size="11">ROLE: CREATOR &amp; ARCHITECT</text>
  <text x="655" y="235" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="11">-&gt;</text>
</svg>'''
    with open('assets/cards/aether.svg', 'w') as f:
        f.write(svg)
    print("Created assets/cards/aether.svg")

def create_card_name_sandbox():
    svg = '''<svg width="900" height="270" viewBox="0 0 900 270" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg3" x1="0" y1="0" x2="900" y2="270" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#06120e"/>
      <stop offset="60%" stop-color="#0b1a13"/>
      <stop offset="100%" stop-color="#050e09"/>
    </linearGradient>
    <linearGradient id="cardBorder3" x1="0" y1="0" x2="900" y2="270" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0.8"/>
    </linearGradient>
    <filter id="glow3" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect x="1" y="1" width="898" height="268" rx="14" fill="url(#cardBg3)" stroke="url(#cardBorder3)" stroke-width="1.5"/>

  <!-- Top Bar -->
  <g transform="translate(30, 24)">
    <rect x="0" y="0" width="76" height="22" rx="4" fill="#042013" stroke="#00FF66" stroke-opacity="0.6"/>
    <text x="38" y="15" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11" font-weight="700" letter-spacing="1">SYS::03</text>
    
    <rect x="88" y="0" width="220" height="22" rx="4" fill="#042013" stroke="#00FF66" stroke-opacity="0.5"/>
    <text x="198" y="15" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="0.5">96% PARSER PASS RATE // 386 TESTS</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="30" y="80" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="26" font-weight="800" letter-spacing="-0.5">NAME Sandbox</text>
  <text x="220" y="78" fill="#00FF66" font-family="'Fira Code', monospace" font-size="13" font-weight="600">// Multiplayer Board Game Engine &amp; AST</text>
  <text x="30" y="102" fill="#8899A6" font-family="'Inter', sans-serif" font-size="13">Tile-based multiplayer creation sandbox with a custom natural language rule compiler.</text>

  <!-- Feature Points -->
  <g transform="translate(30, 130)">
    <text x="0" y="0" fill="#00FF66" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="0" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">English-to-AST Compiler:</text>
    <text x="200" y="0" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Compiles natural text into deterministic action trees with 386 test cases</text>

    <text x="0" y="24" fill="#00FF66" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="24" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Hybrid Combat System:</text>
    <text x="190" y="24" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Deep battle loops merging Pokémon elemental matchups with D&amp;D d20 economy</text>

    <text x="0" y="48" fill="#00FF66" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="48" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Realtime State Sync:</text>
    <text x="180" y="48" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Authoritative server rooms powered by Colyseus WebSocket state synchronization</text>
  </g>

  <!-- Bottom Tech Stack Pills -->
  <g transform="translate(30, 218)">
    <rect x="0" y="0" width="80" height="24" rx="12" fill="#082517" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="40" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">Colyseus</text>

    <rect x="88" y="0" width="70" height="24" rx="12" fill="#082517" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="123" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">Next.js</text>

    <rect x="166" y="0" width="94" height="24" rx="12" fill="#082517" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="213" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">AST Parser</text>

    <rect x="268" y="0" width="80" height="24" rx="12" fill="#082517" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="308" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">Supabase</text>

    <rect x="356" y="0" width="94" height="24" rx="12" fill="#082517" stroke="#00FF66" stroke-opacity="0.3"/>
    <text x="403" y="16" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">TypeScript</text>
  </g>

  <!-- Right Visual: Isometric Tile Board Grid -->
  <g transform="translate(730, 100)">
    <!-- Hex / Diamond Tiles -->
    <polygon points="50,0 90,20 50,40 10,20" fill="#0b2c1c" stroke="#00FF66" stroke-width="1.5"/>
    <polygon points="10,20 50,40 50,65 10,45" fill="#061d12" stroke="#00FF66" stroke-width="1"/>
    <polygon points="90,20 50,40 50,65 90,45" fill="#082216" stroke="#00FF66" stroke-width="1"/>
    
    <polygon points="90,20 130,40 90,60 50,40" fill="#0e3a24" stroke="#00F5D4" stroke-width="1.5"/>
    <polygon points="10,60 50,80 10,100 -30,80" fill="#092417" stroke="#00FF66" stroke-opacity="0.4" stroke-width="1"/>

    <!-- Glowing Node on Top -->
    <circle cx="50" cy="15" r="6" fill="#00FF66" filter="url(#glow3)"/>
    <circle cx="90" cy="35" r="4" fill="#00F5D4"/>
  </g>

  <!-- Role Stamp -->
  <text x="640" y="235" text-anchor="end" fill="#8899A6" font-family="'Fira Code', monospace" font-size="11">ROLE: ENGINE &amp; AST COMPILER</text>
  <text x="655" y="235" fill="#00FF66" font-family="'Fira Code', monospace" font-size="11">-&gt;</text>
</svg>'''
    with open('assets/cards/name-sandbox.svg', 'w') as f:
        f.write(svg)
    print("Created assets/cards/name-sandbox.svg")

def create_card_academic_engine():
    svg = '''<svg width="900" height="270" viewBox="0 0 900 270" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg4" x1="0" y1="0" x2="900" y2="270" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#050e0d"/>
      <stop offset="60%" stop-color="#091614"/>
      <stop offset="100%" stop-color="#040908"/>
    </linearGradient>
    <linearGradient id="cardBorder4" x1="0" y1="0" x2="900" y2="270" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#00FF66" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.8"/>
    </linearGradient>
    <filter id="glow4" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect x="1" y="1" width="898" height="268" rx="14" fill="url(#cardBg4)" stroke="url(#cardBorder4)" stroke-width="1.5"/>

  <!-- Top Bar -->
  <g transform="translate(30, 24)">
    <rect x="0" y="0" width="76" height="22" rx="4" fill="#041a15" stroke="#10B981" stroke-opacity="0.6"/>
    <text x="38" y="15" text-anchor="middle" fill="#10B981" font-family="'Fira Code', monospace" font-size="11" font-weight="700" letter-spacing="1">SYS::04</text>
    
    <rect x="88" y="0" width="220" height="22" rx="4" fill="#041a15" stroke="#00FF66" stroke-opacity="0.5"/>
    <text x="198" y="15" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10" font-weight="600" letter-spacing="0.5">KTU OOP COURSE // 4-PERSON TEAM</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="30" y="80" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="26" font-weight="800" letter-spacing="-0.5">Academic Integrity Engine</text>
  <text x="360" y="78" fill="#10B981" font-family="'Fira Code', monospace" font-size="13" font-weight="600">// Pluggable Plagiarism &amp; AI Authorship</text>
  <text x="30" y="102" fill="#8899A6" font-family="'Inter', sans-serif" font-size="13">High-throughput detection microservice analyzing code structure, syntax fingerprints, and AI patterns.</text>

  <!-- Feature Points -->
  <g transform="translate(30, 130)">
    <text x="0" y="0" fill="#10B981" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="0" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Multi-Language Tokenizer:</text>
    <text x="215" y="0" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Structural AST tokenization supporting Java, C, C++, Python, and JavaScript</text>

    <text x="0" y="24" fill="#10B981" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="24" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Winnowing &amp; AI Heuristics:</text>
    <text x="215" y="24" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">K-gram fingerprinting coupled with algorithmic AI authorship stylometry</text>

    <text x="0" y="48" fill="#10B981" font-family="'Fira Code', monospace" font-size="13" font-weight="700">&gt;&gt;</text>
    <text x="24" y="48" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13" font-weight="600">REST Microservice Core:</text>
    <text x="195" y="48" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Javalin embedded HTTP runtime with SQLite persistent fingerprint registry</text>
  </g>

  <!-- Bottom Tech Stack Pills -->
  <g transform="translate(30, 218)">
    <rect x="0" y="0" width="86" height="24" rx="12" fill="#06221a" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="43" y="16" text-anchor="middle" fill="#10B981" font-family="'Fira Code', monospace" font-size="11">Java Core</text>

    <rect x="94" y="0" width="76" height="24" rx="12" fill="#06221a" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="132" y="16" text-anchor="middle" fill="#10B981" font-family="'Fira Code', monospace" font-size="11">Javalin</text>

    <rect x="178" y="0" width="70" height="24" rx="12" fill="#06221a" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="213" y="16" text-anchor="middle" fill="#10B981" font-family="'Fira Code', monospace" font-size="11">SQLite</text>

    <rect x="256" y="0" width="100" height="24" rx="12" fill="#06221a" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="306" y="16" text-anchor="middle" fill="#10B981" font-family="'Fira Code', monospace" font-size="11">AST Winnow</text>

    <rect x="364" y="0" width="80" height="24" rx="12" fill="#06221a" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="404" y="16" text-anchor="middle" fill="#10B981" font-family="'Fira Code', monospace" font-size="11">REST API</text>
  </g>

  <!-- Right Visual: Fingerprint Matrix & Binary Scan -->
  <g transform="translate(735, 90)">
    <rect x="0" y="0" width="90" height="110" rx="6" fill="#051c15" stroke="#10B981" stroke-opacity="0.5"/>
    <text x="12" y="25" fill="#10B981" font-family="'Fira Code', monospace" font-size="9">&gt; HASH_WINNOW</text>
    <line x1="10" y1="35" x2="80" y2="35" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="12" y="52" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10">8F 3A C9 12</text>
    <text x="12" y="68" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10">44 E1 0B 78</text>
    <text x="12" y="84" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10">99 D2 FF 40</text>
    <circle cx="75" cy="95" r="4" fill="#10B981" filter="url(#glow4)"/>
  </g>

  <!-- Role Stamp -->
  <text x="640" y="235" text-anchor="end" fill="#8899A6" font-family="'Fira Code', monospace" font-size="11">ROLE: DETECTION &amp; REST ARCHITECT</text>
  <text x="655" y="235" fill="#10B981" font-family="'Fira Code', monospace" font-size="11">-&gt;</text>
</svg>'''
    with open('assets/cards/academic-engine.svg', 'w') as f:
        f.write(svg)
    print("Created assets/cards/academic-engine.svg")

def create_card_side_quests():
    svg = '''<svg width="900" height="180" viewBox="0 0 900 180" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sqBg" x1="0" y1="0" x2="900" y2="180" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#050e0b"/>
      <stop offset="50%" stop-color="#081813"/>
      <stop offset="100%" stop-color="#040b08"/>
    </linearGradient>
    <linearGradient id="sqBorder" x1="0" y1="0" x2="900" y2="180" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#00F5D4" stop-opacity="0.3"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="898" height="178" rx="12" fill="url(#sqBg)" stroke="url(#sqBorder)" stroke-width="1.5"/>

  <!-- Left Side Quest: Swaram -->
  <g transform="translate(30, 24)">
    <rect x="0" y="0" width="60" height="20" rx="4" fill="#041b12" stroke="#00FF66" stroke-opacity="0.5"/>
    <text x="30" y="14" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10" font-weight="700">QUEST 01</text>
    
    <text x="75" y="16" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="17" font-weight="800">Swaram</text>
    <text x="155" y="15" fill="#00FF66" font-family="'Fira Code', monospace" font-size="12">// Voice Accessibility PWA</text>

    <text x="0" y="48" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Voice-first form-filling application engineered for blind &amp; low-vision users.</text>
    <text x="0" y="70" fill="#8899A6" font-family="'Inter', sans-serif" font-size="12">Custom acoustic feedback loops and speech-to-intent field navigation.</text>

    <!-- Tags -->
    <g transform="translate(0, 96)">
      <rect x="0" y="0" width="70" height="22" rx="11" fill="#0b2419" stroke="#00FF66" stroke-opacity="0.3"/>
      <text x="35" y="15" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10">Voice UI</text>
      
      <rect x="76" y="0" width="50" height="22" rx="11" fill="#0b2419" stroke="#00FF66" stroke-opacity="0.3"/>
      <text x="101" y="15" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10">PWA</text>

      <rect x="132" y="0" width="94" height="22" rx="11" fill="#0b2419" stroke="#00FF66" stroke-opacity="0.3"/>
      <text x="179" y="15" text-anchor="middle" fill="#00FF66" font-family="'Fira Code', monospace" font-size="10">Accessibility</text>
    </g>
  </g>

  <!-- Divider -->
  <line x1="450" y1="20" x2="450" y2="160" stroke="#00FF66" stroke-opacity="0.15" stroke-width="1" stroke-dasharray="4 4"/>

  <!-- Right Side Quest: Operation Vault -->
  <g transform="translate(480, 24)">
    <rect x="0" y="0" width="60" height="20" rx="4" fill="#041b17" stroke="#00F5D4" stroke-opacity="0.5"/>
    <text x="30" y="14" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10" font-weight="700">QUEST 02</text>
    
    <text x="75" y="16" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="17" font-weight="800">Operation Vault</text>
    <text x="215" y="15" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="12">// Induction Puzzle</text>

    <text x="0" y="48" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Mobile-first interactive crypto/logic puzzle game for the CSI induction event.</text>
    <text x="0" y="70" fill="#8899A6" font-family="'Inter', sans-serif" font-size="12">Multi-tier cipher mechanics, rapid live event scoring, and team puzzle gates.</text>

    <!-- Tags -->
    <g transform="translate(0, 96)">
      <rect x="0" y="0" width="90" height="22" rx="11" fill="#07241e" stroke="#00F5D4" stroke-opacity="0.3"/>
      <text x="45" y="15" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10">Mobile-First</text>

      <rect x="96" y="0" width="80" height="22" rx="11" fill="#07241e" stroke="#00F5D4" stroke-opacity="0.3"/>
      <text x="136" y="15" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10">CSI Event</text>

      <rect x="182" y="0" width="90" height="22" rx="11" fill="#07241e" stroke="#00F5D4" stroke-opacity="0.3"/>
      <text x="227" y="15" text-anchor="middle" fill="#00F5D4" font-family="'Fira Code', monospace" font-size="10">Puzzle Logic</text>
    </g>
  </g>
</svg>'''
    with open('assets/cards/side-quests.svg', 'w') as f:
        f.write(svg)
    print("Created assets/cards/side-quests.svg")

def create_headers():
    headers = [
        ('header-about.svg', '// 01 : IDENTITY & ARCHITECTURAL DIRECTIVE', 'WHO I AM // HOW I DIRECT AI'),
        ('header-projects.svg', '// 02 : FEATURED SYSTEMS & ENGINES', 'CORE ARCHITECTURES & ACTIVE BUILDS'),
        ('header-stack.svg', '// 03 : ABSORBED CAPABILITIES', 'POLYMORPHIC TECH STACK & TOOLS'),
        ('header-activations.svg', '// 04 : ACTIVE FREQUENCIES', 'ROLES, CHAPTERS & COMMUNITY NODES'),
        ('header-telemetry.svg', '// 05 : TELEMETRY & METRICS', 'LIVE REPO ACTIVITY & CONTRIBUTION GRID')
    ]
    for filename, title, sub in headers:
        svg = f'''<svg width="900" height="50" viewBox="0 0 900 50" fill="none" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="49" x2="900" y2="49" stroke="#00FF66" stroke-opacity="0.2" stroke-width="1"/>
  <rect x="0" y="8" width="6" height="34" rx="2" fill="#00FF66"/>
  <text x="18" y="27" fill="#00FF66" font-family="'Fira Code', monospace" font-size="14" font-weight="700" letter-spacing="1.5">{title}</text>
  <text x="890" y="27" text-anchor="end" fill="#8899A6" font-family="'Fira Code', monospace" font-size="11" letter-spacing="1">{sub}</text>
  <line x1="18" y1="36" x2="250" y2="36" stroke="#00F5D4" stroke-opacity="0.5" stroke-width="1"/>
</svg>'''
        with open(f'assets/headers/{filename}', 'w') as f:
            f.write(svg)
        print(f"Created assets/headers/{filename}")

if __name__ == '__main__':
    create_svg_hud()
    create_card_skloop()
    create_card_aether()
    create_card_name_sandbox()
    create_card_academic_engine()
    create_card_side_quests()
    create_headers()
