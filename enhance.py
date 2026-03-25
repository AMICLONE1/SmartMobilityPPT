#!/usr/bin/env python3
"""Add interactive enhancements: TOC slide, quiz slides, animated SVGs, quiz JS"""

filepath = r"d:\EV_LAB\Smart Mobiltiy Session\SmartMobilityPPT\EV_Workshop_Day4_Presentation.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ═══════════════════════════════════════════════
# 1. ADD CSS — before </style>
# ═══════════════════════════════════════════════
new_css = """
    /* ── TOC Slide ── */
    .toc-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; max-width:1000px; margin:32px auto 0; }
    .toc-card { background:var(--bg3); border:1px solid var(--border); border-radius:16px; padding:28px 24px; cursor:pointer; transition:all .4s cubic-bezier(.4,0,.2,1); position:relative; overflow:hidden; text-decoration:none; color:var(--text); display:block; }
    .toc-card::before { content:''; position:absolute; inset:0; opacity:0; transition:opacity .4s; border-radius:16px; }
    .toc-card:hover { transform:translateY(-6px) scale(1.03); box-shadow:0 12px 40px rgba(0,0,0,.4); }
    .toc-card:hover::before { opacity:1; }
    .toc-card.toc-green::before { background:radial-gradient(circle at 50% 0%,rgba(0,229,160,.12),transparent 70%); }
    .toc-card.toc-green { border-top:3px solid var(--green); }
    .toc-card.toc-red::before { background:radial-gradient(circle at 50% 0%,rgba(255,107,107,.12),transparent 70%); }
    .toc-card.toc-red { border-top:3px solid var(--red); }
    .toc-card.toc-gold::before { background:radial-gradient(circle at 50% 0%,rgba(240,192,64,.12),transparent 70%); }
    .toc-card.toc-gold { border-top:3px solid var(--gold); }
    .toc-icon { font-size:32px; display:block; margin-bottom:12px; }
    .toc-chapter { font-family:'JetBrains Mono',monospace; font-size:10px; color:var(--muted); letter-spacing:2px; text-transform:uppercase; margin-bottom:6px; }
    .toc-title { font-family:'Playfair Display',serif; font-weight:700; font-size:18px; margin-bottom:8px; }
    .toc-desc { font-size:12px; color:var(--text2); line-height:1.5; }
    @media(max-width:900px){ .toc-grid{grid-template-columns:1fr 1fr;} }

    /* ── Quiz Slides ── */
    .quiz-q { font-family:'Playfair Display',serif; font-weight:700; font-size:18px; margin:16px 0 12px; color:var(--text); }
    .quiz-options { display:flex; flex-direction:column; gap:10px; max-width:600px; }
    .quiz-opt { background:var(--bg3); border:1px solid var(--border); border-radius:10px; padding:14px 20px; cursor:pointer; font-size:14px; color:var(--text2); transition:all .3s; display:flex; align-items:center; gap:12px; user-select:none; }
    .quiz-opt:hover { border-color:var(--cyan); background:var(--bg4); color:var(--text); }
    .quiz-opt .q-letter { width:28px; height:28px; border-radius:50%; background:var(--bg4); border:1px solid var(--border); display:flex; align-items:center; justify-content:center; font-family:'JetBrains Mono',monospace; font-size:12px; font-weight:600; color:var(--muted); flex-shrink:0; transition:all .3s; }
    .quiz-opt.correct { border-color:var(--green); background:rgba(0,229,160,.08); color:var(--text); }
    .quiz-opt.correct .q-letter { background:var(--green); color:var(--bg); border-color:var(--green); }
    .quiz-opt.wrong { border-color:var(--red); background:rgba(255,107,107,.06); opacity:.6; }
    .quiz-opt.wrong .q-letter { border-color:var(--red); color:var(--red); }
    .quiz-opt.answered { pointer-events:none; }
    .quiz-explain { display:none; margin-top:10px; padding:12px 16px; background:var(--bg3); border-left:3px solid var(--green); border-radius:0 8px 8px 0; font-size:13px; color:var(--text2); line-height:1.6; }
    .quiz-explain.show { display:block; animation:slideIn .3s ease both; }

    /* ── SVG Animations ── */
    @keyframes ionShuttle { 0%{transform:translateX(0)} 50%{transform:translateX(60px)} 100%{transform:translateX(0)} }
    @keyframes ionShuttleRev { 0%{transform:translateX(0)} 50%{transform:translateX(-60px)} 100%{transform:translateX(0)} }
    .ion-anim { animation: ionShuttle 3s ease-in-out infinite; }
    .ion-anim-rev { animation: ionShuttleRev 3s ease-in-out infinite; }
    @keyframes drawLine { from{stroke-dashoffset:500} to{stroke-dashoffset:0} }
    .svg-draw { stroke-dasharray:500; stroke-dashoffset:500; animation: drawLine 2s ease forwards; }
    .svg-draw-delay { stroke-dasharray:500; stroke-dashoffset:500; animation: drawLine 2s ease 0.8s forwards; }
    @keyframes fadeInUp { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }
    .svg-fade { opacity:0; animation: fadeInUp .5s ease 2s forwards; }
    .svg-fade-d2 { opacity:0; animation: fadeInUp .5s ease 2.5s forwards; }
    .svg-fade-d3 { opacity:0; animation: fadeInUp .5s ease 3s forwards; }
"""

content = content.replace('  </style>', new_css + '  </style>', 1)
print("1. CSS added")

# ═══════════════════════════════════════════════
# 2. INSERT TOC SLIDE
# ═══════════════════════════════════════════════
toc_slide = """
  <!-- TOC SLIDE -->
  <section class="slide" data-num="toc" data-section="intro" id="sTOC">
    <div class="brand-tr">PowerNetPro Pvt. Ltd.</div>
    <div class="sf">Omkar · EV Centre of Excellence, MIT-WPU | PowerNetPro Pvt.Ltd.</div>
    <span class="tag tag-intro">ROADMAP</span>
    <h2 class="st">Today's Journey</h2>
    <p class="ss">Click any section to jump directly. Use arrow keys to navigate sequentially.</p>
    <div class="toc-grid">
      <a href="#s15" class="toc-card toc-green" onclick="event.preventDefault();document.getElementById('s15').scrollIntoView({behavior:'smooth'})">
        <span class="toc-icon">🔋</span>
        <div class="toc-chapter">Chapters 1-2</div>
        <div class="toc-title">SOC Fundamentals</div>
        <div class="toc-desc">Cell chemistry, capacity, internal resistance, and why SOC matters.</div>
      </a>
      <a href="#s25" class="toc-card toc-green" onclick="event.preventDefault();document.getElementById('s25').scrollIntoView({behavior:'smooth'})">
        <span class="toc-icon">📈</span>
        <div class="toc-chapter">Chapter 3</div>
        <div class="toc-title">OCV Method</div>
        <div class="toc-desc">Low-rate discharge, GITT, polynomial fits, hysteresis correction.</div>
      </a>
      <a href="#s63" class="toc-card toc-green" onclick="event.preventDefault();document.getElementById('s63').scrollIntoView({behavior:'smooth'})">
        <span class="toc-icon">🎯</span>
        <div class="toc-chapter">Chapter 4</div>
        <div class="toc-title">Extended Kalman Filter</div>
        <div class="toc-desc">State-space modeling, EKF derivation, Simulink implementation.</div>
      </a>
      <a href="#s95" class="toc-card toc-red" onclick="event.preventDefault();document.getElementById('s95').scrollIntoView({behavior:'smooth'})">
        <span class="toc-icon">🚗</span>
        <div class="toc-chapter">Chapter 5</div>
        <div class="toc-title">Regen Braking</div>
        <div class="toc-desc">Free body diagrams, braking strategies, energy recovery limits.</div>
      </a>
      <a href="#s131" class="toc-card toc-red" onclick="event.preventDefault();document.getElementById('s131').scrollIntoView({behavior:'smooth'})">
        <span class="toc-icon">⚡</span>
        <div class="toc-chapter">Chapter 6</div>
        <div class="toc-title">Regen Damper</div>
        <div class="toc-desc">Quarter-car model, electromagnetic harvesting, impedance matching.</div>
      </a>
      <a href="#s149" class="toc-card toc-gold" onclick="event.preventDefault();document.getElementById('s149').scrollIntoView({behavior:'smooth'})">
        <span class="toc-icon">🔧</span>
        <div class="toc-chapter">Hands-On</div>
        <div class="toc-title">Lab &amp; Closing</div>
        <div class="toc-desc">Build Simulink models, compare strategies, Q&amp;A session.</div>
      </a>
    </div>
  </section>
"""

scroll_hint_pos = content.find('scroll-hint')
first_section_end = content.find('</section>', scroll_hint_pos)
content = content[:first_section_end + len('</section>')] + '\n' + toc_slide + content[first_section_end + len('</section>'):]
print("2. TOC slide inserted")

# ═══════════════════════════════════════════════
# 3. INSERT QUIZ A
# ═══════════════════════════════════════════════
quiz_a = """
  <!-- QUIZ A -->
  <section class="slide" data-num="quiz-a" data-section="soc-ekf" id="sQuizA">
    <div class="brand-tr">PowerNetPro Pvt. Ltd.</div>
    <div class="sf">Omkar · EV Centre of Excellence, MIT-WPU | PowerNetPro Pvt.Ltd.</div>
    <span class="tag tag-green">CHECKPOINT</span>
    <h2 class="st">Quick Quiz — SOC Estimation</h2>
    <p class="sb">Test your understanding before Part II. Click an option to check your answer.</p>
    <div class="merged-slide-container">
      <div class="merged-col">
        <div class="quiz-q">Q1: Why is OCV unreliable for LFP at mid-range SOC?</div>
        <div class="quiz-options" data-quiz="q1">
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">A</span>LFP cells have too high internal resistance</div>
          <div class="quiz-opt" data-correct="true" onclick="quizAnswer(this)"><span class="q-letter">B</span>The OCV-SOC curve is nearly flat from 20-80%</div>
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">C</span>LFP cannot be discharged below 20% SOC</div>
        </div>
        <div class="quiz-explain" data-for="q1">LFP has a flat voltage plateau (~3.2V) across mid-range, making it impossible to distinguish 30% from 70% SOC using voltage alone.</div>
        <div class="quiz-q">Q2: What causes Coulomb Counting drift?</div>
        <div class="quiz-options" data-quiz="q2">
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">A</span>Temperature changes in the battery</div>
          <div class="quiz-opt" data-correct="true" onclick="quizAnswer(this)"><span class="q-letter">B</span>Current sensor offset errors accumulate via integration</div>
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">C</span>The battery capacity changes every cycle</div>
        </div>
        <div class="quiz-explain" data-for="q2">Even a tiny offset (1mA) accumulates over hours of integration — the fundamental weakness of open-loop CC.</div>
      </div>
      <div class="merged-col">
        <div class="quiz-q">Q3: What makes EKF superior to Coulomb Counting?</div>
        <div class="quiz-options" data-quiz="q3">
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">A</span>It uses a more accurate current sensor</div>
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">B</span>It does not require any battery model</div>
          <div class="quiz-opt" data-correct="true" onclick="quizAnswer(this)"><span class="q-letter">C</span>It corrects drift by comparing predicted vs measured voltage</div>
        </div>
        <div class="quiz-explain" data-for="q3">The EKF predicts terminal voltage, compares with measurement, and uses the innovation to correct drift via the Kalman gain.</div>
        <div class="note note-green" style="margin-top:20px"><strong>Ready for Part II?</strong> Next: Regenerative Energy — where physics meets energy recovery.</div>
      </div>
    </div>
  </section>
"""

ch4_pos = content.find('Chapter 4 Summary')
if ch4_pos >= 0:
    ch4_end = content.find('</section>', ch4_pos)
    content = content[:ch4_end + len('</section>')] + '\n' + quiz_a + content[ch4_end + len('</section>'):]
    print("3. Quiz A inserted")
else:
    print("3. WARNING: Chapter 4 Summary not found")

# ═══════════════════════════════════════════════
# 4. INSERT QUIZ B
# ═══════════════════════════════════════════════
quiz_b = """
  <!-- QUIZ B -->
  <section class="slide" data-num="quiz-b" data-section="regen-damper" id="sQuizB">
    <div class="brand-tr">PowerNetPro Pvt. Ltd.</div>
    <div class="sf">Omkar · EV Centre of Excellence, MIT-WPU | PowerNetPro Pvt.Ltd.</div>
    <span class="tag tag-red">CHECKPOINT</span>
    <h2 class="st">Quick Quiz — Regenerative Energy</h2>
    <p class="sb">Test your understanding of regen braking and damper harvesting.</p>
    <div class="merged-slide-container">
      <div class="merged-col">
        <div class="quiz-q">Q1: What limits regen braking at low speeds?</div>
        <div class="quiz-options" data-quiz="q4">
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">A</span>Battery is fully charged</div>
          <div class="quiz-opt" data-correct="true" onclick="quizAnswer(this)"><span class="q-letter">B</span>Back-EMF is too low for the motor to generate torque</div>
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">C</span>Tire friction coefficient drops below 0.1</div>
        </div>
        <div class="quiz-explain" data-for="q4">At low speeds, back-EMF is proportional to speed — too little for meaningful braking torque.</div>
        <div class="quiz-q">Q2: When is max power transferred from regen damper?</div>
        <div class="quiz-options" data-quiz="q5">
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">A</span>When R_load = 0 (short circuit)</div>
          <div class="quiz-opt" data-correct="true" onclick="quizAnswer(this)"><span class="q-letter">B</span>When R_load = R_coil (impedance matching)</div>
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">C</span>When R_load is as large as possible</div>
        </div>
        <div class="quiz-explain" data-for="q5">Maximum power transfer theorem: P_max when load resistance equals source resistance.</div>
      </div>
      <div class="merged-col">
        <div class="quiz-q">Q3: Which ISO 8608 class = typical Indian urban roads?</div>
        <div class="quiz-options" data-quiz="q6">
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">A</span>Class A (very smooth)</div>
          <div class="quiz-opt" data-correct="true" onclick="quizAnswer(this)"><span class="q-letter">B</span>Class C (average)</div>
          <div class="quiz-opt" data-correct="false" onclick="quizAnswer(this)"><span class="q-letter">C</span>Class E (very poor)</div>
        </div>
        <div class="quiz-explain" data-for="q6">Class C (Gd=256e-6) = typical Indian urban. D/E are rural/damaged; A is new highways.</div>
        <div class="note note-red" style="margin-top:20px"><strong>Great work!</strong> Now let's build in the Hands-On Lab.</div>
      </div>
    </div>
  </section>
"""

ch6_pos = content.find('Chapter 6 Summary')
if ch6_pos >= 0:
    ch6_end = content.find('</section>', ch6_pos)
    content = content[:ch6_end + len('</section>')] + '\n' + quiz_b + content[ch6_end + len('</section>'):]
    print("4. Quiz B inserted")
else:
    print("4. WARNING: Chapter 6 Summary not found")

# ═══════════════════════════════════════════════
# 5-7. ANIMATE SVGs
# ═══════════════════════════════════════════════
# Li-ion charge path
r = content.replace('marker-end="url(#ah)" />', 'marker-end="url(#ah)" class="ion-anim" />', 1)
if r != content: content = r; print("5a. Li-ion charge animated")
r = content.replace('marker-end="url(#ah2)" />', 'marker-end="url(#ah2)" class="ion-anim-rev" />', 1)
if r != content: content = r; print("5b. Li-ion discharge animated")

# EKF convergence
ekf_pos = content.find('Coulomb')
if ekf_pos > 0:
    # Find within 2000 chars after
    block = content[ekf_pos:ekf_pos+2000]
    
    # Drift line
    old = 'stroke="#ff6b6b" stroke-width="2" />'
    pos = block.find(old)
    if pos >= 0:
        abs_pos = ekf_pos + pos
        content = content[:abs_pos] + 'stroke="#ff6b6b" stroke-width="2" class="svg-draw" />' + content[abs_pos+len(old):]
        print("6a. EKF drift line animated")
    
    # Refresh block
    block = content[ekf_pos:ekf_pos+2500]
    old = '>Drift!</text>'
    pos = block.find(old)
    if pos >= 0:
        abs_pos = ekf_pos + pos
        content = content[:abs_pos] + ' class="svg-fade">Drift!</text>' + content[abs_pos+len(old):]
        print("6b. Drift label animated")
    
    block = content[ekf_pos:ekf_pos+2500]
    old = 'stroke="#00d4ff" stroke-width="2" />'
    pos = block.find(old)
    if pos >= 0:
        abs_pos = ekf_pos + pos
        content = content[:abs_pos] + 'stroke="#00d4ff" stroke-width="2" class="svg-draw-delay" />' + content[abs_pos+len(old):]
        print("6c. EKF convergence animated")
    
    block = content[ekf_pos:ekf_pos+2500]
    old = '>Converges!</text>'
    pos = block.find(old)
    if pos >= 0:
        abs_pos = ekf_pos + pos
        content = content[:abs_pos] + ' class="svg-fade-d2">Converges!</text>' + content[abs_pos+len(old):]
        print("6d. Converges label animated")

# GITT pulse
gitt_pos = content.find('GITT: Pulse')
if gitt_pos > 0:
    block = content[gitt_pos:gitt_pos+1500]
    old = 'stroke="#00e5a0" stroke-width="2" />'
    pos = block.find(old)
    if pos >= 0:
        abs_pos = gitt_pos + pos
        content = content[:abs_pos] + 'stroke="#00e5a0" stroke-width="2" class="svg-draw" />' + content[abs_pos+len(old):]
        print("7a. GITT voltage animated")
    
    block = content[gitt_pos:gitt_pos+1500]
    old = 'font-size="7">OCV</text>'
    pos = block.find(old)
    if pos >= 0:
        abs_pos = gitt_pos + pos
        content = content[:abs_pos] + 'font-size="7" class="svg-fade">OCV</text>' + content[abs_pos+len(old):]
        print("7b. OCV label 1 animated")
    
    block = content[gitt_pos:gitt_pos+2000]
    pos = block.find(old)
    if pos >= 0:
        abs_pos = gitt_pos + pos
        content = content[:abs_pos] + 'font-size="7" class="svg-fade-d2">OCV</text>' + content[abs_pos+len(old):]
        print("7c. OCV label 2 animated")
    
    block = content[gitt_pos:gitt_pos+2000]
    pos = block.find(old)
    if pos >= 0:
        abs_pos = gitt_pos + pos
        content = content[:abs_pos] + 'font-size="7" class="svg-fade-d3">OCV</text>' + content[abs_pos+len(old):]
        print("7d. OCV label 3 animated")

# ═══════════════════════════════════════════════
# 8. ADD QUIZ JS
# ═══════════════════════════════════════════════
quiz_js = """
// Quiz handler
window.quizAnswer=function(el){
  var parent=el.closest('.quiz-options');
  var opts=parent.querySelectorAll('.quiz-opt');
  for(var i=0;i<opts.length;i++){opts[i].classList.add('answered');if(opts[i].dataset.correct==='true')opts[i].classList.add('correct');else if(opts[i]===el)opts[i].classList.add('wrong');}
  var explain=parent.nextElementSibling;
  if(explain&&explain.classList.contains('quiz-explain'))explain.classList.add('show');
};
"""

# Try both line ending styles
inserted_js = False
for ending in ['})();\r\n</script>', '})();\n</script>']:
    if ending in content:
        content = content.replace(ending, quiz_js + ending, 1)
        print("8. Quiz JS added")
        inserted_js = True
        break
if not inserted_js:
    print("8. WARNING: JS insertion point not found")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone! All enhancements applied.")
