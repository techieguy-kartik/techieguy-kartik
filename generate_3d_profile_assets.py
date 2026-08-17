import os
import math

output_dir = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(output_dir, exist_ok=True)

# 1. Generate 3d-isometric-system-stack.svg
def generate_isometric_stack():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" width="100%">
  <defs>
    <linearGradient id="cardGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161B22" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#0D1117" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="neonCyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00D4FF"/>
      <stop offset="100%" stop-color="#00599C"/>
    </linearGradient>
    <linearGradient id="neonPurple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#A855F7"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="neonEmerald" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="neonPink" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EC4899"/>
      <stop offset="100%" stop-color="#8B5CF6"/>
    </linearGradient>

    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .bg-main { fill: #0B0E14; rx: 12px; stroke: #21262D; stroke-width: 1.5; }
    .header-tag { font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 13px; font-weight: 700; fill: #00D4FF; letter-spacing: 1.5px; }
    .header-sub { font-family: monospace; font-size: 11px; fill: #8B949E; }
    .card-box { rx: 10px; stroke-width: 1.5; fill: url(#cardGrad1); transition: all 0.3s ease; }
    .card-title { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 14px; font-weight: 700; }
    .item-text { font-family: monospace; font-size: 11px; fill: #C9D1D9; }
    .item-dim { font-family: monospace; font-size: 10px; fill: #8B949E; }
    .bus-line { stroke-dasharray: 4,4; animation: busFlow 2s linear infinite; }
    @keyframes busFlow { 0% { stroke-dashoffset: 16; } 100% { stroke-dashoffset: 0; } }
  </style>

  <rect width="100%" height="100%" class="bg-main"/>

  <text x="30" y="36" class="header-tag">SYSTEM_ARCHITECTURE // DISTRIBUTED AUTONOMOUS STACK</text>
  <text x="970" y="36" class="header-sub" text-anchor="end">[SAMSUNG R&amp;D • END-TO-END PIPELINE]</text>
  <line x1="30" y1="50" x2="970" y2="50" stroke="#21262D" stroke-width="1.5"/>

  <!-- Interconnect Bus Lines -->
  <line x1="240" y1="185" x2="270" y2="185" stroke="#00D4FF" stroke-width="2" class="bus-line"/>
  <line x1="480" y1="185" x2="510" y2="185" stroke="#A855F7" stroke-width="2" class="bus-line"/>
  <line x1="720" y1="185" x2="750" y2="185" stroke="#10B981" stroke-width="2" class="bus-line"/>

  <!-- ================= CARD 1: HARDWARE SILICON & CUDA ================= -->
  <g transform="translate(30, 70)">
    <rect width="210" height="260" class="card-box" stroke="#00D4FF" filter="url(#softGlow)"/>
    
    <g transform="translate(105, 45)">
      <polygon points="0,-18 36,0 0,18 -36,0" fill="url(#neonCyan)" opacity="0.8"/>
      <polygon points="-36,0 0,18 0,26 -36,8" fill="#00599C" opacity="0.9"/>
      <polygon points="36,0 0,18 0,26 36,8" fill="#00D4FF" opacity="0.6"/>
      <circle cx="0" cy="0" r="8" fill="#0D1117" stroke="#00D4FF" stroke-width="1.5"/>
      <text x="0" y="3.5" font-size="8" fill="#00D4FF" text-anchor="middle" font-family="monospace">⚡</text>
    </g>

    <text x="105" y="95" class="card-title" fill="#00D4FF" text-anchor="middle">Silicon &amp; CUDA</text>
    
    <rect x="55" y="105" width="100" height="18" fill="#0D1117" stroke="#00D4FF" rx="4"/>
    <text x="105" y="117" font-family="monospace" font-size="9" fill="#00D4FF" text-anchor="middle">GPU ACCELERATION</text>

    <line x1="20" y1="135" x2="190" y2="135" stroke="#21262D" stroke-width="1"/>

    <text x="20" y="160" class="item-text">• Triton Kernel Authoring</text>
    <text x="20" y="176" class="item-dim">  Custom memory hierarchy</text>

    <text x="20" y="202" class="item-text">• FlashAttention Engine</text>
    <text x="20" y="218" class="item-dim">  Nsight profiling &amp; PPA</text>

    <text x="20" y="244" class="item-text">• PyTorch &amp; C++20</text>
  </g>

  <!-- ================= CARD 2: QUANTUM COMPILER (DisCoCat) ================= -->
  <g transform="translate(270, 70)">
    <rect width="210" height="260" class="card-box" stroke="#A855F7" filter="url(#softGlow)"/>
    
    <g transform="translate(105, 45)">
      <polygon points="0,-18 36,0 0,18 -36,0" fill="url(#neonPurple)" opacity="0.8"/>
      <polygon points="-36,0 0,18 0,26 -36,8" fill="#6366F1" opacity="0.9"/>
      <polygon points="36,0 0,18 0,26 36,8" fill="#A855F7" opacity="0.6"/>
      <circle cx="0" cy="0" r="8" fill="#0D1117" stroke="#A855F7" stroke-width="1.5"/>
      <text x="0" y="3.5" font-size="8" fill="#A855F7" text-anchor="middle" font-family="monospace">⚛️</text>
    </g>

    <text x="105" y="95" class="card-title" fill="#A855F7" text-anchor="middle">Quantum NLP</text>
    
    <rect x="55" y="105" width="100" height="18" fill="#0D1117" stroke="#A855F7" rx="4"/>
    <text x="105" y="117" font-family="monospace" font-size="9" fill="#A855F7" text-anchor="middle">DISCOCAT COMPILER</text>

    <line x1="20" y1="135" x2="190" y2="135" stroke="#21262D" stroke-width="1"/>

    <text x="20" y="160" class="item-text">• Grammar ➔ NISQ Gates</text>
    <text x="20" y="176" class="item-dim">  Lambeq compositional AI</text>

    <text x="20" y="202" class="item-text">• Variational Classifiers</text>
    <text x="20" y="218" class="item-dim">  Parameterized circuits</text>

    <text x="20" y="244" class="item-text">• Qiskit &amp; PennyLane</text>
  </g>

  <!-- ================= CARD 3: SWARM MARL & 3DGS ROBOTICS ================= -->
  <g transform="translate(510, 70)">
    <rect width="210" height="260" class="card-box" stroke="#10B981" filter="url(#softGlow)"/>
    
    <g transform="translate(105, 45)">
      <polygon points="0,-18 36,0 0,18 -36,0" fill="url(#neonEmerald)" opacity="0.8"/>
      <polygon points="-36,0 0,18 0,26 -36,8" fill="#059669" opacity="0.9"/>
      <polygon points="36,0 0,18 0,26 36,8" fill="#10B981" opacity="0.6"/>
      <circle cx="0" cy="0" r="8" fill="#0D1117" stroke="#10B981" stroke-width="1.5"/>
      <text x="0" y="3.5" font-size="8" fill="#10B981" text-anchor="middle" font-family="monospace">🤖</text>
    </g>

    <text x="105" y="95" class="card-title" fill="#10B981" text-anchor="middle">Swarm Robotics</text>
    
    <rect x="55" y="105" width="100" height="18" fill="#0D1117" stroke="#10B981" rx="4"/>
    <text x="105" y="117" font-family="monospace" font-size="9" fill="#10B981" text-anchor="middle">EMBODIED SPATIAL</text>

    <line x1="20" y1="135" x2="190" y2="135" stroke="#21262D" stroke-width="1"/>

    <text x="20" y="160" class="item-text">• Attention CTDE Swarms</text>
    <text x="20" y="176" class="item-dim">  Quadrotors + UGVs MARL</text>

    <text x="20" y="202" class="item-text">• 3D Gaussian Splatting</text>
    <text x="20" y="218" class="item-dim">  Real-time Nav2 SLAM</text>

    <text x="20" y="244" class="item-text">• ROS2 &amp; Mesh Routing</text>
  </g>

  <!-- ================= CARD 4: SPACE-GRADE ORBITAL AI ================= -->
  <g transform="translate(750, 70)">
    <rect width="210" height="260" class="card-box" stroke="#EC4899" filter="url(#softGlow)"/>
    
    <g transform="translate(105, 45)">
      <polygon points="0,-18 36,0 0,18 -36,0" fill="url(#neonPink)" opacity="0.8"/>
      <polygon points="-36,0 0,18 0,26 -36,8" fill="#8B5CF6" opacity="0.9"/>
      <polygon points="36,0 0,18 0,26 36,8" fill="#EC4899" opacity="0.6"/>
      <circle cx="0" cy="0" r="8" fill="#0D1117" stroke="#EC4899" stroke-width="1.5"/>
      <text x="0" y="3.5" font-size="8" fill="#EC4899" text-anchor="middle" font-family="monospace">🛰️</text>
    </g>

    <text x="105" y="95" class="card-title" fill="#EC4899" text-anchor="middle">Orbital Edge AI</text>
    
    <rect x="55" y="105" width="100" height="18" fill="#0D1117" stroke="#EC4899" rx="4"/>
    <text x="105" y="117" font-family="monospace" font-size="9" fill="#EC4899" text-anchor="middle">LEO FEDERATED</text>

    <line x1="20" y1="135" x2="190" y2="135" stroke="#21262D" stroke-width="1"/>

    <text x="20" y="160" class="item-text">• LEO Constellations</text>
    <text x="20" y="176" class="item-dim">  Continual online learning</text>

    <text x="20" y="202" class="item-text">• Delta-Weight Transfers</text>
    <text x="20" y="218" class="item-dim">  Zero-latency sync</text>

    <text x="20" y="244" class="item-text">• Space-Grade Inference</text>
  </g>
</svg>'''
    filepath = os.path.join(output_dir, "3d-isometric-system-stack.svg")
    with open(filepath, "w") as f:
        f.write(svg)
    print(f"Generated {filepath}")
    filepath = os.path.join(output_dir, "3d-isometric-system-stack.svg")
    with open(filepath, "w") as f:
        f.write(svg)
    print(f"Generated {filepath}")

# 2. Generate quantum-bloch-radar.svg
def generate_bloch_radar():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="100%">
  <defs>
    <linearGradient id="radarSweep" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#00D4FF" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="blochGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7B2CBF"/>
      <stop offset="50%" stop-color="#FF007F"/>
      <stop offset="100%" stop-color="#00F5D4"/>
    </linearGradient>
    <filter id="radarGlow">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .radar-bg { fill: #0B0E14; rx: 12px; stroke: #1E293B; stroke-width: 1.5; }
    .hud-title { font-family: 'Courier New', monospace; font-weight: bold; fill: #00D4FF; font-size: 14px; letter-spacing: 2px; }
    .hud-sub { font-family: monospace; font-size: 11px; fill: #94A3B8; }
    .dial-title { font-family: 'Segoe UI', monospace; font-weight: 700; font-size: 13px; fill: #E2E8F0; }
    
    @keyframes radarSpin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    @keyframes pingNode {
      0%, 100% { r: 4; opacity: 0.3; }
      50% { r: 7; opacity: 1; }
    }
    @keyframes vectorPrecession {
      0% { transform: rotate(0deg); }
      50% { transform: rotate(45deg); }
      100% { transform: rotate(0deg); }
    }
  </style>

  <rect width="100%" height="100%" class="radar-bg"/>

  <text x="30" y="35" class="hud-title">REAL-TIME TELEMETRY // ORBITAL RADAR &amp; QUANTUM STATE VECTOR</text>
  <text x="970" y="35" font-family="monospace" fill="#00F5D4" font-size="12" text-anchor="end">STATUS: CONTINUOUS RECURSIVE SYNC</text>
  <line x1="30" y1="48" x2="970" y2="48" stroke="#1E293B" stroke-width="1.5"/>

  <!-- ================= LEFT PANEL: ORBITAL SWARM RADAR ================= -->
  <g transform="translate(250, 170)">
    <!-- Radar Rings -->
    <circle cx="0" cy="0" r="95" fill="#0D1117" stroke="#1E293B" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="70" fill="none" stroke="#1E293B" stroke-width="1" stroke-dasharray="3,3"/>
    <circle cx="0" cy="0" r="45" fill="none" stroke="#1E293B" stroke-width="1"/>
    <circle cx="0" cy="0" r="20" fill="none" stroke="#00D4FF" stroke-width="1" opacity="0.4"/>

    <!-- Crosshairs -->
    <line x1="-95" y1="0" x2="95" y2="0" stroke="#1E293B" stroke-width="1"/>
    <line x1="0" y1="-95" x2="0" y2="95" stroke="#1E293B" stroke-width="1"/>

    <!-- Rotating Radar Sweep -->
    <g style="transform-origin: 0px 0px; animation: radarSpin 4s linear infinite;">
      <path d="M 0 0 L 95 0 A 95 95 0 0 1 0 95 Z" fill="url(#radarSweep)" opacity="0.4"/>
      <line x1="0" y1="0" x2="95" y2="0" stroke="#00D4FF" stroke-width="1.5" filter="url(#radarGlow)"/>
    </g>

    <!-- Radar Target Nodes -->
    <circle cx="45" cy="-35" r="4" fill="#00F5D4" filter="url(#radarGlow)">
      <animate attributeName="opacity" values="0.2;1;0.2" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="54" y="-32" font-family="monospace" font-size="9" fill="#00F5D4">LEO-Sat 01</text>

    <circle cx="-50" cy="40" r="4" fill="#FF007F" filter="url(#radarGlow)">
      <animate attributeName="opacity" values="1;0.2;1" dur="2.5s" repeatCount="indefinite"/>
    </circle>
    <text x="-90" y="55" font-family="monospace" font-size="9" fill="#FF007F">Drone-Swarm α</text>

    <circle cx="20" cy="60" r="4" fill="#00D4FF" filter="url(#radarGlow)">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="1.8s" repeatCount="indefinite"/>
    </circle>

    <!-- Central Base -->
    <circle cx="0" cy="0" r="4" fill="#FFFFFF" filter="url(#radarGlow)"/>
  </g>

  <!-- Left Panel Labels -->
  <text x="140" y="75" class="dial-title">🛰️ Autonomous Swarm Radar</text>
  <text x="140" y="280" class="hud-sub">Track: 12 Quadrotors + 4 Satellites</text>

  <!-- Divider Line Between Panels -->
  <line x1="500" y1="65" x2="500" y2="280" stroke="#1E293B" stroke-width="1.5"/>

  <!-- ================= RIGHT PANEL: 3D QUANTUM BLOCH SPHERE ================= -->
  <g transform="translate(750, 170)">
    <!-- 3D Sphere Wireframe -->
    <circle cx="0" cy="0" r="90" fill="#0D1117" stroke="#7B2CBF" stroke-width="1.5" opacity="0.6"/>
    <!-- Equator Ellipse -->
    <ellipse cx="0" cy="0" rx="90" ry="30" fill="none" stroke="#FF007F" stroke-width="1.2" opacity="0.5" stroke-dasharray="4,3"/>
    <!-- Meridian Ellipse -->
    <ellipse cx="0" cy="0" rx="30" ry="90" fill="none" stroke="#00F5D4" stroke-width="1.2" opacity="0.5" stroke-dasharray="4,3"/>

    <!-- Axes -->
    <line x1="0" y1="-98" x2="0" y2="98" stroke="#94A3B8" stroke-width="1.2"/>
    <line x1="-98" y1="0" x2="98" y2="0" stroke="#94A3B8" stroke-width="1.2" opacity="0.5"/>

    <!-- Poles -->
    <text x="0" y="-104" font-family="monospace" font-size="11" font-weight="bold" fill="#00D4FF" text-anchor="middle">|0⟩ (Ground)</text>
    <text x="0" y="112" font-family="monospace" font-size="11" font-weight="bold" fill="#7B2CBF" text-anchor="middle">|1⟩ (Excited)</text>

    <!-- State Vector |ψ⟩ Precessing -->
    <g style="transform-origin: 0px 0px; animation: vectorPrecession 5s ease-in-out infinite;">
      <line x1="0" y1="0" x2="55" y2="-60" stroke="#00F5D4" stroke-width="2.5" filter="url(#radarGlow)"/>
      <polygon points="55,-60 44,-54 48,-46" fill="#00F5D4" filter="url(#radarGlow)"/>
      <circle cx="55" cy="-60" r="4" fill="#FFFFFF" filter="url(#radarGlow)"/>
    </g>
    <text x="70" y="-62" font-family="monospace" font-size="11" font-weight="bold" fill="#00F5D4">|ψ⟩ State</text>
  </g>

  <!-- Right Panel Labels -->
  <text x="640" y="75" class="dial-title">⚛️ Qubit Bloch Sphere State</text>
  <text x="640" y="280" class="hud-sub">State: |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩</text>
</svg>'''
    filepath = os.path.join(output_dir, "quantum-bloch-radar.svg")
    with open(filepath, "w") as f:
        f.write(svg)
    print(f"Generated {filepath}")

# 3. Generate holographic-skill-matrix.svg
def generate_skill_matrix():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" width="100%">
  <defs>
    <linearGradient id="neonBar1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00D4FF"/>
      <stop offset="100%" stop-color="#00F5D4"/>
    </linearGradient>
    <linearGradient id="neonBar2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7B2CBF"/>
      <stop offset="100%" stop-color="#FF007F"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#131B2E" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0B0E14" stop-opacity="0.9"/>
    </linearGradient>
    <filter id="skillGlow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .matrix-bg { fill: #0B0E14; rx: 12px; stroke: #1E293B; stroke-width: 1.5; }
    .matrix-title { font-family: 'Courier New', monospace; font-weight: bold; fill: #00D4FF; font-size: 14px; letter-spacing: 2px; }
    .card { fill: url(#cardGrad); rx: 8px; stroke: #1E293B; stroke-width: 1.2; }
    .quad-title { font-family: 'Segoe UI', sans-serif; font-weight: 700; font-size: 13px; }
    .skill-name { font-family: monospace; font-size: 11px; fill: #E2E8F0; }
    .bar-bg { fill: #1E293B; rx: 4px; }
    .bar-fill { rx: 4px; }
    .status-pill { font-family: monospace; font-size: 9px; font-weight: bold; fill: #00F5D4; }
  </style>

  <rect width="100%" height="100%" class="matrix-bg"/>

  <text x="30" y="35" class="matrix-title">CORE_CAPABILITY_MATRIX // ACCELERATION &amp; AUTONOMOUS SYSTEMS</text>
  <text x="970" y="35" font-family="monospace" fill="#00F5D4" font-size="12" text-anchor="end">SAMSUNG R&amp;D BENCHMARK</text>
  <line x1="30" y1="48" x2="970" y2="48" stroke="#1E293B" stroke-width="1.5"/>

  <!-- ================= QUADRANT 1: HARDWARE & KERNELS ================= -->
  <g transform="translate(30, 65)">
    <rect width="455" height="130" class="card" stroke="#76B900"/>
    <text x="20" y="28" class="quad-title" fill="#76B900">⚡ GPU Kernels &amp; Hardware Acceleration</text>
    <rect x="360" y="15" width="75" height="18" fill="#1E293B" rx="9" stroke="#76B900"/>
    <text x="397" y="27" class="status-pill" fill="#76B900" text-anchor="middle">OPTIMIZED</text>

    <!-- Skill 1 -->
    <text x="20" y="60" class="skill-name">CUDA C++ / Triton Kernel Authoring</text>
    <rect x="20" y="68" width="415" height="8" class="bar-bg"/>
    <rect x="20" y="68" width="395" height="8" fill="url(#neonBar1)" class="bar-fill" filter="url(#skillGlow)"/>

    <!-- Skill 2 -->
    <text x="20" y="100" class="skill-name">FlashAttention &amp; GPU Memory Hierarchy</text>
    <rect x="20" y="108" width="415" height="8" class="bar-bg"/>
    <rect x="20" y="108" width="380" height="8" fill="url(#neonBar1)" class="bar-fill" filter="url(#skillGlow)"/>
  </g>

  <!-- ================= QUADRANT 2: AUTONOMOUS & SWARM ================= -->
  <g transform="translate(515, 65)">
    <rect width="455" height="130" class="card" stroke="#00D4FF"/>
    <text x="20" y="28" class="quad-title" fill="#00D4FF">🤖 Autonomous AI &amp; Swarm Intelligence</text>
    <rect x="360" y="15" width="75" height="18" fill="#1E293B" rx="9" stroke="#00D4FF"/>
    <text x="397" y="27" class="status-pill" fill="#00D4FF" text-anchor="middle">ACTIVE R&amp;D</text>

    <!-- Skill 1 -->
    <text x="20" y="60" class="skill-name">Multi-Agent RL (CTDE Attention Swarms)</text>
    <rect x="20" y="68" width="415" height="8" class="bar-bg"/>
    <rect x="20" y="68" width="390" height="8" fill="url(#neonBar1)" class="bar-fill" filter="url(#skillGlow)"/>

    <!-- Skill 2 -->
    <text x="20" y="100" class="skill-name">3D Gaussian Splatting (3DGS) &amp; Nav2 SLAM</text>
    <rect x="20" y="108" width="415" height="8" class="bar-bg"/>
    <rect x="20" y="108" width="370" height="8" fill="url(#neonBar1)" class="bar-fill" filter="url(#skillGlow)"/>
  </g>

  <!-- ================= QUADRANT 3: SPACE-GRADE EDGE AI ================= -->
  <g transform="translate(30, 210)">
    <rect width="455" height="130" class="card" stroke="#00F5D4"/>
    <text x="20" y="28" class="quad-title" fill="#00F5D4">🛰️ Space-Grade Orbital &amp; Federated AI</text>
    <rect x="360" y="15" width="75" height="18" fill="#1E293B" rx="9" stroke="#00F5D4"/>
    <text x="397" y="27" class="status-pill" fill="#00F5D4" text-anchor="middle">DEPLOYED</text>

    <!-- Skill 1 -->
    <text x="20" y="60" class="skill-name">LEO Satellite Continual Federated Learning</text>
    <rect x="20" y="68" width="415" height="8" class="bar-bg"/>
    <rect x="20" y="68" width="385" height="8" fill="url(#neonBar1)" class="bar-fill" filter="url(#skillGlow)"/>

    <!-- Skill 2 -->
    <text x="20" y="100" class="skill-name">Delta-Weight Sync &amp; Low-Power Inference</text>
    <rect x="20" y="108" width="415" height="8" class="bar-bg"/>
    <rect x="20" y="108" width="360" height="8" fill="url(#neonBar1)" class="bar-fill" filter="url(#skillGlow)"/>
  </g>

  <!-- ================= QUADRANT 4: QUANTUM COMPUTING ================= -->
  <g transform="translate(515, 210)">
    <rect width="455" height="130" class="card" stroke="#FF007F"/>
    <text x="20" y="28" class="quad-title" fill="#FF007F">⚛️ Quantum NLP &amp; DisCoCat NISQ Compilers</text>
    <rect x="360" y="15" width="75" height="18" fill="#1E293B" rx="9" stroke="#FF007F"/>
    <text x="397" y="27" class="status-pill" fill="#FF007F" text-anchor="middle">RESEARCH</text>

    <!-- Skill 1 -->
    <text x="20" y="60" class="skill-name">DisCoCat Grammar-to-Circuit Compilation</text>
    <rect x="20" y="68" width="415" height="8" class="bar-bg"/>
    <rect x="20" y="68" width="375" height="8" fill="url(#neonBar2)" class="bar-fill" filter="url(#skillGlow)"/>

    <!-- Skill 2 -->
    <text x="20" y="100" class="skill-name">Qiskit, PennyLane &amp; Variational Quantum Circuits</text>
    <rect x="20" y="108" width="415" height="8" class="bar-bg"/>
    <rect x="20" y="108" width="365" height="8" fill="url(#neonBar2)" class="bar-fill" filter="url(#skillGlow)"/>
  </g>
</svg>'''
    filepath = os.path.join(output_dir, "holographic-skill-matrix.svg")
    with open(filepath, "w") as f:
        f.write(svg)
    print(f"Generated {filepath}")

# 4. Generate cyber-living-wave.svg
def generate_cyber_wave():
    width = 1200
    height = 40
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" preserveAspectRatio="none">')
    lines.append('<defs>')
    lines.append('  <linearGradient id="cyberWaveGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    lines.append('    <stop offset="0%" stop-color="#00D4FF"/>')
    lines.append('    <stop offset="25%" stop-color="#7B2CBF"/>')
    lines.append('    <stop offset="50%" stop-color="#00F5D4"/>')
    lines.append('    <stop offset="75%" stop-color="#FF007F"/>')
    lines.append('    <stop offset="100%" stop-color="#00D4FF"/>')
    lines.append('  </linearGradient>')
    lines.append('  <filter id="waveGlow">')
    lines.append('    <feGaussianBlur stdDeviation="2.5" result="blur"/>')
    lines.append('    <feMerge>')
    lines.append('      <feMergeNode in="blur"/>')
    lines.append('      <feMergeNode in="SourceGraphic"/>')
    lines.append('    </feMerge>')
    lines.append('  </filter>')
    lines.append('</defs>')
    lines.append('<style>')
    lines.append('  @keyframes wavePulse { 0%, 100% { opacity: 0.35; } 50% { opacity: 0.95; } }')
    lines.append('  @keyframes flowParticle { 0% { transform: translateX(-40px); opacity: 0; } 10% { opacity: 1; } 90% { opacity: 1; } 100% { transform: translateX(1240px); opacity: 0; } }')
    lines.append('</style>')

    # Background wave line
    mid = height / 2
    path_d = f"M 0 {mid} Q 300 {mid-12} 600 {mid} T 1200 {mid}"
    lines.append(f'<path d="{path_d}" fill="none" stroke="url(#cyberWaveGrad)" stroke-width="2" filter="url(#waveGlow)" style="animation: wavePulse 3s ease-in-out infinite;"/>')

    # Floating photon particles
    colors = ['#00D4FF', '#00F5D4', '#7B2CBF', '#FF007F', '#76B900']
    for i in range(20):
        delay = i * 0.4
        dur = 3.8 + (i % 4) * 0.6
        y = mid + math.sin(i * 0.8) * 6
        c = colors[i % len(colors)]
        lines.append(f'<circle cx="0" cy="{y:.1f}" r="1.6" fill="{c}" filter="url(#waveGlow)" style="animation: flowParticle {dur:.1f}s linear infinite {delay:.2f}s;"/>')

    lines.append('</svg>')
    filepath = os.path.join(output_dir, "cyber-living-wave.svg")
    with open(filepath, "w") as f:
        f.write('\n'.join(lines))
    print(f"Generated {filepath}")

# Retain existing generators
def generate_3d_orbital():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 320" width="100%">
  <defs>
    <linearGradient id="orbitGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00D4FF"/>
      <stop offset="50%" stop-color="#7B2CBF"/>
      <stop offset="100%" stop-color="#00F5D4"/>
    </linearGradient>
    <linearGradient id="earthGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00599C"/>
      <stop offset="50%" stop-color="#00D4FF"/>
      <stop offset="100%" stop-color="#0B0E14"/>
    </linearGradient>
    <filter id="glow3d">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <style>
    .bg-3d { fill: #0B0E14; rx: 12px; stroke: #1E293B; stroke-width: 1.5; }
    .orbit-ring { fill: none; stroke: url(#orbitGrad1); stroke-width: 1.5; opacity: 0.6; stroke-dasharray: 6,4; }
    .node-text { font-family: monospace; font-size: 11px; fill: #E2E8F0; }
    @keyframes orbitRotate { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    @keyframes pulseNode { 0%, 100% { transform: scale(1); opacity: 0.8; } 50% { transform: scale(1.3); opacity: 1; } }
  </style>

  <rect width="100%" height="100%" class="bg-3d" />

  <g opacity="0.15" stroke="#00D4FF" stroke-width="0.8">
    <line x1="0" y1="260" x2="1000" y2="260" />
    <line x1="0" y1="290" x2="1000" y2="290" />
    <line x1="100" y1="200" x2="0" y2="320" />
    <line x1="300" y1="200" x2="200" y2="320" />
    <line x1="500" y1="200" x2="500" y2="320" />
    <line x1="700" y1="200" x2="800" y2="320" />
    <line x1="900" y1="200" x2="1000" y2="320" />
  </g>

  <text x="30" y="35" font-family="'Courier New', monospace" font-weight="bold" fill="#00D4FF" font-size="14" letter-spacing="2">3D_ORBITAL_SWARM_TOPOLOGY // SATELLITE &amp; DRONE MESH</text>
  <text x="970" y="35" font-family="'Courier New', monospace" fill="#00F5D4" font-size="12" text-anchor="end">[LATENCY: 0.4ms] [NODES: 24/24 SYNCED]</text>

  <g transform="translate(500, 160)">
    <circle cx="0" cy="0" r="45" fill="url(#earthGrad)" filter="url(#glow3d)" opacity="0.9"/>
    <circle cx="0" cy="0" r="45" fill="none" stroke="#00D4FF" stroke-width="1.5" opacity="0.8"/>
    <text x="0" y="5" font-family="monospace" font-weight="bold" fill="#FFFFFF" font-size="11" text-anchor="middle">EARTH NODE</text>
    <text x="0" y="20" font-family="monospace" fill="#00F5D4" font-size="9" text-anchor="middle">Samsung R&amp;D Base</text>

    <ellipse cx="0" cy="0" rx="260" ry="70" class="orbit-ring" transform="rotate(-15)"/>
    <ellipse cx="0" cy="0" rx="360" ry="95" class="orbit-ring" transform="rotate(25)"/>

    <g transform="rotate(-15)">
      <g transform="translate(-220, -35)">
        <circle cx="0" cy="0" r="8" fill="#00D4FF" filter="url(#glow3d)"/>
        <rect x="-16" y="-3" width="8" height="6" fill="#7B2CBF"/>
        <rect x="8" y="-3" width="8" height="6" fill="#7B2CBF"/>
        <text x="0" y="-14" class="node-text" text-anchor="middle">LEO-Sat Alpha</text>
      </g>
      <g transform="translate(210, 40)">
        <circle cx="0" cy="0" r="8" fill="#00F5D4" filter="url(#glow3d)"/>
        <rect x="-16" y="-3" width="8" height="6" fill="#00599C"/>
        <rect x="8" y="-3" width="8" height="6" fill="#00599C"/>
        <text x="0" y="22" class="node-text" text-anchor="middle">LEO-Sat Beta</text>
      </g>
    </g>

    <g transform="rotate(25)">
      <g transform="translate(-300, 50)">
        <circle cx="0" cy="0" r="7" fill="#FF007F" filter="url(#glow3d)"/>
        <line x1="-12" y1="0" x2="12" y2="0" stroke="#FF007F" stroke-width="1.5"/>
        <line x1="0" y1="-12" x2="0" y2="12" stroke="#FF007F" stroke-width="1.5"/>
        <text x="0" y="20" class="node-text" text-anchor="middle">MARL Swarm Quad-1</text>
      </g>
      <g transform="translate(310, -45)">
        <circle cx="0" cy="0" r="7" fill="#7B2CBF" filter="url(#glow3d)"/>
        <line x1="-12" y1="0" x2="12" y2="0" stroke="#7B2CBF" stroke-width="1.5"/>
        <line x1="0" y1="-12" x2="0" y2="12" stroke="#7B2CBF" stroke-width="1.5"/>
        <text x="0" y="-16" class="node-text" text-anchor="middle">MARL Swarm Quad-2</text>
      </g>
    </g>
  </g>
</svg>'''
    filepath = os.path.join(output_dir, "3d-orbital-constellation.svg")
    with open(filepath, "w") as f:
        f.write(svg)
    print(f"Generated {filepath}")

def generate_3d_quantum():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 240" width="100%">
  <defs>
    <linearGradient id="qGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7B2CBF"/>
      <stop offset="50%" stop-color="#00D4FF"/>
      <stop offset="100%" stop-color="#00F5D4"/>
    </linearGradient>
    <filter id="qGlow">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="#0B0E14" rx="12" stroke="#1E293B" stroke-width="1.5"/>

  <text x="30" y="35" font-family="'Courier New', monospace" font-weight="bold" fill="#7B2CBF" font-size="14" letter-spacing="2">3D_QUANTUM_DISCOCAT_COMPILER // GRAMMAR TO NISQ GATES</text>
  <text x="970" y="35" font-family="monospace" fill="#00D4FF" font-size="12" text-anchor="end">[QISKIT &amp; PENNYLANE ACCELERATED]</text>

  <g stroke="url(#qGrad)" stroke-width="2" opacity="0.8">
    <line x1="80" y1="80" x2="920" y2="80"/>
    <line x1="80" y1="130" x2="920" y2="130"/>
    <line x1="80" y1="180" x2="920" y2="180"/>
  </g>

  <text x="40" y="84" font-family="monospace" fill="#00D4FF" font-size="13" font-weight="bold">|q0⟩</text>
  <text x="40" y="134" font-family="monospace" fill="#7B2CBF" font-size="13" font-weight="bold">|q1⟩</text>
  <text x="40" y="184" font-family="monospace" fill="#00F5D4" font-size="13" font-weight="bold">|q2⟩</text>

  <g transform="translate(180, 0)" filter="url(#qGlow)">
    <rect x="0" y="65" width="30" height="30" fill="#1E293B" stroke="#00D4FF" stroke-width="1.5" rx="4"/>
    <text x="15" y="85" font-family="sans-serif" fill="#00D4FF" font-size="14" font-weight="bold" text-anchor="middle">H</text>

    <rect x="0" y="115" width="30" height="30" fill="#1E293B" stroke="#7B2CBF" stroke-width="1.5" rx="4"/>
    <text x="15" y="135" font-family="sans-serif" fill="#7B2CBF" font-size="14" font-weight="bold" text-anchor="middle">H</text>
  </g>

  <g transform="translate(360, 0)" filter="url(#qGlow)">
    <line x1="15" y1="80" x2="15" y2="180" stroke="#00F5D4" stroke-width="2"/>
    <circle cx="15" cy="80" r="5" fill="#00F5D4"/>
    <circle cx="15" cy="180" r="10" fill="none" stroke="#00F5D4" stroke-width="2"/>
    <line x1="15" y1="173" x2="15" y2="187" stroke="#00F5D4" stroke-width="2"/>
    <line x1="8" y1="180" x2="22" y2="180" stroke="#00F5D4" stroke-width="2"/>
  </g>

  <g transform="translate(540, 0)" filter="url(#qGlow)">
    <rect x="0" y="65" width="60" height="30" fill="#1E293B" stroke="#FF007F" stroke-width="1.5" rx="4"/>
    <text x="30" y="84" font-family="sans-serif" fill="#FF007F" font-size="11" font-weight="bold" text-anchor="middle">Rz(θ1)</text>

    <rect x="0" y="115" width="60" height="30" fill="#1E293B" stroke="#00D4FF" stroke-width="1.5" rx="4"/>
    <text x="30" y="134" font-family="sans-serif" fill="#00D4FF" font-size="11" font-weight="bold" text-anchor="middle">Ry(θ2)</text>

    <rect x="0" y="165" width="60" height="30" fill="#1E293B" stroke="#00F5D4" stroke-width="1.5" rx="4"/>
    <text x="30" y="184" font-family="sans-serif" fill="#00F5D4" font-size="11" font-weight="bold" text-anchor="middle">Rz(θ3)</text>
  </g>

  <g transform="translate(760, 0)">
    <rect x="0" y="65" width="30" height="30" fill="#0D1117" stroke="#94A3B8" stroke-width="1.5" rx="4"/>
    <path d="M 8 85 A 10 10 0 0 1 22 85" fill="none" stroke="#E2E8F0" stroke-width="1.5"/>
    <line x1="15" y1="85" x2="22" y2="73" stroke="#00F5D4" stroke-width="1.5"/>

    <rect x="0" y="115" width="30" height="30" fill="#0D1117" stroke="#94A3B8" stroke-width="1.5" rx="4"/>
    <path d="M 8 135 A 10 10 0 0 1 22 135" fill="none" stroke="#E2E8F0" stroke-width="1.5"/>
    <line x1="15" y1="135" x2="22" y2="123" stroke="#00F5D4" stroke-width="1.5"/>

    <rect x="0" y="165" width="30" height="30" fill="#0D1117" stroke="#94A3B8" stroke-width="1.5" rx="4"/>
    <path d="M 8 185 A 10 10 0 0 1 22 185" fill="none" stroke="#E2E8F0" stroke-width="1.5"/>
    <line x1="15" y1="185" x2="22" y2="173" stroke="#00F5D4" stroke-width="1.5"/>
  </g>
</svg>'''
    filepath = os.path.join(output_dir, "3d-quantum-circuit.svg")
    with open(filepath, "w") as f:
        f.write(svg)
    print(f"Generated {filepath}")

def generate_hud():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" width="100%">
  <defs>
    <linearGradient id="hudBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00D4FF"/>
      <stop offset="50%" stop-color="#7B2CBF"/>
      <stop offset="100%" stop-color="#00F5D4"/>
    </linearGradient>
    <filter id="hudGlow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <style>
    .bg { fill: #0B0E14; rx: 12px; stroke: url(#hudBorder); stroke-width: 2; }
    .text-title { font-family: 'Courier New', monospace; font-weight: bold; fill: #00D4FF; font-size: 16px; letter-spacing: 2px; }
    .text-val { font-family: 'Segoe UI', sans-serif; fill: #E2E8F0; font-size: 13px; }
    .text-dim { fill: #94A3B8; font-size: 11px; }
    .tag { fill: #1E293B; stroke: #00D4FF; stroke-width: 1; rx: 4px; }
    .tag-text { font-family: monospace; fill: #00F5D4; font-size: 11px; }
  </style>

  <rect width="100%" height="100%" class="bg" />

  <path d="M 15 35 L 15 15 L 35 15" stroke="#00D4FF" stroke-width="2" fill="none" />
  <path d="M 985 35 L 985 15 L 965 15" stroke="#00D4FF" stroke-width="2" fill="none" />
  <path d="M 15 245 L 15 265 L 35 265" stroke="#00D4FF" stroke-width="2" fill="none" />
  <path d="M 985 245 L 985 265 L 965 265" stroke="#00D4FF" stroke-width="2" fill="none" />

  <text x="35" y="45" class="text-title">SYSTEM_HUD // KARTIK ARORA [SAMSUNG R&amp;D]</text>
  <text x="965" y="45" class="text-title" text-anchor="end">STATUS: ACTIVE // ORBITAL DEPLOYED</text>
  <line x1="35" y1="58" x2="965" y2="58" stroke="#1E293B" stroke-width="1.5"/>

  <text x="40" y="90" fill="#7B2CBF" font-family="monospace" font-weight="bold" font-size="13">SYSTEM DOMAINS</text>
  
  <rect x="40" y="105" width="280" height="34" class="tag"/>
  <text x="50" y="126" class="tag-text">🛰️ LEO Satellite Federated AI</text>
  
  <rect x="40" y="148" width="280" height="34" class="tag"/>
  <text x="50" y="169" class="tag-text">🤖 Swarm MARL &amp; Drone Mesh</text>
  
  <rect x="40" y="191" width="280" height="34" class="tag"/>
  <text x="50" y="212" class="tag-text">⚛️ DisCoCat QNLP to NISQ Circuits</text>

  <text x="360" y="90" fill="#00D4FF" font-family="monospace" font-weight="bold" font-size="13">HARDWARE &amp; KERNEL STACK</text>

  <text x="360" y="118" class="text-val">⚡ CUDA &amp; Triton Kernel Optimization</text>
  <text x="360" y="136" class="text-dim">Flash Attention • Custom Memory Hierarchy Tuning</text>

  <text x="360" y="165" class="text-val">👁️ 3D Gaussian Splatting (3DGS)</text>
  <text x="360" y="183" class="text-dim">Real-time Robotic Localisation &amp; Nav2 Stack</text>

  <text x="360" y="212" class="text-val">💻 Quantum Simulators &amp; Frameworks</text>
  <text x="360" y="230" class="text-dim">Qiskit • PennyLane • Lambeq Grammar Mapping</text>

  <text x="700" y="90" fill="#00F5D4" font-family="monospace" font-weight="bold" font-size="13">RESEARCH TELEMETRY</text>

  <text x="700" y="118" class="text-val">Organization: <tspan fill="#00D4FF">Samsung R&amp;D India</tspan></text>
  <text x="700" y="145" class="text-val">Human-in-the-Loop: <tspan fill="#FF007F">0% (Autonomous)</tspan></text>
  <text x="700" y="172" class="text-val">Orchestration: <tspan fill="#00F5D4">Multi-Agent Swarm</tspan></text>

  <rect x="700" y="195" width="250" height="12" fill="#1E293B" rx="6"/>
  <rect x="700" y="195" width="220" height="12" fill="url(#hudBorder)" rx="6" filter="url(#hudGlow)"/>
  <text x="700" y="225" class="text-dim">Autonomous Convergence: 94.8%</text>

  <line x1="20" y1="20" x2="980" y2="20" stroke="#00D4FF" stroke-width="1" opacity="0.3">
    <animate attributeName="y1" values="20;260;20" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="y2" values="20;260;20" dur="6s" repeatCount="indefinite"/>
  </line>
</svg>'''
    filepath = os.path.join(output_dir, "orbital-hud.svg")
    with open(filepath, "w") as f:
        f.write(svg)
    print(f"Generated {filepath}")

def generate_terminal():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 240" width="100%">
  <rect width="100%" height="100%" fill="#0D1117" rx="8" stroke="#30363D" stroke-width="1"/>
  
  <circle cx="20" cy="20" r="6" fill="#FF5F56"/>
  <circle cx="40" cy="20" r="6" fill="#FFBD2E"/>
  <circle cx="60" cy="20" r="6" fill="#27C93F"/>
  <text x="450" y="24" fill="#8B949E" font-family="monospace" font-size="12" text-anchor="middle">kartik@samsung-rd-orbital:~</text>
  
  <line x1="0" y1="36" x2="900" y2="36" stroke="#21262D" stroke-width="1"/>
  
  <g font-family="'JetBrains Mono', 'Fira Code', monospace" font-size="13">
    <text x="20" y="65" fill="#58A6FF">kartik@samsung-rd:~$ <tspan fill="#E6EDE3">python3 -m kartik_arora.init --mode autonomous</tspan></text>

    <text x="20" y="95" fill="#7EE787">[SUCCESS]</text>
    <text x="110" y="95" fill="#C9D1D9">Identity Loaded: <tspan fill="#79C0FF">Kartik Arora | Software Engineer @ Samsung R&amp;D</tspan></text>

    <text x="20" y="125" fill="#7EE787">[ORBITAL]</text>
    <text x="110" y="125" fill="#C9D1D9">LEO Satellite Constellation: <tspan fill="#FFA657">Federated Weight-Delta Transfer Active</tspan></text>

    <text x="20" y="155" fill="#7EE787">[QUANTUM]</text>
    <text x="110" y="155" fill="#C9D1D9">DisCoCat Compiler: <tspan fill="#D2A8FF">Mapped to Parameterized NISQ Circuits</tspan></text>

    <text x="20" y="185" fill="#7EE787">[SWARM]</text>
    <text x="110" y="185" fill="#C9D1D9">Multi-Agent Coordination: <tspan fill="#FF7B72">Attention CTDE (Quadrotors + UGVs)</tspan></text>

    <text x="20" y="215" fill="#58A6FF">kartik@samsung-rd:~$ <tspan fill="#7EE787">_</tspan></text>
  </g>
</svg>'''
    filepath = os.path.join(output_dir, "matrix-terminal.svg")
    with open(filepath, "w") as f:
        f.write(svg)
    print(f"Generated {filepath}")

if __name__ == "__main__":
    generate_isometric_stack()
    generate_bloch_radar()
    generate_skill_matrix()
    generate_cyber_wave()
    generate_3d_orbital()
    generate_3d_quantum()
    generate_hud()
    generate_terminal()
