import os
import xml.etree.ElementTree as ET

def generate_all():
    os.makedirs('assets/cards', exist_ok=True)
    os.makedirs('assets/headers', exist_ok=True)

    # 1. SLIME HUD
    hud_svg = '''<svg width="920" height="200" viewBox="0 0 920 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hudBg" x1="0" y1="0" x2="920" y2="200" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#07120e"/>
      <stop offset="50%" stop-color="#0b1a14"/>
      <stop offset="100%" stop-color="#050c09"/>
    </linearGradient>
    <linearGradient id="hudBorder" x1="0" y1="0" x2="920" y2="200" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#34D399" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="slimeDrop" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#34D399"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Container -->
  <rect x="1" y="1" width="918" height="198" rx="16" fill="url(#hudBg)" stroke="url(#hudBorder)" stroke-width="1.5"/>

  <!-- Top Glass Accent Strip -->
  <path d="M 1 16 C 1 7.716 7.716 1 16 1 L 904 1 C 912.284 1 919 7.716 919 16 L 919 44 L 1 44 Z" fill="#0f241c" fill-opacity="0.7"/>
  <line x1="1" y1="44" x2="919" y2="44" stroke="#10B981" stroke-opacity="0.25" stroke-width="1"/>

  <!-- Top Header Content -->
  <!-- Cute Slime Icon -->
  <g transform="translate(24, 14)">
    <path d="M 10 3 C 5 3, 2 8, 2 13 C 2 19, 6 21, 11 21 C 16 21, 20 19, 20 13 C 20 8, 17 3, 10 3 Z" fill="url(#slimeDrop)"/>
    <circle cx="8" cy="11" r="1.5" fill="#04120c"/>
    <circle cx="14" cy="11" r="1.5" fill="#04120c"/>
    <ellipse cx="6" cy="7" rx="2.5" ry="1.2" fill="#ffffff" opacity="0.6"/>
  </g>
  <text x="52" y="28" fill="#34D399" font-family="'Inter', sans-serif" font-size="13" font-weight="700" letter-spacing="0.5">SLIME CREATOR STATION</text>
  <text x="238" y="28" fill="#64748B" font-family="'Inter', sans-serif" font-size="12">•</text>
  <text x="252" y="28" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">Directing AI Tooling &amp; Systems Architecture</text>

  <!-- Status Pill Right -->
  <rect x="734" y="13" width="162" height="22" rx="11" fill="#092117" stroke="#10B981" stroke-opacity="0.4"/>
  <circle cx="748" cy="24" r="4" fill="#34D399" filter="url(#softGlow)"/>
  <text x="760" y="28" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="600">STATE: TRANSLUCENT</text>

  <!-- Content Columns -->
  <!-- Column 1: Identity & Habitat -->
  <g transform="translate(30, 68)">
    <rect x="0" y="0" width="74" height="18" rx="4" fill="#0d291e"/>
    <text x="37" y="13" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="9" font-weight="700">IDENTITY</text>
    <text x="0" y="38" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="16" font-weight="700">Tejas K M ("Shinz")</text>
    <text x="0" y="56" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">ASIET CSE '29 • Batch Representative</text>
    <text x="0" y="74" fill="#64748B" font-family="'Inter', sans-serif" font-size="12">Kerala, India • CSI, µLearn, IEEE</text>
  </g>

  <!-- Divider 1 -->
  <line x1="280" y1="62" x2="280" y2="175" stroke="#10B981" stroke-opacity="0.15" stroke-width="1" stroke-dasharray="3 3"/>

  <!-- Column 2: Tooling & Literacy -->
  <g transform="translate(310, 68)">
    <rect x="0" y="0" width="86" height="18" rx="4" fill="#0d291e"/>
    <text x="43" y="13" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="9" font-weight="700">AI DIRECTIVE</text>
    <text x="0" y="38" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="15" font-weight="600">AI-Directed Engineering</text>
    <text x="0" y="56" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">Claude Code • Antigravity • Groq / Llama</text>
    <text x="0" y="74" fill="#34D399" font-family="'Inter', sans-serif" font-size="12" font-weight="500">Deep Code Literacy &amp; Architecture</text>
  </g>

  <!-- Divider 2 -->
  <line x1="590" y1="62" x2="590" y2="175" stroke="#10B981" stroke-opacity="0.15" stroke-width="1" stroke-dasharray="3 3"/>

  <!-- Column 3: Vision & Fluidity -->
  <g transform="translate(620, 68)">
    <rect x="0" y="0" width="88" height="18" rx="4" fill="#0d291e"/>
    <text x="44" y="13" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="9" font-weight="700">TRAJECTORY</text>
    <text x="0" y="38" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Technical Product Leadership</text>
    <text x="0" y="56" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">End-to-End Ownership &amp; Ventures</text>
    
    <!-- Fluidity Meter -->
    <g transform="translate(0, 72)">
      <rect x="0" y="0" width="240" height="10" rx="5" fill="#071b12" stroke="#10B981" stroke-opacity="0.3"/>
      <rect x="2" y="2" width="210" height="6" rx="3" fill="#34D399" filter="url(#softGlow)"/>
      <text x="0" y="24" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="500">Fluidity: Rapidly Absorbing Complexity</text>
    </g>
  </g>
</svg>'''

    with open('assets/slime-hud.svg', 'w') as f:
        f.write(hud_svg)

    # 2. SKLOOP CARD
    skloop_svg = '''<svg width="920" height="340" viewBox="0 0 920 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="skBg" x1="0" y1="0" x2="920" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#071410"/>
      <stop offset="60%" stop-color="#0a1d17"/>
      <stop offset="100%" stop-color="#050e0a"/>
    </linearGradient>
    <linearGradient id="skBorder" x1="0" y1="0" x2="920" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#00FF66" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#047857" stop-opacity="0.7"/>
    </linearGradient>
    <linearGradient id="slimeBody" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4ade80"/>
      <stop offset="60%" stop-color="#22c55e"/>
      <stop offset="100%" stop-color="#15803d"/>
    </linearGradient>
    <filter id="skGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect x="1" y="1" width="918" height="338" rx="16" fill="url(#skBg)" stroke="url(#skBorder)" stroke-width="1.5"/>

  <!-- Header Strip -->
  <g transform="translate(32, 26)">
    <rect x="0" y="0" width="80" height="22" rx="6" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.4"/>
    <text x="40" y="15" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11" font-weight="700">PROJECT 01</text>

    <rect x="92" y="0" width="168" height="22" rx="6" fill="#0d2b1f" stroke="#34D399" stroke-opacity="0.4"/>
    <text x="176" y="15" text-anchor="middle" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="600">IN ACTIVE DEVELOPMENT</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="32" y="84" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="28" font-weight="800" letter-spacing="-0.5">Skloop</text>
  <text x="140" y="82" fill="#34D399" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Gamified EdTech Platform</text>
  <text x="32" y="110" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Architecting immersive narrative coding worlds with live execution and adaptive AI guidance.</text>

  <!-- Features Tree -->
  <g transform="translate(32, 142)">
    <!-- Item 1 -->
    <circle cx="4" cy="4" r="3" fill="#34D399"/>
    <text x="18" y="8" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Loopverse &amp; Underlayer:</text>
    <text x="185" y="8" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Dual narrative worlds structuring curriculum &amp; hidden hacker puzzles</text>

    <!-- Item 2 -->
    <circle cx="4" cy="32" r="3" fill="#34D399"/>
    <text x="18" y="36" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Loopy AI Companion:</text>
    <text x="165" y="36" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Dynamic dual-personality mentor balancing guided help &amp; code challenges</text>

    <!-- Item 3 -->
    <circle cx="4" cy="60" r="3" fill="#34D399"/>
    <text x="18" y="64" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Progression &amp; Monaco:</text>
    <text x="180" y="64" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">In-browser IDE environment, XP loops, quest branches, and gear shop</text>
  </g>

  <!-- Tech Pills Row -->
  <g transform="translate(32, 245)">
    <rect x="0" y="0" width="74" height="26" rx="13" fill="#0d2a1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="37" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">Next.js</text>

    <rect x="82" y="0" width="94" height="26" rx="13" fill="#0d2a1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="129" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">TypeScript</text>

    <rect x="184" y="0" width="76" height="26" rx="13" fill="#0d2a1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="222" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">Monaco</text>

    <rect x="268" y="0" width="86" height="26" rx="13" fill="#0d2a1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="311" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">AI Agents</text>

    <rect x="362" y="0" width="84" height="26" rx="13" fill="#0d2a1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="404" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">Supabase</text>
  </g>

  <!-- Ownership Meta Line -->
  <g transform="translate(32, 295)">
    <text x="0" y="14" fill="#64748B" font-family="'Inter', sans-serif" font-size="12" font-weight="600">ROLE FOCUS: ARCHITECTURE, UI &amp; PRODUCT EXPERIENCE</text>
    <text x="400" y="14" fill="#10B981" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Explore Repository →</text>
  </g>

  <!-- Right Visual: Detailed Mascot Slime "Loopy" + Mini IDE Window -->
  <g transform="translate(640, 50)">
    <!-- Mini IDE Window Frame -->
    <rect x="0" y="30" width="240" height="190" rx="10" fill="#06120e" stroke="#10B981" stroke-opacity="0.4" stroke-width="1.5"/>
    <path d="M 0 40 C 0 34.477 4.477 30 10 30 L 230 30 C 235.523 30 240 34.477 240 40 L 240 56 L 0 56 Z" fill="#0e2a1e"/>
    <circle cx="14" cy="43" r="3.5" fill="#ef4444"/>
    <circle cx="26" cy="43" r="3.5" fill="#eab308"/>
    <circle cx="38" cy="43" r="3.5" fill="#22c55e"/>
    <text x="60" y="47" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10">loopy.agent.ts</text>

    <!-- Syntax Code Lines -->
    <text x="16" y="80" fill="#34D399" font-family="'Fira Code', monospace" font-size="10">const</text>
    <text x="52" y="80" fill="#FFFFFF" font-family="'Fira Code', monospace" font-size="10">loopy =</text>
    <text x="106" y="80" fill="#38bdf8" font-family="'Fira Code', monospace" font-size="10">new</text>
    <text x="130" y="80" fill="#facc15" font-family="'Fira Code', monospace" font-size="10">Companion({</text>

    <text x="28" y="98" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10">persona:</text>
    <text x="82" y="98" fill="#4ade80" font-family="'Fira Code', monospace" font-size="10">'mentor'</text>
    <text x="136" y="98" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10">|</text>
    <text x="148" y="98" fill="#f87171" font-family="'Fira Code', monospace" font-size="10">'tester'</text>

    <text x="28" y="116" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10">mode:</text>
    <text x="64" y="116" fill="#4ade80" font-family="'Fira Code', monospace" font-size="10">'adaptive'</text>

    <text x="16" y="134" fill="#facc15" font-family="'Fira Code', monospace" font-size="10">});</text>

    <!-- Mini Quest Badge Box inside IDE -->
    <rect x="16" y="150" width="208" height="54" rx="6" fill="#0d2b1f" stroke="#34D399" stroke-opacity="0.3"/>
    <text x="28" y="168" fill="#F8FAFC" font-family="'Inter', sans-serif" font-size="11" font-weight="700">Quest: Defeat Bug Dragon</text>
    <rect x="28" y="176" width="184" height="6" rx="3" fill="#071b12"/>
    <rect x="28" y="176" width="138" height="6" rx="3" fill="#34D399" filter="url(#skGlow)"/>
    <text x="28" y="196" fill="#34D399" font-family="'Fira Code', monospace" font-size="9">+250 XP • Loopverse Tier 2</text>

    <!-- Cute 3D-style Slime Mascot Peeking Out -->
    <g transform="translate(140, -10)">
      <!-- Drop Shadow -->
      <ellipse cx="40" cy="55" rx="35" ry="8" fill="#000000" opacity="0.4"/>
      <!-- Slime Body -->
      <path d="M 40 8 C 18 8, 4 28, 4 48 C 4 70, 18 78, 40 78 C 62 78, 76 70, 76 48 C 76 28, 62 8, 40 8 Z" fill="url(#slimeBody)" filter="url(#skGlow)"/>
      <!-- Glossy Reflection -->
      <ellipse cx="28" cy="24" rx="14" ry="7" transform="rotate(-30 28 24)" fill="#ffffff" opacity="0.55"/>
      <ellipse cx="22" cy="18" rx="4" ry="2" fill="#ffffff" opacity="0.75"/>
      <!-- Cute Eyes -->
      <ellipse cx="30" cy="45" rx="3.5" ry="5.5" fill="#082315"/>
      <circle cx="31.5" cy="43.5" r="1.5" fill="#ffffff"/>
      <ellipse cx="50" cy="45" rx="3.5" ry="5.5" fill="#082315"/>
      <circle cx="51.5" cy="43.5" r="1.5" fill="#ffffff"/>
      <!-- Smiling Mouth -->
      <path d="M 36 53 Q 40 58, 44 53" stroke="#082315" stroke-width="2" stroke-linecap="round" fill="none"/>
      <!-- Cheeks -->
      <ellipse cx="24" cy="50" rx="4" ry="2" fill="#ff70a6" opacity="0.45"/>
      <ellipse cx="56" cy="50" rx="4" ry="2" fill="#ff70a6" opacity="0.45"/>
      <!-- Small floating drip -->
      <circle cx="68" cy="20" r="3" fill="#4ade80" opacity="0.8"/>
      <circle cx="74" cy="12" r="1.5" fill="#34D399" opacity="0.6"/>
    </g>
  </g>
</svg>'''

    with open('assets/cards/skloop.svg', 'w') as f:
        f.write(skloop_svg)

    # 3. AETHER READER CARD
    aether_svg = '''<svg width="920" height="340" viewBox="0 0 920 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="aeBg" x1="0" y1="0" x2="920" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#061214"/>
      <stop offset="60%" stop-color="#091c20"/>
      <stop offset="100%" stop-color="#040e10"/>
    </linearGradient>
    <linearGradient id="aeBorder" x1="0" y1="0" x2="920" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#10b981" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.7"/>
    </linearGradient>
    <linearGradient id="mangaPage" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#164e63"/>
      <stop offset="100%" stop-color="#083344"/>
    </linearGradient>
    <filter id="aeGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect x="1" y="1" width="918" height="338" rx="16" fill="url(#aeBg)" stroke="url(#aeBorder)" stroke-width="1.5"/>

  <!-- Header Strip -->
  <g transform="translate(32, 26)">
    <rect x="0" y="0" width="80" height="22" rx="6" fill="#0c2c33" stroke="#06b6d4" stroke-opacity="0.4"/>
    <text x="40" y="15" text-anchor="middle" fill="#22d3ee" font-family="'Fira Code', monospace" font-size="11" font-weight="700">PROJECT 02</text>

    <rect x="92" y="0" width="220" height="22" rx="6" fill="#0c2c33" stroke="#22d3ee" stroke-opacity="0.4"/>
    <text x="202" y="15" text-anchor="middle" fill="#22d3ee" font-family="'Inter', sans-serif" font-size="11" font-weight="600">SHIPPED • PRIVATE ARCHITECTURE</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="32" y="84" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="28" font-weight="800" letter-spacing="-0.5">Aether Reader</text>
  <text x="230" y="82" fill="#22d3ee" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Full-Stack Manga &amp; Manhwa PWA</text>
  <text x="32" y="110" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">High-speed distraction-free reader engine aggregating multi-scanlation feeds with telemetry.</text>

  <!-- Features Tree -->
  <g transform="translate(32, 142)">
    <circle cx="4" cy="4" r="3" fill="#22d3ee"/>
    <text x="18" y="8" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Source-Adapter Pattern:</text>
    <text x="195" y="8" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Decoupled Express scrapers abstracting multiple upstream scanlation feeds</text>

    <circle cx="4" cy="32" r="3" fill="#22d3ee"/>
    <text x="18" y="36" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">MAL-Style Tracking:</text>
    <text x="168" y="36" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Chapter bookmarking, reading velocity telemetry &amp; full analytics dashboard</text>

    <circle cx="4" cy="60" r="3" fill="#22d3ee"/>
    <text x="18" y="64" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Offline Resilience:</text>
    <text x="160" y="64" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">PWA Service Worker caching + local IndexedDB with Supabase cloud sync</text>
  </g>

  <!-- Tech Pills Row -->
  <g transform="translate(32, 245)">
    <rect x="0" y="0" width="90" height="26" rx="13" fill="#0c2b33" stroke="#06b6d4" stroke-opacity="0.3"/>
    <text x="45" y="17" text-anchor="middle" fill="#22d3ee" font-family="'Fira Code', monospace" font-size="11">Next.js 15</text>

    <rect x="98" y="0" width="94" height="26" rx="13" fill="#0c2b33" stroke="#06b6d4" stroke-opacity="0.3"/>
    <text x="145" y="17" text-anchor="middle" fill="#22d3ee" font-family="'Fira Code', monospace" font-size="11">TypeScript</text>

    <rect x="200" y="0" width="76" height="26" rx="13" fill="#0c2b33" stroke="#06b6d4" stroke-opacity="0.3"/>
    <text x="238" y="17" text-anchor="middle" fill="#22d3ee" font-family="'Fira Code', monospace" font-size="11">Tailwind</text>

    <rect x="284" y="0" width="76" height="26" rx="13" fill="#0c2b33" stroke="#06b6d4" stroke-opacity="0.3"/>
    <text x="322" y="17" text-anchor="middle" fill="#22d3ee" font-family="'Fira Code', monospace" font-size="11">Express</text>

    <rect x="368" y="0" width="84" height="26" rx="13" fill="#0c2b33" stroke="#06b6d4" stroke-opacity="0.3"/>
    <text x="410" y="17" text-anchor="middle" fill="#22d3ee" font-family="'Fira Code', monospace" font-size="11">Supabase</text>
  </g>

  <!-- Ownership Meta Line -->
  <g transform="translate(32, 295)">
    <text x="0" y="14" fill="#64748B" font-family="'Inter', sans-serif" font-size="12" font-weight="600">ROLE FOCUS: CREATOR &amp; FULL-STACK ARCHITECT</text>
    <text x="380" y="14" fill="#06b6d4" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Architecture Specs →</text>
  </g>

  <!-- Right Visual: Detailed E-Reader / Manhwa UI Mockup -->
  <g transform="translate(660, 45)">
    <!-- Reader Tablet Body -->
    <rect x="0" y="0" width="210" height="250" rx="16" fill="#082026" stroke="#06b6d4" stroke-opacity="0.5" stroke-width="2"/>
    <!-- Screen Bezel -->
    <rect x="10" y="10" width="190" height="230" rx="10" fill="#041217"/>
    
    <!-- Top Status Bar -->
    <rect x="10" y="10" width="190" height="24" rx="10" fill="#0a2e37"/>
    <text x="22" y="26" fill="#22d3ee" font-family="'Fira Code', monospace" font-size="9">CH. 142 : AWAKENING</text>
    <circle cx="185" cy="22" r="3" fill="#22c55e"/>

    <!-- Manga Illustration Frame Inside Screen -->
    <rect x="20" y="42" width="170" height="135" rx="6" fill="url(#mangaPage)"/>
    <!-- Speed lines in comic panel -->
    <line x1="25" y1="45" x2="70" y2="90" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1.5"/>
    <line x1="185" y1="45" x2="140" y2="90" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1.5"/>
    <circle cx="105" cy="100" r="28" fill="#083344" stroke="#22d3ee" stroke-width="1.5" filter="url(#aeGlow)"/>
    <polygon points="105,80 120,115 90,115" fill="#22d3ee" opacity="0.8"/>

    <!-- Reading Progress Floating Bar -->
    <g transform="translate(20, 188)">
      <rect x="0" y="0" width="170" height="42" rx="6" fill="#07252c" stroke="#22d3ee" stroke-opacity="0.4"/>
      <text x="10" y="18" fill="#F8FAFC" font-family="'Inter', sans-serif" font-size="10" font-weight="700">Reading Velocity: 42 Ch/Hr</text>
      <!-- Mini Progress Ring / Bar -->
      <rect x="10" y="26" width="110" height="6" rx="3" fill="#041418"/>
      <rect x="10" y="26" width="88" height="6" rx="3" fill="#22d3ee"/>
      <text x="128" y="32" fill="#22d3ee" font-family="'Fira Code', monospace" font-size="9">80% MAL</text>
    </g>
  </g>
</svg>'''

    with open('assets/cards/aether.svg', 'w') as f:
        f.write(aether_svg)

    # 4. NAME SANDBOX CARD
    sandbox_svg = '''<svg width="920" height="340" viewBox="0 0 920 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sbBg" x1="0" y1="0" x2="920" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#071510"/>
      <stop offset="60%" stop-color="#0b2219"/>
      <stop offset="100%" stop-color="#05100c"/>
    </linearGradient>
    <linearGradient id="sbBorder" x1="0" y1="0" x2="920" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.7"/>
    </linearGradient>
    <filter id="sbGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect x="1" y="1" width="918" height="338" rx="16" fill="url(#sbBg)" stroke="url(#sbBorder)" stroke-width="1.5"/>

  <!-- Header Strip -->
  <g transform="translate(32, 26)">
    <rect x="0" y="0" width="80" height="22" rx="6" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.4"/>
    <text x="40" y="15" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11" font-weight="700">PROJECT 03</text>

    <rect x="92" y="0" width="220" height="22" rx="6" fill="#0d2b1f" stroke="#34D399" stroke-opacity="0.4"/>
    <text x="202" y="15" text-anchor="middle" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="600">96% PARSER PASS RATE • 386 TESTS</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="32" y="84" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="28" font-weight="800" letter-spacing="-0.5">NAME Sandbox</text>
  <text x="250" y="82" fill="#34D399" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Multiplayer Board Game Platform</text>
  <text x="32" y="110" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Tile-based multiplayer creation sandbox with a custom natural language rule compiler.</text>

  <!-- Features Tree -->
  <g transform="translate(32, 142)">
    <circle cx="4" cy="4" r="3" fill="#34D399"/>
    <text x="18" y="8" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">English-to-AST Compiler:</text>
    <text x="195" y="8" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Compiles natural game rules into deterministic AST trees with 386 test suites</text>

    <circle cx="4" cy="32" r="3" fill="#34D399"/>
    <text x="18" y="36" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Hybrid Combat System:</text>
    <text x="185" y="36" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Deep battle loops merging Pokémon type matchups with D&amp;D d20 action economy</text>

    <circle cx="4" cy="60" r="3" fill="#34D399"/>
    <text x="18" y="64" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Realtime State Engine:</text>
    <text x="180" y="64" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Authoritative multiplayer room synchronization powered by Colyseus WebSockets</text>
  </g>

  <!-- Tech Pills Row -->
  <g transform="translate(32, 245)">
    <rect x="0" y="0" width="84" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="42" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">Colyseus</text>

    <rect x="92" y="0" width="76" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="130" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">Next.js</text>

    <rect x="176" y="0" width="100" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="226" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">AST Parser</text>

    <rect x="284" y="0" width="84" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="326" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">Supabase</text>

    <rect x="376" y="0" width="94" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="423" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">TypeScript</text>
  </g>

  <!-- Ownership Meta Line -->
  <g transform="translate(32, 295)">
    <text x="0" y="14" fill="#64748B" font-family="'Inter', sans-serif" font-size="12" font-weight="600">ROLE FOCUS: CORE SYSTEMS &amp; AST ENGINE DEVELOPER</text>
    <text x="410" y="14" fill="#10B981" font-family="'Inter', sans-serif" font-size="12" font-weight="600">View Sandbox Engine →</text>
  </g>

  <!-- Right Visual: Isometric Combat Board + d20 Die + AST Flow -->
  <g transform="translate(650, 40)">
    <!-- Board Frame -->
    <rect x="0" y="0" width="230" height="255" rx="14" fill="#082016" stroke="#10B981" stroke-opacity="0.4" stroke-width="1.5"/>

    <!-- Isometric Hex Grid Tiles -->
    <g transform="translate(115, 65)">
      <!-- Tile 1 Center -->
      <polygon points="0,-25 35,-5 35,25 0,45 -35,25 -35,-5" fill="#124a30" stroke="#34D399" stroke-width="1.5"/>
      <!-- Tile 2 Top Right -->
      <polygon points="50,-50 80,-35 80,-5 50,10 20,-5 20,-35" fill="#0d3824" stroke="#10B981" stroke-opacity="0.6" stroke-width="1"/>
      <!-- Tile 3 Top Left -->
      <polygon points="-50,-50 -20,-35 -20,-5 -50,10 -80,-5 -80,-35" fill="#0d3824" stroke="#10B981" stroke-opacity="0.6" stroke-width="1"/>

      <!-- Glowing Player Unit on Center Tile -->
      <circle cx="0" cy="5" r="14" fill="#34D399" fill-opacity="0.2" filter="url(#sbGlow)"/>
      <circle cx="0" cy="5" r="7" fill="#34D399"/>
      
      <!-- 20-sided Die Floating -->
      <g transform="translate(45, -20)">
        <polygon points="0,-16 14,-6 14,10 0,18 -14,10 -14,-6" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
        <text x="0" y="6" text-anchor="middle" fill="#082016" font-family="'Inter', sans-serif" font-size="10" font-weight="900">20</text>
      </g>
    </g>

    <!-- Natural Language -> AST Transformation Card -->
    <g transform="translate(15, 155)">
      <rect x="0" y="0" width="200" height="85" rx="8" fill="#051710" stroke="#34D399" stroke-opacity="0.4"/>
      <text x="12" y="20" fill="#38bdf8" font-family="'Fira Code', monospace" font-size="9">RULE: "on enter tile -&gt; strike"</text>
      <line x1="12" y1="28" x2="188" y2="28" stroke="#10B981" stroke-opacity="0.2"/>
      <text x="12" y="44" fill="#34D399" font-family="'Fira Code', monospace" font-size="9">AST: TriggerNode(TileEnter)</text>
      <text x="36" y="58" fill="#F8FAFC" font-family="'Fira Code', monospace" font-size="9">.Action(Electric, d20)</text>
      <rect x="12" y="66" width="176" height="14" rx="3" fill="#124a30"/>
      <text x="100" y="77" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="8" font-weight="700">COMPILER PASS RATE: 96.4%</text>
    </g>
  </g>
</svg>'''

    with open('assets/cards/name-sandbox.svg', 'w') as f:
        f.write(sandbox_svg)

    # 5. ACADEMIC INTEGRITY ENGINE CARD
    academic_svg = '''<svg width="920" height="340" viewBox="0 0 920 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="acBg" x1="0" y1="0" x2="920" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#061410"/>
      <stop offset="60%" stop-color="#091f17"/>
      <stop offset="100%" stop-color="#040e0a"/>
    </linearGradient>
    <linearGradient id="acBorder" x1="0" y1="0" x2="920" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#22c55e" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#047857" stop-opacity="0.7"/>
    </linearGradient>
    <filter id="acGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect x="1" y="1" width="918" height="338" rx="16" fill="url(#acBg)" stroke="url(#acBorder)" stroke-width="1.5"/>

  <!-- Header Strip -->
  <g transform="translate(32, 26)">
    <rect x="0" y="0" width="80" height="22" rx="6" fill="#0c2d20" stroke="#10B981" stroke-opacity="0.4"/>
    <text x="40" y="15" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11" font-weight="700">PROJECT 04</text>

    <rect x="92" y="0" width="220" height="22" rx="6" fill="#0c2d20" stroke="#34D399" stroke-opacity="0.4"/>
    <text x="202" y="15" text-anchor="middle" fill="#34D399" font-family="'Inter', sans-serif" font-size="11" font-weight="600">KTU OOP PROJECT • 4-PERSON TEAM</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="32" y="84" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="28" font-weight="800" letter-spacing="-0.5">Academic Integrity Engine</text>
  <text x="380" y="82" fill="#34D399" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Plagiarism &amp; AI Detection Backend</text>
  <text x="32" y="110" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">High-throughput detection microservice analyzing code structure, syntax fingerprints, and AI markers.</text>

  <!-- Features Tree -->
  <g transform="translate(32, 142)">
    <circle cx="4" cy="4" r="3" fill="#34D399"/>
    <text x="18" y="8" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Multi-Language Tokenizer:</text>
    <text x="205" y="8" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Structural AST tokenization supporting Java, C, C++, Python, and JavaScript</text>

    <circle cx="4" cy="32" r="3" fill="#34D399"/>
    <text x="18" y="36" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Winnowing &amp; AI Heuristics:</text>
    <text x="205" y="36" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">K-gram fingerprinting coupled with algorithmic AI authorship stylometry</text>

    <circle cx="4" cy="60" r="3" fill="#34D399"/>
    <text x="18" y="64" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="13" font-weight="600">REST Microservice Core:</text>
    <text x="180" y="64" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Javalin embedded HTTP runtime with SQLite persistent fingerprint registry</text>
  </g>

  <!-- Tech Pills Row -->
  <g transform="translate(32, 245)">
    <rect x="0" y="0" width="86" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="43" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">Java Core</text>

    <rect x="94" y="0" width="76" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="132" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">Javalin</text>

    <rect x="178" y="0" width="70" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="213" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">SQLite</text>

    <rect x="256" y="0" width="100" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="306" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">AST Winnow</text>

    <rect x="364" y="0" width="80" height="26" rx="13" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.3"/>
    <text x="404" y="17" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="11">REST API</text>
  </g>

  <!-- Ownership Meta Line -->
  <g transform="translate(32, 295)">
    <text x="0" y="14" fill="#64748B" font-family="'Inter', sans-serif" font-size="12" font-weight="600">ROLE FOCUS: BACKEND &amp; DETECTION ENGINE ARCHITECT</text>
    <text x="410" y="14" fill="#10B981" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Engine Source Code →</text>
  </g>

  <!-- Right Visual: Code Inspector & Circular Similarity Gauge -->
  <g transform="translate(650, 40)">
    <rect x="0" y="0" width="230" height="255" rx="14" fill="#072016" stroke="#10B981" stroke-opacity="0.4" stroke-width="1.5"/>

    <!-- Circular Gauge -->
    <g transform="translate(115, 75)">
      <!-- Outer Arc -->
      <circle cx="0" cy="0" r="45" stroke="#0e3a27" stroke-width="8" fill="none"/>
      <!-- Active Gauge Arc (approx 270 deg) -->
      <circle cx="0" cy="0" r="45" stroke="#34D399" stroke-width="8" stroke-dasharray="210 280" stroke-linecap="round" fill="none" filter="url(#acGlow)"/>
      <text x="0" y="8" text-anchor="middle" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="900">88%</text>
      <text x="0" y="24" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="8" font-weight="600">SIMILARITY</text>
    </g>

    <!-- Side-by-side Fingerprint Diff Matrix -->
    <g transform="translate(15, 145)">
      <rect x="0" y="0" width="200" height="95" rx="8" fill="#04140e" stroke="#10B981" stroke-opacity="0.3"/>
      <!-- Left Token Hash -->
      <text x="12" y="20" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9">SUBMISSION_AST</text>
      <text x="12" y="38" fill="#34D399" font-family="'Fira Code', monospace" font-size="9">METHOD_DECL [A4]</text>
      <text x="12" y="52" fill="#34D399" font-family="'Fira Code', monospace" font-size="9">LOOP_FOR_IN [B1]</text>
      <text x="12" y="66" fill="#34D399" font-family="'Fira Code', monospace" font-size="9">RET_EXPR_ID [C7]</text>

      <!-- Center Match Connector -->
      <line x1="100" y1="12" x2="100" y2="78" stroke="#10B981" stroke-opacity="0.3" stroke-dasharray="2 2"/>

      <!-- Right Token Hash -->
      <text x="110" y="20" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9">CORPUS_TARGET</text>
      <text x="110" y="38" fill="#34D399" font-family="'Fira Code', monospace" font-size="9">METHOD_DECL [A4]</text>
      <text x="110" y="52" fill="#34D399" font-family="'Fira Code', monospace" font-size="9">LOOP_FOR_IN [B1]</text>
      <text x="110" y="66" fill="#34D399" font-family="'Fira Code', monospace" font-size="9">RET_EXPR_ID [C7]</text>

      <rect x="12" y="74" width="176" height="14" rx="3" fill="#124a30"/>
      <text x="100" y="84" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="8" font-weight="700">WINNOW HASH MATCH: CONFIRMED</text>
    </g>
  </g>
</svg>'''

    with open('assets/cards/academic-engine.svg', 'w') as f:
        f.write(academic_svg)

    # 6. SIDE QUESTS CARD
    side_svg = '''<svg width="920" height="200" viewBox="0 0 920 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sqBg" x1="0" y1="0" x2="920" y2="200" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#061410"/>
      <stop offset="50%" stop-color="#091d17"/>
      <stop offset="100%" stop-color="#050f0b"/>
    </linearGradient>
    <linearGradient id="sqBorder" x1="0" y1="0" x2="920" y2="200" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#34D399" stop-opacity="0.3"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="918" height="198" rx="16" fill="url(#sqBg)" stroke="url(#sqBorder)" stroke-width="1.5"/>

  <!-- Left Quest: Swaram -->
  <g transform="translate(32, 28)">
    <rect x="0" y="0" width="70" height="22" rx="6" fill="#0d2b1f" stroke="#10B981" stroke-opacity="0.4"/>
    <text x="35" y="15" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700">QUEST 01</text>
    
    <text x="82" y="18" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="800">Swaram</text>
    <text x="160" y="17" fill="#34D399" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Voice Accessibility PWA</text>

    <text x="0" y="52" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Voice-first form-filling application engineered for blind &amp; low-vision users.</text>
    <text x="0" y="74" fill="#64748B" font-family="'Inter', sans-serif" font-size="12">Custom acoustic feedback loops and speech-to-intent field navigation.</text>

    <!-- Waveform Visualizer -->
    <g transform="translate(0, 95)">
      <rect x="0" y="8" width="4" height="16" rx="2" fill="#34D399"/>
      <rect x="8" y="2" width="4" height="28" rx="2" fill="#34D399"/>
      <rect x="16" y="6" width="4" height="20" rx="2" fill="#34D399"/>
      <rect x="24" y="0" width="4" height="32" rx="2" fill="#34D399"/>
      <rect x="32" y="4" width="4" height="24" rx="2" fill="#34D399"/>
      <rect x="40" y="10" width="4" height="12" rx="2" fill="#34D399"/>

      <g transform="translate(60, 4)">
        <rect x="0" y="0" width="76" height="24" rx="12" fill="#0d2a1e" stroke="#10B981" stroke-opacity="0.3"/>
        <text x="38" y="16" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="10">Voice UI</text>

        <rect x="82" y="0" width="56" height="24" rx="12" fill="#0d2a1e" stroke="#10B981" stroke-opacity="0.3"/>
        <text x="110" y="16" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="10">PWA</text>

        <rect x="144" y="0" width="96" height="24" rx="12" fill="#0d2a1e" stroke="#10B981" stroke-opacity="0.3"/>
        <text x="192" y="16" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="10">Accessibility</text>
      </g>
    </g>
  </g>

  <!-- Center Divider -->
  <line x1="460" y1="25" x2="460" y2="175" stroke="#10B981" stroke-opacity="0.15" stroke-width="1" stroke-dasharray="3 3"/>

  <!-- Right Quest: Operation Vault -->
  <g transform="translate(490, 28)">
    <rect x="0" y="0" width="70" height="22" rx="6" fill="#0d2b1f" stroke="#34D399" stroke-opacity="0.4"/>
    <text x="35" y="15" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700">QUEST 02</text>
    
    <text x="82" y="18" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="800">Operation Vault</text>
    <text x="215" y="17" fill="#34D399" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Induction Challenge</text>

    <text x="0" y="52" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">Mobile-first interactive crypto/logic puzzle game for the CSI induction event.</text>
    <text x="0" y="74" fill="#64748B" font-family="'Inter', sans-serif" font-size="12">Multi-tier cipher mechanics, rapid live event scoring, and puzzle gates.</text>

    <!-- Vault Dial Visual -->
    <g transform="translate(0, 95)">
      <circle cx="16" cy="14" r="14" stroke="#34D399" stroke-width="2" fill="#0d2a1e"/>
      <circle cx="16" cy="14" r="5" fill="#34D399"/>
      <line x1="16" y1="2" x2="16" y2="7" stroke="#34D399" stroke-width="2"/>
      <line x1="16" y1="21" x2="16" y2="26" stroke="#34D399" stroke-width="2"/>

      <g transform="translate(45, 4)">
        <rect x="0" y="0" width="94" height="24" rx="12" fill="#0d2a1e" stroke="#34D399" stroke-opacity="0.3"/>
        <text x="47" y="16" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="10">Mobile-First</text>

        <rect x="100" y="0" width="80" height="24" rx="12" fill="#0d2a1e" stroke="#34D399" stroke-opacity="0.3"/>
        <text x="140" y="16" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="10">CSI Event</text>

        <rect x="186" y="0" width="94" height="24" rx="12" fill="#0d2a1e" stroke="#34D399" stroke-opacity="0.3"/>
        <text x="233" y="16" text-anchor="middle" fill="#34D399" font-family="'Fira Code', monospace" font-size="10">Puzzle Logic</text>
      </g>
    </g>
  </g>
</svg>'''

    with open('assets/cards/side-quests.svg', 'w') as f:
        f.write(side_svg)

    # 7. SECTION HEADERS (NO "//", 100% VALID XML ESCAPING)
    headers = [
        ('header-about.svg', '01 • ABOUT &amp; ARCHITECTURAL DIRECTIVE', 'WHO I AM • HOW I DIRECT AI'),
        ('header-projects.svg', '02 • FEATURED SYSTEMS &amp; ENGINES', 'CORE ARCHITECTURES &amp; BUILDS'),
        ('header-stack.svg', '03 • ABSORBED CAPABILITIES', 'TECH STACK &amp; TOOLING ECOSYSTEM'),
        ('header-activations.svg', '04 • ACTIVE FREQUENCIES', 'COMMUNITY NODES &amp; ROLES'),
        ('header-telemetry.svg', '05 • REPO TELEMETRY &amp; METRICS', 'LIVE CONTRIBUTIONS &amp; METRICS')
    ]
    for filename, title, sub in headers:
        svg = f'''<svg width="920" height="46" viewBox="0 0 920 46" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="6" width="6" height="32" rx="3" fill="#10B981"/>
  <text x="18" y="28" fill="#34D399" font-family="'Inter', sans-serif" font-size="14" font-weight="800" letter-spacing="0.5">{title}</text>
  <text x="910" y="28" text-anchor="end" fill="#64748B" font-family="'Fira Code', monospace" font-size="11">{sub}</text>
  <line x1="18" y1="38" x2="920" y2="38" stroke="#10B981" stroke-opacity="0.2" stroke-width="1"/>
</svg>'''
        with open(f'assets/headers/{filename}', 'w') as f:
            f.write(svg)

    # 8. ASCII PORTRAIT TERMINAL
    if os.path.exists('picture.txt'):
        import xml.sax.saxutils as saxutils
        with open('picture.txt') as f:
            lines = f.readlines()
        escaped_lines = [saxutils.escape(l.rstrip('\n\r')) for l in lines]
        char_w = 4.8
        line_h = 8.2
        start_x = 28
        start_y = 65
        width = 920
        height = int(len(lines) * line_h + 85)

        svg_parts = [
            f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">',
            '  <defs>',
            '    <linearGradient id="termBg" x1="0" y1="0" x2="0" y2="1">',
            '      <stop offset="0%" stop-color="#050f0b"/>',
            '      <stop offset="100%" stop-color="#081711"/>',
            '    </linearGradient>',
            '    <linearGradient id="termBorder" x1="0" y1="0" x2="920" y2="920" gradientUnits="userSpaceOnUse">',
            '      <stop offset="0%" stop-color="#10B981" stop-opacity="0.7"/>',
            '      <stop offset="50%" stop-color="#34D399" stop-opacity="0.2"/>',
            '      <stop offset="100%" stop-color="#059669" stop-opacity="0.7"/>',
            '    </linearGradient>',
            '    <filter id="phosphorGlow" x="-10%" y="-10%" width="120%" height="120%">',
            '      <feGaussianBlur stdDeviation="0.6" result="blur"/>',
            '      <feMerge>',
            '        <feMergeNode in="blur"/>',
            '        <feMergeNode in="SourceGraphic"/>',
            '      </feMerge>',
            '    </filter>',
            '  </defs>',
            f'  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="14" fill="url(#termBg)" stroke="url(#termBorder)" stroke-width="1.5"/>',
            f'  <path d="M 1 14 C 1 6.82 6.82 1 14 1 L {width - 14} 1 C {width - 6.82} 1 {width - 1} 6.82 {width - 1} 14 L {width - 1} 38 L 1 38 Z" fill="#0a2218" fill-opacity="0.8"/>',
            f'  <line x1="1" y1="38" x2="{width - 1}" y2="38" stroke="#10B981" stroke-opacity="0.25" stroke-width="1"/>',
            '  <circle cx="22" cy="19" r="4.5" fill="#ef4444"/>',
            '  <circle cx="36" cy="19" r="4.5" fill="#eab308"/>',
            '  <circle cx="50" cy="19" r="4.5" fill="#22c55e"/>',
            '  <text x="72" y="23" fill="#94A3B8" font-family="\'Fira Code\', monospace" font-size="11" font-weight="600">shinz@asiet ~ cat portrait.ascii</text>',
            f'  <rect x="{width - 160}" y="9" width="145" height="20" rx="4" fill="#05150e" stroke="#10B981" stroke-opacity="0.3"/>',
            f'  <text x="{width - 88}" y="23" text-anchor="middle" fill="#34D399" font-family="\'Fira Code\', monospace" font-size="10" font-weight="600">180 x 101 MATRIX</text>',
            f'  <g font-family="\'Courier New\', monospace" font-size="7.5px" font-weight="600" fill="#34D399" filter="url(#phosphorGlow)" xml:space="preserve">'
        ]
        for i, l in enumerate(escaped_lines):
            y = start_y + i * line_h
            svg_parts.append(f'    <text x="{start_x}" y="{y:.1f}">{l}</text>')
        svg_parts.append('  </g>')
        svg_parts.append('</svg>')

        with open('assets/ascii-portrait.svg', 'w') as out:
            out.write('\n'.join(svg_parts))
        print("Generated assets/ascii-portrait.svg")

    print("All assets generated successfully!")

if __name__ == '__main__':
    generate_all()
