import os
import math

output_dir = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(output_dir, exist_ok=True)

# 1. Generate 3d-orbital-constellation.svg
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

  <!-- 3D Perspective Grid Background -->
  <g opacity="0.15" stroke="#00D4FF" stroke-width="0.8">
    <line x1="0" y1="260" x2="1000" y2="260" />
    <line x1="0" y1="290" x2="1000" y2="290" />
    <line x1="100" y1="200" x2="0" y2="320" />
    <line x1="300" y1="200" x2="200" y2="320" />
    <line x1="500" y1="200" x2="500" y2="320" />
    <line x1="700" y1="200" x2="800" y2="320" />
    <line x1="900" y1="200" x2="1000" y2="320" />
  </g>

  <!-- Title & Status Header -->
  <text x="30" y="35" font-family="'Courier New', monospace" font-weight="bold" fill="#00D4FF" font-size="14" letter-spacing="2">3D_ORBITAL_SWARM_TOPOLOGY // SATELLITE &amp; DRONE MESH</text>
  <text x="970" y="35" font-family="'Courier New', monospace" fill="#00F5D4" font-size="12" text-anchor="end">[LATENCY: 0.4ms] [NODES: 24/24 SYNCED]</text>

  <!-- Central 3D Earth Node -->
  <g transform="translate(500, 160)">
    <!-- Earth Sphere Glow -->
    <circle cx="0" cy="0" r="45" fill="url(#earthGrad)" filter="url(#glow3d)" opacity="0.9"/>
    <circle cx="0" cy="0" r="45" fill="none" stroke="#00D4FF" stroke-width="1.5" opacity="0.8"/>
    <text x="0" y="5" font-family="monospace" font-weight="bold" fill="#FFFFFF" font-size="11" text-anchor="middle">EARTH NODE</text>
    <text x="0" y="20" font-family="monospace" fill="#00F5D4" font-size="9" text-anchor="middle">Samsung R&amp;D Base</text>

    <!-- 3D Orbit Ring 1 (LEO Satellites - Horizontal Ellipse) -->
    <ellipse cx="0" cy="0" rx="260" ry="70" class="orbit-ring" transform="rotate(-15)"/>

    <!-- 3D Orbit Ring 2 (Drone Swarm - Vertical Ellipse) -->
    <ellipse cx="0" cy="0" rx="360" ry="95" class="orbit-ring" transform="rotate(25)"/>

    <!-- Satellite Nodes on Orbit 1 -->
    <g transform="rotate(-15)">
      <!-- Sat 1 -->
      <g transform="translate(-220, -35)">
        <circle cx="0" cy="0" r="8" fill="#00D4FF" filter="url(#glow3d)"/>
        <rect x="-16" y="-3" width="8" height="6" fill="#7B2CBF"/>
        <rect x="8" y="-3" width="8" height="6" fill="#7B2CBF"/>
        <text x="0" y="-14" class="node-text" text-anchor="middle">LEO-Sat Alpha</text>
      </g>
      <!-- Sat 2 -->
      <g transform="translate(210, 40)">
        <circle cx="0" cy="0" r="8" fill="#00F5D4" filter="url(#glow3d)"/>
        <rect x="-16" y="-3" width="8" height="6" fill="#00599C"/>
        <rect x="8" y="-3" width="8" height="6" fill="#00599C"/>
        <text x="0" y="22" class="node-text" text-anchor="middle">LEO-Sat Beta</text>
      </g>
    </g>

    <!-- Swarm Drone Nodes on Orbit 2 -->
    <g transform="rotate(25)">
      <!-- Drone Quadrotor 1 -->
      <g transform="translate(-300, 50)">
        <circle cx="0" cy="0" r="7" fill="#FF007F" filter="url(#glow3d)"/>
        <line x1="-12" y1="0" x2="12" y2="0" stroke="#FF007F" stroke-width="1.5"/>
        <line x1="0" y1="-12" x2="0" y2="12" stroke="#FF007F" stroke-width="1.5"/>
        <text x="0" y="20" class="node-text" text-anchor="middle">MARL Swarm Quad-1</text>
      </g>
      <!-- Drone Quadrotor 2 -->
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

# 2. Generate 3d-quantum-circuit.svg
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

  <!-- 3D Perspective Circuit Wires -->
  <g stroke="url(#qGrad)" stroke-width="2" opacity="0.8">
    <line x1="80" y1="80" x2="920" y2="80"/>
    <line x1="80" y1="130" x2="920" y2="130"/>
    <line x1="80" y1="180" x2="920" y2="180"/>
  </g>

  <!-- Qubit Labels -->
  <text x="40" y="84" font-family="monospace" fill="#00D4FF" font-size="13" font-weight="bold">|q0⟩</text>
  <text x="40" y="134" font-family="monospace" fill="#7B2CBF" font-size="13" font-weight="bold">|q1⟩</text>
  <text x="40" y="184" font-family="monospace" fill="#00F5D4" font-size="13" font-weight="bold">|q2⟩</text>

  <!-- Hadamard Gates -->
  <g transform="translate(180, 0)" filter="url(#qGlow)">
    <rect x="0" y="65" width="30" height="30" fill="#1E293B" stroke="#00D4FF" stroke-width="1.5" rx="4"/>
    <text x="15" y="85" font-family="sans-serif" fill="#00D4FF" font-size="14" font-weight="bold" text-anchor="middle">H</text>

    <rect x="0" y="115" width="30" height="30" fill="#1E293B" stroke="#7B2CBF" stroke-width="1.5" rx="4"/>
    <text x="15" y="135" font-family="sans-serif" fill="#7B2CBF" font-size="14" font-weight="bold" text-anchor="middle">H</text>
  </g>

  <!-- CNOT Entanglement Gate -->
  <g transform="translate(360, 0)" filter="url(#qGlow)">
    <line x1="15" y1="80" x2="15" y2="180" stroke="#00F5D4" stroke-width="2"/>
    <circle cx="15" cy="80" r="5" fill="#00F5D4"/>
    <circle cx="15" cy="180" r="10" fill="none" stroke="#00F5D4" stroke-width="2"/>
    <line x1="15" y1="173" x2="15" y2="187" stroke="#00F5D4" stroke-width="2"/>
    <line x1="8" y1="180" x2="22" y2="180" stroke="#00F5D4" stroke-width="2"/>
  </g>

  <!-- Parameterized Rotation Gates Rz(θ) -->
  <g transform="translate(540, 0)" filter="url(#qGlow)">
    <rect x="0" y="65" width="60" height="30" fill="#1E293B" stroke="#FF007F" stroke-width="1.5" rx="4"/>
    <text x="30" y="84" font-family="sans-serif" fill="#FF007F" font-size="11" font-weight="bold" text-anchor="middle">Rz(θ1)</text>

    <rect x="0" y="115" width="60" height="30" fill="#1E293B" stroke="#00D4FF" stroke-width="1.5" rx="4"/>
    <text x="30" y="134" font-family="sans-serif" fill="#00D4FF" font-size="11" font-weight="bold" text-anchor="middle">Ry(θ2)</text>

    <rect x="0" y="165" width="60" height="30" fill="#1E293B" stroke="#00F5D4" stroke-width="1.5" rx="4"/>
    <text x="30" y="184" font-family="sans-serif" fill="#00F5D4" font-size="11" font-weight="bold" text-anchor="middle">Rz(θ3)</text>
  </g>

  <!-- Measurement Meters -->
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

# 3. Generate living-orbital-pulse.svg
def generate_pulse():
    width = 1200
    height = 30
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" preserveAspectRatio="none">')
    lines.append('<defs>')
    lines.append('  <linearGradient id="cyanFlow" x1="0" y1="0" x2="1" y2="0">')
    lines.append('    <stop offset="0%" stop-color="#00D4FF"/>')
    lines.append('    <stop offset="25%" stop-color="#7B2CBF"/>')
    lines.append('    <stop offset="50%" stop-color="#00F5D4"/>')
    lines.append('    <stop offset="75%" stop-color="#FF007F"/>')
    lines.append('    <stop offset="100%" stop-color="#00D4FF"/>')
    lines.append('  </linearGradient>')
    lines.append('  <filter id="glow">')
    lines.append('    <feGaussianBlur stdDeviation="2.5" result="blur"/>')
    lines.append('    <feMerge>')
    lines.append('      <feMergeNode in="blur"/>')
    lines.append('      <feMergeNode in="blur"/>')
    lines.append('      <feMergeNode in="SourceGraphic"/>')
    lines.append('    </feMerge>')
    lines.append('  </filter>')
    lines.append('</defs>')
    lines.append('<style>')
    lines.append('  @keyframes particle { 0% { transform: translateX(-50px); opacity: 0; } 10% { opacity: 1; } 90% { opacity: 1; } 100% { transform: translateX(1250px); opacity: 0; } }')
    lines.append('  @keyframes pulse { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }')
    lines.append('</style>')
    mid = height / 2
    lines.append(f'<line x1="0" y1="{mid}" x2="{width}" y2="{mid}" stroke="url(#cyanFlow)" stroke-width="1.8" filter="url(#glow)" style="animation: pulse 3s ease-in-out infinite;"/>')
    colors = ['#00D4FF', '#00F5D4', '#7B2CBF', '#FF007F']
    for i in range(24):
        delay = i * 0.35
        dur = 4.0 + (i % 4) * 0.5
        y = mid + math.sin(i * 0.9) * 3.5
        c = colors[i % 4]
        lines.append(f'<circle cx="0" cy="{y:.1f}" r="1.5" fill="{c}" filter="url(#glow)" style="animation: particle {dur:.1f}s linear infinite {delay:.2f}s;"/>')
    lines.append('</svg>')
    filepath = os.path.join(output_dir, "living-orbital-pulse.svg")
    with open(filepath, "w") as f:
        f.write('\n'.join(lines))
    print(f"Generated {filepath}")

# 4. Generate orbital-hud.svg
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

# 5. Generate matrix-terminal.svg
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
    generate_3d_orbital()
    generate_3d_quantum()
    generate_pulse()
    generate_hud()
    generate_terminal()
