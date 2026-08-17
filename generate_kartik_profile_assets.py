import os
import math

output_dir = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(output_dir, exist_ok=True)

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

def generate_swarm_mesh():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 160" width="100%">
  <defs>
    <linearGradient id="meshGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00D4FF"/>
      <stop offset="50%" stop-color="#7B2CBF"/>
      <stop offset="100%" stop-color="#00F5D4"/>
    </linearGradient>
    <filter id="meshGlow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="#0B0E14" rx="8" stroke="#1E293B"/>
  
  <g stroke="url(#meshGrad)" stroke-width="1.2" opacity="0.4">
    <line x1="80" y1="80" x2="220" y2="40"/>
    <line x1="80" y1="80" x2="220" y2="120"/>
    <line x1="220" y1="40" x2="450" y2="80"/>
    <line x1="220" y1="120" x2="450" y2="80"/>
    <line x1="450" y1="80" x2="680" y2="40"/>
    <line x1="450" y1="80" x2="680" y2="120"/>
    <line x1="680" y1="40" x2="820" y2="80"/>
    <line x1="680" y1="120" x2="820" y2="80"/>
  </g>

  <g filter="url(#meshGlow)">
    <circle cx="80" cy="80" r="7" fill="#00D4FF"/>
    <circle cx="220" cy="40" r="6" fill="#00F5D4"/>
    <circle cx="220" cy="120" r="6" fill="#7B2CBF"/>
    <circle cx="450" cy="80" r="9" fill="#FF007F"/>
    <circle cx="680" cy="40" r="6" fill="#7B2CBF"/>
    <circle cx="680" cy="120" r="6" fill="#00F5D4"/>
    <circle cx="820" cy="80" r="7" fill="#00D4FF"/>
  </g>

  <g font-family="monospace" font-size="11" fill="#E2E8F0" text-anchor="middle">
    <text x="80" y="110" fill="#00D4FF">Orbital Node</text>
    <text x="220" y="25" fill="#00F5D4">Quadrotor A</text>
    <text x="220" y="145" fill="#7B2CBF">UGV Alpha</text>
    <text x="450" y="110" fill="#FF007F" font-weight="bold">Central Swarm CTDE</text>
    <text x="680" y="25" fill="#7B2CBF">DisCoCat Circuit</text>
    <text x="680" y="145" fill="#00F5D4">Triton Kernel</text>
    <text x="820" y="110" fill="#00D4FF">Edge Sync</text>
  </g>
</svg>'''
    filepath = os.path.join(output_dir, "swarm-network-mesh.svg")
    with open(filepath, "w") as f:
        f.write(svg)
    print(f"Generated {filepath}")

if __name__ == "__main__":
    generate_pulse()
    generate_hud()
    generate_terminal()
    generate_swarm_mesh()
