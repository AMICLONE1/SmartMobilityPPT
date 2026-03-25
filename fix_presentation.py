"""
Fix script for EV Workshop Day 4 Presentation:
1. Replace generic SVGs with context-accurate, detailed SVGs
2. Fix viewbox -> viewBox
3. Add "PowerNetPro Pvt. Ltd." top-right branding on every slide
4. Enhance interactivity (scroll animations, improved CSS)
5. Fix slide counter total
"""
import re

path = r"d:\EV_LAB\Smart Mobiltiy Session\SmartMobilityPPT\EV_Workshop_Day4_Presentation.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# ── 1. Fix viewbox -> viewBox ──
html = html.replace('viewbox=', 'viewBox=')

# ── 2. Add PowerNetPro Pvt. Ltd. branding CSS + top-right element ──
brand_css = """
.brand-tr{position:absolute;top:24px;right:36px;font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--cyan);letter-spacing:1.5px;opacity:.7;z-index:5;text-transform:uppercase}
.brand-tr::before{content:'';display:inline-block;width:8px;height:8px;background:var(--cyan);border-radius:50%;margin-right:8px;vertical-align:middle;box-shadow:0 0 8px var(--cyan)}
.slide{animation:slideIn .6s ease both}
@keyframes slideIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.reveal-step{opacity:1!important;transform:translateY(0)!important}
.card{transition:all .3s cubic-bezier(.4,0,.2,1)}
.card:hover{transform:translateY(-4px) scale(1.02);box-shadow:0 8px 32px rgba(0,0,0,.3)}
.eq{transition:all .3s;cursor:default}
.eq:hover{border-color:var(--cyan);box-shadow:0 0 20px rgba(0,212,255,.15);transform:scale(1.02)}
.note{transition:all .3s}
.note:hover{transform:translateX(4px)}
.stat:hover .stat-num{transform:scale(1.1);transition:transform .3s}
.stat-num{transition:transform .3s}
.sn{display:none}
"""
html = html.replace('</style>', brand_css + '</style>')

# ── 3. Insert brand element into every slide ──
html = re.sub(
    r'(<section\s+class="slide[^"]*"[^>]*>)',
    r'\1<div class="brand-tr">PowerNetPro Pvt. Ltd.</div>',
    html
)

# ── 4. Replace ALL generic SVGs with context-accurate ones ──
# Each SVG replacement maps the "Visual:" caption text to a proper SVG

svg_replacements = {}

# --- Energy flow infographic ---
svg_replacements['energy flow in an electric vehicle'] = '''<svg viewBox="0 0 420 180" style="width:100%;height:auto">
<defs><linearGradient id="gf1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#00e5a0"/><stop offset="1" stop-color="#00d4ff"/></linearGradient></defs>
<rect x="20" y="60" width="80" height="60" rx="10" fill="none" stroke="#00e5a0" stroke-width="2"/><text x="60" y="85" fill="#e8e6f0" font-size="11" text-anchor="middle" font-family="monospace">Battery</text><text x="60" y="100" fill="#9896a8" font-size="9" text-anchor="middle">⚡ 60 kWh</text>
<path d="M100 90 L155 90" stroke="url(#gf1)" stroke-width="3" fill="none"/><polygon points="155,90 148,85 148,95" fill="#00d4ff"/>
<rect x="160" y="60" width="80" height="60" rx="10" fill="none" stroke="#5b8cff" stroke-width="2"/><text x="200" y="85" fill="#e8e6f0" font-size="11" text-anchor="middle" font-family="monospace">Motor</text><text x="200" y="100" fill="#9896a8" font-size="9" text-anchor="middle">🔄 PMSM</text>
<path d="M240 90 L295 90" stroke="url(#gf1)" stroke-width="3" fill="none"/><polygon points="295,90 288,85 288,95" fill="#00d4ff"/>
<rect x="300" y="60" width="80" height="60" rx="10" fill="none" stroke="#f0c040" stroke-width="2"/><text x="340" y="85" fill="#e8e6f0" font-size="11" text-anchor="middle" font-family="monospace">Wheels</text><text x="340" y="100" fill="#9896a8" font-size="9" text-anchor="middle">🛞 Torque</text>
<path d="M300 130 C250 160, 150 160, 100 130" stroke="#00e5a0" stroke-width="2" stroke-dasharray="6 4" fill="none"/><polygon points="100,130 107,127 105,135" fill="#00e5a0"/>
<text x="200" y="155" fill="#00e5a0" font-size="10" text-anchor="middle" font-family="monospace">♻ Regenerative Braking</text>
</svg>'''

# --- MATLAB/Simulink screenshot ---
svg_replacements['MATLAB R2025b interface'] = '''<svg viewBox="0 0 420 160" style="width:100%;height:auto">
<rect x="10" y="10" width="400" height="140" rx="8" fill="#111118" stroke="#1e1e2a" stroke-width="2"/>
<rect x="10" y="10" width="400" height="22" rx="8" fill="#1c1c28"/>
<circle cx="28" cy="21" r="5" fill="#ff6b6b"/><circle cx="44" cy="21" r="5" fill="#f0c040"/><circle cx="60" cy="21" r="5" fill="#00e5a0"/>
<text x="200" y="24" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace">MATLAB R2025b — Simulink</text>
<rect x="30" y="50" width="70" height="35" rx="5" fill="none" stroke="#00e5a0" stroke-width="2"/><text x="65" y="72" fill="#e8e6f0" font-size="9" text-anchor="middle" font-family="monospace">Battery</text>
<path d="M100 67 L140 67" stroke="#5b8cff" stroke-width="2"/><polygon points="140,67 134,63 134,71" fill="#5b8cff"/>
<rect x="145" y="50" width="70" height="35" rx="5" fill="none" stroke="#00d4ff" stroke-width="2"/><text x="180" y="72" fill="#e8e6f0" font-size="9" text-anchor="middle" font-family="monospace">EKF</text>
<path d="M215 67 L255 67" stroke="#5b8cff" stroke-width="2"/><polygon points="255,67 249,63 249,71" fill="#5b8cff"/>
<rect x="260" y="50" width="70" height="35" rx="5" fill="none" stroke="#f0c040" stroke-width="2"/><text x="295" y="72" fill="#e8e6f0" font-size="9" text-anchor="middle" font-family="monospace">Scope</text>
<rect x="30" y="100" width="300" height="35" rx="5" fill="#16161f" stroke="#1e1e2a"/><path d="M40 125 L60 110 L80 120 L100 105 L120 118 L140 108 L160 115 L180 100 L200 112 L220 106 L240 110 L260 102 L280 108 L300 98 L320 105" fill="none" stroke="#00e5a0" stroke-width="2"/>
</svg>'''

# --- Fuel gauge analogy ---
svg_replacements['fuel gauge for ICE vehicle'] = '''<svg viewBox="0 0 420 180" style="width:100%;height:auto">
<text x="105" y="20" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">ICE: Simple</text>
<text x="315" y="20" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">EV: Complex</text>
<rect x="40" y="35" width="130" height="130" rx="12" fill="none" stroke="#1e1e2a" stroke-width="2"/>
<circle cx="105" cy="110" r="45" fill="none" stroke="#f0c040" stroke-width="3"/>
<path d="M75 140 L105 80" stroke="#ff6b6b" stroke-width="3" stroke-linecap="round"/>
<text x="105" y="150" fill="#f0c040" font-size="10" text-anchor="middle" font-family="monospace">Float Sensor</text>
<rect x="250" y="35" width="130" height="130" rx="12" fill="none" stroke="#1e1e2a" stroke-width="2"/>
<text x="315" y="65" fill="#00d4ff" font-size="10" text-anchor="middle" font-family="monospace">V(t) →</text>
<text x="315" y="85" fill="#00e5a0" font-size="10" text-anchor="middle" font-family="monospace">I(t) →</text>
<text x="315" y="105" fill="#ff6b6b" font-size="10" text-anchor="middle" font-family="monospace">T(t) →</text>
<rect x="275" y="115" width="80" height="25" rx="6" fill="none" stroke="#00d4ff" stroke-width="2"/><text x="315" y="132" fill="#00d4ff" font-size="9" text-anchor="middle" font-family="monospace">Algorithm</text>
<text x="315" y="160" fill="#00e5a0" font-size="10" text-anchor="middle" font-family="monospace">→ SOC %</text>
<path d="M190 100 L230 100" stroke="#5b8cff" stroke-width="2" stroke-dasharray="6"/><text x="210" y="95" fill="#5b8cff" font-size="12" text-anchor="middle">vs</text>
</svg>'''

# --- Li-ion cell cross-section ---
svg_replacements['Cross-section diagram of a lithium-ion cell'] = '''<svg viewBox="0 0 420 200" style="width:100%;height:auto">
<rect x="30" y="20" width="80" height="160" rx="4" fill="none" stroke="#5b8cff" stroke-width="2"/>
<text x="70" y="15" fill="#5b8cff" font-size="10" text-anchor="middle" font-family="monospace">Anode (−)</text>
<text x="70" y="105" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace">Graphite</text>
<rect x="130" y="20" width="40" height="160" rx="2" fill="none" stroke="#f0c040" stroke-width="1.5" stroke-dasharray="4"/>
<text x="150" y="15" fill="#f0c040" font-size="9" text-anchor="middle" font-family="monospace">Separator</text>
<rect x="190" y="20" width="80" height="160" rx="4" fill="none" stroke="#ff6b6b" stroke-width="2"/>
<text x="230" y="15" fill="#ff6b6b" font-size="10" text-anchor="middle" font-family="monospace">Cathode (+)</text>
<text x="230" y="105" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace">NMC</text>
<path d="M110 60 L170 60" stroke="#00e5a0" stroke-width="2" marker-end="url(#ah)"/><text x="140" y="55" fill="#00e5a0" font-size="8" text-anchor="middle">Li⁺</text>
<path d="M170 100 L110 100" stroke="#00d4ff" stroke-width="2" marker-end="url(#ah2)"/><text x="140" y="95" fill="#00d4ff" font-size="8" text-anchor="middle">Li⁺</text>
<text x="140" y="140" fill="#9896a8" font-size="9" text-anchor="middle">Electrolyte</text>
<text x="330" y="60" fill="#00e5a0" font-size="10" font-family="monospace">→ Charge</text>
<text x="330" y="100" fill="#00d4ff" font-size="10" font-family="monospace">← Discharge</text>
</svg>'''

# --- Capacity vs C-rate ---
svg_replacements['capacity vs C-rate'] = '''<svg viewBox="0 0 420 220" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">Capacity vs C-Rate at Different Temperatures</text>
<path d="M60 30 L60 190 L380 190" fill="none" stroke="#9896a8" stroke-width="2"/>
<text x="30" y="115" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace" transform="rotate(-90,30,115)">Capacity (Ah)</text>
<text x="220" y="210" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace">C-Rate</text>
<text x="100" y="200" fill="#9896a8" font-size="8" text-anchor="middle">0.5C</text><text x="180" y="200" fill="#9896a8" font-size="8" text-anchor="middle">1C</text><text x="260" y="200" fill="#9896a8" font-size="8" text-anchor="middle">2C</text><text x="340" y="200" fill="#9896a8" font-size="8" text-anchor="middle">4C</text>
<path d="M80 50 L160 55 L260 70 L360 100" fill="none" stroke="#ff6b6b" stroke-width="2.5"/><text x="370" y="100" fill="#ff6b6b" font-size="8">45°C</text>
<path d="M80 60 L160 68 L260 90 L360 130" fill="none" stroke="#00e5a0" stroke-width="2.5"/><text x="370" y="130" fill="#00e5a0" font-size="8">25°C</text>
<path d="M80 80 L160 100 L260 135 L360 170" fill="none" stroke="#5b8cff" stroke-width="2.5"/><text x="370" y="170" fill="#5b8cff" font-size="8">-10°C</text>
</svg>'''

# --- OCV vs SOC curve ---
svg_replacements['OCV vs SOC characteristic curve'] = '''<svg viewBox="0 0 420 220" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">OCV vs SOC — NMC Cell</text>
<path d="M60 30 L60 190 L380 190" fill="none" stroke="#9896a8" stroke-width="2"/>
<text x="30" y="115" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace" transform="rotate(-90,30,115)">OCV (V)</text>
<text x="220" y="210" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace">SOC (%)</text>
<text x="55" y="180" fill="#9896a8" font-size="8" text-anchor="end">3.0</text><text x="55" y="140" fill="#9896a8" font-size="8" text-anchor="end">3.3</text><text x="55" y="100" fill="#9896a8" font-size="8" text-anchor="end">3.6</text><text x="55" y="60" fill="#9896a8" font-size="8" text-anchor="end">3.9</text><text x="55" y="35" fill="#9896a8" font-size="8" text-anchor="end">4.2</text>
<text x="80" y="200" fill="#9896a8" font-size="8" text-anchor="middle">0</text><text x="160" y="200" fill="#9896a8" font-size="8" text-anchor="middle">25</text><text x="240" y="200" fill="#9896a8" font-size="8" text-anchor="middle">50</text><text x="320" y="200" fill="#9896a8" font-size="8" text-anchor="middle">75</text><text x="370" y="200" fill="#9896a8" font-size="8" text-anchor="middle">100</text>
<path d="M80 175 C100 170 120 155 150 140 C180 128 220 120 260 110 C300 90 340 55 370 35" fill="none" stroke="#00e5a0" stroke-width="3"/>
<text x="100" y="160" fill="#ff6b6b" font-size="8" font-style="italic">Steep</text>
<text x="220" y="105" fill="#f0c040" font-size="8" font-style="italic">Flat region</text>
<text x="350" y="45" fill="#ff6b6b" font-size="8" font-style="italic">Steep</text>
</svg>'''

# --- Pulse discharge test ---
svg_replacements['pulse discharge test'] = '''<svg viewBox="0 0 420 200" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">Voltage Response to Current Pulse</text>
<path d="M50 25 L50 180 L390 180" fill="none" stroke="#9896a8" stroke-width="2"/>
<text x="220" y="198" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace">Time (s)</text>
<path d="M60 60 L100 60 L100 85 L140 95 L200 100 L200 70 L240 58 L300 55 L300 55" fill="none" stroke="#00e5a0" stroke-width="2.5"/>
<path d="M100 85 L100 60" stroke="#ff6b6b" stroke-width="1.5" stroke-dasharray="4"/><text x="108" y="73" fill="#ff6b6b" font-size="8" font-family="monospace">R₀ drop</text>
<path d="M100 85 C130 92, 170 97, 200 100" stroke="#00d4ff" stroke-width="1" stroke-dasharray="4"/><text x="150" y="108" fill="#00d4ff" font-size="8" font-family="monospace">τ₁ decay</text>
<text x="250" y="50" fill="#00e5a0" font-size="8" font-family="monospace">Recovery</text>
</svg>'''

# --- OCV-SOC curves for multiple chemistries ---
svg_replacements['OCV-SOC curves overlaid'] = '''<svg viewBox="0 0 420 220" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">OCV-SOC Curves by Chemistry</text>
<path d="M60 30 L60 190 L380 190" fill="none" stroke="#9896a8" stroke-width="2"/>
<path d="M80 170 C120 160 200 110 280 80 C340 55 370 40 375 35" fill="none" stroke="#00e5a0" stroke-width="2.5"/><text x="378" y="35" fill="#00e5a0" font-size="8">NMC</text>
<path d="M80 155 C100 150 140 148 200 145 C260 142 300 140 340 120 C360 100 375 80 375 75" fill="none" stroke="#ff6b6b" stroke-width="2.5"/><text x="378" y="75" fill="#ff6b6b" font-size="8">LFP</text>
<path d="M80 165 C100 150 160 100 240 60 C300 38 360 30 375 28" fill="none" stroke="#5b8cff" stroke-width="2.5"/><text x="378" y="28" fill="#5b8cff" font-size="8">NCA</text>
<path d="M80 160 C140 155 200 152 260 148 C320 140 360 130 375 125" fill="none" stroke="#f0c040" stroke-width="2.5"/><text x="378" y="125" fill="#f0c040" font-size="8">LTO</text>
<rect x="80" y="140" width="250" height="15" rx="3" fill="rgba(255,107,107,0.08)" stroke="none"/><text x="205" y="150" fill="#ff6b6b" font-size="7" text-anchor="middle" opacity="0.6">LFP: Flat plateau → OCV unreliable</text>
</svg>'''

# --- GITT test ---
svg_replacements['GITT test profile'] = '''<svg viewBox="0 0 420 180" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="10" text-anchor="middle" font-family="monospace">GITT: Pulse + Rest → OCV Extraction</text>
<path d="M50 25 L50 165 L400 165" fill="none" stroke="#9896a8" stroke-width="1.5"/>
<path d="M70 100 L70 60 L110 60 L110 75 C120 85 140 88 150 90 L150 90 L150 55 L190 55 L190 68 C200 78 220 82 230 85 L230 85 L230 48 L270 48 L270 62 C280 72 300 77 310 80" fill="none" stroke="#00e5a0" stroke-width="2"/>
<path d="M70 150 L70 120 L110 120 L110 150 L150 150 L150 120 L190 120 L190 150 L230 150 L230 120 L270 120 L270 150 L310 150" fill="none" stroke="#5b8cff" stroke-width="1.5" opacity="0.6"/>
<text x="350" y="85" fill="#00e5a0" font-size="9" font-family="monospace">Voltage</text>
<text x="350" y="150" fill="#5b8cff" font-size="9" font-family="monospace">Current</text>
<text x="130" y="95" fill="#f0c040" font-size="7">OCV</text><text x="210" y="90" fill="#f0c040" font-size="7">OCV</text><text x="290" y="85" fill="#f0c040" font-size="7">OCV</text>
</svg>'''

# --- Hysteresis ---
svg_replacements['charge and discharge OCV curves'] = '''<svg viewBox="0 0 420 200" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">LFP Hysteresis: Charge vs Discharge OCV</text>
<path d="M60 30 L60 180 L380 180" fill="none" stroke="#9896a8" stroke-width="2"/>
<path d="M80 155 C140 150 200 145 280 143 C340 140 370 110 375 90" fill="none" stroke="#00e5a0" stroke-width="2.5"/><text x="378" y="90" fill="#00e5a0" font-size="8">Charge</text>
<path d="M80 165 C140 160 200 155 280 153 C340 150 370 120 375 100" fill="none" stroke="#00d4ff" stroke-width="2.5"/><text x="378" y="100" fill="#00d4ff" font-size="8">Discharge</text>
<path d="M200 145 L200 155" stroke="#ff6b6b" stroke-width="2"/><text x="210" y="142" fill="#ff6b6b" font-size="9" font-family="monospace">h(SOC)</text>
<path d="M200 145 L205 148" stroke="#ff6b6b" stroke-width="1.5"/><path d="M200 155 L205 152" stroke="#ff6b6b" stroke-width="1.5"/>
</svg>'''

# --- Drift over time ---
svg_replacements['True SOC (straight line) vs Coulomb Counting'] = '''<svg viewBox="0 0 420 220" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">Coulomb Counting Drift vs True SOC</text>
<path d="M60 30 L60 190 L380 190" fill="none" stroke="#9896a8" stroke-width="2"/>
<text x="220" y="210" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace">Time (hours)</text>
<path d="M80 40 L370 170" fill="none" stroke="#00e5a0" stroke-width="2.5"/><text x="375" y="170" fill="#00e5a0" font-size="8">True SOC</text>
<path d="M80 40 L370 170" fill="none" stroke="#5b8cff" stroke-width="2" stroke-dasharray="6"/><text x="375" y="163" fill="#5b8cff" font-size="7">0mA</text>
<path d="M80 40 L200 100 L370 150" fill="none" stroke="#f0c040" stroke-width="2"/><text x="375" y="150" fill="#f0c040" font-size="7">10mA</text>
<path d="M80 40 L200 85 L370 110" fill="none" stroke="#ff6b6b" stroke-width="2"/><text x="375" y="110" fill="#ff6b6b" font-size="7">50mA</text>
<path d="M80 40 L200 65 L370 60" fill="none" stroke="#ff6b6b" stroke-width="2.5" stroke-dasharray="4"/><text x="375" y="60" fill="#ff6b6b" font-size="7">100mA</text>
</svg>'''

# --- Predict + Correct diagram ---
svg_replacements['Predict'] = '''<svg viewBox="0 0 420 160" style="width:100%;height:auto">
<rect x="20" y="30" width="170" height="100" rx="12" fill="none" stroke="#5b8cff" stroke-width="2"/>
<text x="105" y="25" fill="#5b8cff" font-size="12" text-anchor="middle" font-family="monospace" font-weight="bold">PREDICT</text>
<text x="105" y="60" fill="#e8e6f0" font-size="10" text-anchor="middle">x̂⁻ = A·x̂ + B·u</text>
<text x="105" y="80" fill="#9896a8" font-size="9" text-anchor="middle">Coulomb counting</text>
<text x="105" y="100" fill="#9896a8" font-size="9" text-anchor="middle">+ V_RC model</text>
<text x="105" y="120" fill="#5b8cff" font-size="9" text-anchor="middle" font-style="italic">Model propagates</text>
<path d="M200 80 L225 80" stroke="#f0c040" stroke-width="3"/><polygon points="225,80 218,75 218,85" fill="#f0c040"/>
<rect x="235" y="30" width="170" height="100" rx="12" fill="none" stroke="#00e5a0" stroke-width="2"/>
<text x="320" y="25" fill="#00e5a0" font-size="12" text-anchor="middle" font-family="monospace" font-weight="bold">CORRECT</text>
<text x="320" y="60" fill="#e8e6f0" font-size="10" text-anchor="middle">x̂ = x̂⁻ + K·ỹ</text>
<text x="320" y="80" fill="#9896a8" font-size="9" text-anchor="middle">Voltage measurement</text>
<text x="320" y="100" fill="#9896a8" font-size="9" text-anchor="middle">corrects drift</text>
<text x="320" y="120" fill="#00e5a0" font-size="9" text-anchor="middle" font-style="italic">Measurement pulls back</text>
<path d="M320 133 C320 150 105 150 105 133" stroke="#00d4ff" stroke-width="2" stroke-dasharray="6"/><polygon points="105,133 100,140 110,140" fill="#00d4ff"/>
<text x="210" y="150" fill="#00d4ff" font-size="8" text-anchor="middle">Feedback Loop</text>
</svg>'''

# --- 1RC Thevenin circuit ---
svg_replacements['1RC Thevenin equivalent circuit'] = '''<svg viewBox="0 0 420 180" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">1RC Thevenin Equivalent Circuit</text>
<circle cx="60" cy="100" r="20" fill="none" stroke="#00e5a0" stroke-width="2"/><text x="60" y="95" fill="#00e5a0" font-size="8" text-anchor="middle">OCV</text><text x="60" y="107" fill="#00e5a0" font-size="7" text-anchor="middle">(SOC)</text>
<path d="M80 100 L120 100" stroke="#e8e6f0" stroke-width="2"/>
<rect x="120" y="85" width="50" height="30" rx="3" fill="none" stroke="#ff6b6b" stroke-width="2"/><text x="145" y="104" fill="#ff6b6b" font-size="9" text-anchor="middle" font-family="monospace">R₀</text>
<path d="M170 100 L200 100" stroke="#e8e6f0" stroke-width="2"/>
<rect x="200" y="70" width="50" height="25" rx="3" fill="none" stroke="#5b8cff" stroke-width="2"/><text x="225" y="87" fill="#5b8cff" font-size="9" text-anchor="middle" font-family="monospace">R₁</text>
<rect x="200" y="105" width="50" height="25" rx="3" fill="none" stroke="#f0c040" stroke-width="2"/><text x="225" y="122" fill="#f0c040" font-size="9" text-anchor="middle" font-family="monospace">C₁</text>
<path d="M200 95 L200 105" stroke="#e8e6f0" stroke-width="1.5"/><path d="M250 95 L250 105" stroke="#e8e6f0" stroke-width="1.5"/>
<path d="M250 100 L320 100" stroke="#e8e6f0" stroke-width="2"/>
<text x="320" y="95" fill="#00d4ff" font-size="10" font-family="monospace">V_term</text>
<text x="225" y="148" fill="#9896a8" font-size="8" text-anchor="middle">V_RC</text>
<path d="M225 130 L225 140" stroke="#9896a8" stroke-width="1" stroke-dasharray="3"/>
</svg>'''

# --- EKF convergence ---
svg_replacements['Three SOC curves'] = '''<svg viewBox="0 0 420 200" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">EKF Convergence from Wrong Initial SOC</text>
<path d="M50 25 L50 180 L390 180" fill="none" stroke="#9896a8" stroke-width="2"/>
<path d="M70 35 L380 160" fill="none" stroke="#00e5a0" stroke-width="2.5"/><text x="385" y="160" fill="#00e5a0" font-size="8">True</text>
<path d="M70 35 L380 160" fill="none" stroke="#5b8cff" stroke-width="2" stroke-dasharray="6"/><text x="385" y="153" fill="#5b8cff" font-size="7">CC</text>
<path d="M70 55 C100 50 130 43 160 42 L200 50 L250 70 L300 100 L350 140 L380 160" fill="none" stroke="#ff6b6b" stroke-width="2.5"/><text x="385" y="145" fill="#ff6b6b" font-size="8">EKF</text>
<text x="70" y="30" fill="#00e5a0" font-size="8">95%</text><text x="70" y="50" fill="#ff6b6b" font-size="8">90%</text>
<path d="M130 42 L130 38" stroke="#f0c040" stroke-width="1.5" stroke-dasharray="3"/><text x="145" y="35" fill="#f0c040" font-size="7">~200s convergence</text>
</svg>'''

# --- EKF vs CC proof ---
svg_replacements['Side-by-side comparison'] = '''<svg viewBox="0 0 420 180" style="width:100%;height:auto">
<text x="105" y="15" fill="#ff6b6b" font-size="10" text-anchor="middle" font-family="monospace">Coulomb Counting</text>
<text x="315" y="15" fill="#00e5a0" font-size="10" text-anchor="middle" font-family="monospace">EKF</text>
<rect x="15" y="25" width="190" height="140" rx="8" fill="none" stroke="#1e1e2a" stroke-width="1.5"/>
<path d="M30 35 L30 155 L195 155" fill="none" stroke="#9896a8" stroke-width="1"/>
<path d="M40 50 L180 140" fill="none" stroke="#00e5a0" stroke-width="1.5"/><path d="M40 50 L100 80 L180 120" fill="none" stroke="#ff6b6b" stroke-width="2"/>
<text x="150" y="100" fill="#ff6b6b" font-size="7">Drift!</text>
<rect x="215" y="25" width="190" height="140" rx="8" fill="none" stroke="#1e1e2a" stroke-width="1.5"/>
<path d="M230 35 L230 155 L395 155" fill="none" stroke="#9896a8" stroke-width="1"/>
<path d="M240 50 L380 140" fill="none" stroke="#00e5a0" stroke-width="1.5"/><path d="M240 65 C280 55 320 90 380 140" fill="none" stroke="#00d4ff" stroke-width="2"/>
<text x="320" y="75" fill="#00d4ff" font-size="7">Converges!</text>
</svg>'''

# --- ICE vs EV braking ---
svg_replacements['ICE car with red brake discs'] = '''<svg viewBox="0 0 420 180" style="width:100%;height:auto">
<text x="105" y="18" fill="#ff6b6b" font-size="11" text-anchor="middle" font-family="monospace">ICE: Energy → Heat</text>
<text x="315" y="18" fill="#00e5a0" font-size="11" text-anchor="middle" font-family="monospace">EV: Energy → Battery</text>
<rect x="30" y="30" width="150" height="130" rx="12" fill="none" stroke="#ff6b6b" stroke-width="2" stroke-dasharray="4"/>
<circle cx="80" cy="110" r="25" fill="none" stroke="#ff6b6b" stroke-width="3"/><text x="80" y="115" fill="#ff6b6b" font-size="20" text-anchor="middle">🔥</text>
<circle cx="140" cy="110" r="25" fill="none" stroke="#ff6b6b" stroke-width="3"/><text x="140" y="115" fill="#ff6b6b" font-size="20" text-anchor="middle">🔥</text>
<text x="105" y="65" fill="#9896a8" font-size="9" text-anchor="middle">Friction pads</text><text x="105" y="80" fill="#9896a8" font-size="9" text-anchor="middle">KE → Heat (lost)</text>
<rect x="240" y="30" width="150" height="130" rx="12" fill="none" stroke="#00e5a0" stroke-width="2" stroke-dasharray="4"/>
<circle cx="290" cy="110" r="25" fill="none" stroke="#00e5a0" stroke-width="3"/><text x="290" y="115" fill="#00e5a0" font-size="20" text-anchor="middle">⚡</text>
<circle cx="350" cy="110" r="25" fill="none" stroke="#00e5a0" stroke-width="3"/><text x="350" y="115" fill="#00e5a0" font-size="20" text-anchor="middle">🔋</text>
<path d="M315 110 L330 110" stroke="#00e5a0" stroke-width="2"/><polygon points="330,110 325,107 325,113" fill="#00e5a0"/>
<text x="315" y="65" fill="#9896a8" font-size="9" text-anchor="middle">Motor as generator</text><text x="315" y="80" fill="#9896a8" font-size="9" text-anchor="middle">KE → Electrical → Battery</text>
</svg>'''

# --- Free body diagram ---
svg_replacements['Free body diagram of car during braking'] = '''<svg viewBox="0 0 420 200" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">Free Body Diagram — Braking</text>
<rect x="100" y="80" width="220" height="40" rx="8" fill="none" stroke="#5b8cff" stroke-width="2"/>
<text x="210" y="105" fill="#e8e6f0" font-size="10" text-anchor="middle" font-family="monospace">Vehicle (m)</text>
<circle cx="140" cy="140" r="18" fill="none" stroke="#9896a8" stroke-width="2"/><circle cx="280" cy="140" r="18" fill="none" stroke="#9896a8" stroke-width="2"/>
<path d="M210 80 L210 50" stroke="#ff6b6b" stroke-width="2"/><polygon points="210,50 205,60 215,60" fill="#ff6b6b"/><text x="220" y="55" fill="#ff6b6b" font-size="8" font-family="monospace">CG</text>
<path d="M140 160 L140 185" stroke="#00e5a0" stroke-width="2"/><polygon points="140,185 135,178 145,178" fill="#00e5a0"/><text x="140" y="195" fill="#00e5a0" font-size="8" text-anchor="middle">N_front ↑</text>
<path d="M280 160 L280 185" stroke="#f0c040" stroke-width="2"/><polygon points="280,185 275,178 285,178" fill="#f0c040"/><text x="280" y="195" fill="#f0c040" font-size="8" text-anchor="middle">N_rear ↓</text>
<path d="M100 100 L60 100" stroke="#ff6b6b" stroke-width="2.5"/><polygon points="60,100 70,96 70,104" fill="#ff6b6b"/><text x="55" y="90" fill="#ff6b6b" font-size="8">Decel</text>
<path d="M160 70 L260 70" stroke="#00d4ff" stroke-width="1.5" stroke-dasharray="4"/><text x="210" y="68" fill="#00d4ff" font-size="7" text-anchor="middle">Weight transfer →</text>
</svg>'''

# --- Conventional vs regen damper ---
svg_replacements['conventional hydraulic damper'] = '''<svg viewBox="0 0 420 180" style="width:100%;height:auto">
<text x="105" y="18" fill="#ff6b6b" font-size="11" text-anchor="middle" font-family="monospace">Hydraulic Damper</text>
<text x="315" y="18" fill="#00e5a0" font-size="11" text-anchor="middle" font-family="monospace">EM Regen Damper</text>
<rect x="40" y="30" width="130" height="130" rx="10" fill="none" stroke="#ff6b6b" stroke-width="2"/>
<rect x="80" y="50" width="50" height="80" rx="4" fill="none" stroke="#ff6b6b" stroke-width="2"/>
<text x="105" y="95" fill="#ff6b6b" font-size="14" text-anchor="middle">🔥</text>
<text x="105" y="120" fill="#9896a8" font-size="8" text-anchor="middle">Heat (wasted)</text>
<text x="105" y="150" fill="#9896a8" font-size="8" text-anchor="middle">Vibration → Heat</text>
<rect x="250" y="30" width="130" height="130" rx="10" fill="none" stroke="#00e5a0" stroke-width="2"/>
<rect x="290" y="50" width="50" height="80" rx="4" fill="none" stroke="#00e5a0" stroke-width="2"/>
<text x="315" y="80" fill="#00e5a0" font-size="14" text-anchor="middle">⚡</text>
<path d="M315 100 L315 120 L355 120" stroke="#00e5a0" stroke-width="2"/><text x="365" y="124" fill="#00e5a0" font-size="9">🔋</text>
<text x="315" y="150" fill="#9896a8" font-size="8" text-anchor="middle">Vibration → Electricity</text>
</svg>'''

# --- Quarter-car model ---
svg_replacements['Quarter-car model diagram'] = '''<svg viewBox="0 0 420 240" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">Quarter-Car Suspension Model</text>
<rect x="155" y="30" width="110" height="45" rx="8" fill="none" stroke="#5b8cff" stroke-width="2"/><text x="210" y="57" fill="#e8e6f0" font-size="10" text-anchor="middle" font-family="monospace">m_s (body)</text>
<path d="M180 75 L180 115 M180 75 L195 85 L165 95 L195 105 L175 115" stroke="#00e5a0" stroke-width="2" fill="none"/><text x="155" y="100" fill="#00e5a0" font-size="8">k_s</text>
<rect x="225" y="80" width="20" height="32" rx="3" fill="none" stroke="#ff6b6b" stroke-width="2"/><text x="255" y="100" fill="#ff6b6b" font-size="8">c_eq</text>
<rect x="155" y="120" width="110" height="35" rx="8" fill="none" stroke="#f0c040" stroke-width="2"/><text x="210" y="142" fill="#e8e6f0" font-size="10" text-anchor="middle" font-family="monospace">m_u (wheel)</text>
<path d="M210 155 L210 195 M210 155 L225 165 L195 175 L225 185 L210 195" stroke="#00d4ff" stroke-width="2" fill="none"/><text x="235" y="180" fill="#00d4ff" font-size="8">k_t</text>
<path d="M140 210 L280 210" stroke="#9896a8" stroke-width="3"/><text x="210" y="228" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace">Road z_r(t)</text>
<path d="M160 210 C170 200 180 215 190 205 C200 195 210 210 220 205 C230 195 240 210 250 205 C260 198 270 210 280 210" stroke="#f0c040" stroke-width="1.5" fill="none"/>
</svg>'''

# --- Trade-off curve ---
svg_replacements['Trade-off curve'] = '''<svg viewBox="0 0 420 220" style="width:100%;height:auto">
<text x="210" y="15" fill="#9896a8" font-size="11" text-anchor="middle" font-family="monospace">Comfort vs Energy Trade-off</text>
<path d="M60 30 L60 190 L380 190" fill="none" stroke="#9896a8" stroke-width="2"/>
<text x="220" y="210" fill="#9896a8" font-size="9" text-anchor="middle" font-family="monospace">c_em (Ns/m)</text>
<path d="M80 170 C150 155 220 120 290 70 C330 45 360 35 375 30" fill="none" stroke="#00e5a0" stroke-width="2.5"/><text x="385" y="30" fill="#00e5a0" font-size="8">Power (W)</text>
<path d="M80 170 C130 165 180 155 230 135 C280 100 330 60 375 30" fill="none" stroke="#ff6b6b" stroke-width="2.5"/><text x="385" y="45" fill="#ff6b6b" font-size="8">a_rms</text>
<circle cx="240" cy="130" r="8" fill="none" stroke="#f0c040" stroke-width="2.5"/><text x="260" y="128" fill="#f0c040" font-size="9" font-weight="bold">Sweet Spot</text>
<path d="M240 138 L240 190" stroke="#f0c040" stroke-width="1" stroke-dasharray="4"/>
</svg>'''

# Now do the replacements by matching the "Visual:" caption text
def replace_svg_by_caption(html, key, new_svg):
    """Find the SVG container div that has a caption containing 'key', replace with new SVG."""
    # Pattern: find the whole container div that has a child div with matching caption
    pattern = re.compile(
        r'<div style="[^"]*min-height:220px[^"]*">\s*<svg[^>]*>.*?</svg>\s*<div[^>]*>Visual:\s*' + re.escape(key[:40]) + r'.*?</div>\s*</div>',
        re.DOTALL
    )
    new_container = f'<div style="width:100%; min-height:180px; background:var(--bg3); border:1px solid var(--border); border-radius:14px; position:relative; overflow:hidden; padding:16px; display:flex; flex-direction:column; justify-content:center; align-items:center;">{new_svg}</div>'
    result = pattern.sub(new_container, html)
    return result

for key, svg in svg_replacements.items():
    html = replace_svg_by_caption(html, key, svg)

# ── 5. Fix slide counter total ──
# Count actual slides
slide_count = len(re.findall(r'<section\s+class="slide', html))
html = re.sub(r'const total=\d+;', f'const total={slide_count};', html)
html = re.sub(r"159 Slides", f"{slide_count} Slides", html)

# ── 6. Write back ──
with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Done! Fixed {slide_count} slides.")
print("  - Fixed viewBox attribute casing")
print("  - Added top-right PowerNetPro Pvt. Ltd. branding")
print("  - Replaced generic SVGs with context-accurate diagrams")
print("  - Enhanced interactivity CSS")
print(f"  - Updated slide counter to {slide_count}")
