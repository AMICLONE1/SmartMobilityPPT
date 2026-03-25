import re
from bs4 import BeautifulSoup
import uuid

def make_svg(prompt):
    p_lower = prompt.lower()
    
    # Base premium dark theme styles
    bg = "var(--bg3)"
    stroke = "var(--border)"
    accent1 = "var(--green)"
    accent2 = "var(--cyan)"
    accent3 = "var(--blue)"
    
    html = f'<div style="width:100%; min-height:220px; background:{bg}; border:1px solid {stroke}; border-radius:14px; position:relative; overflow:hidden; padding:20px; display:flex; flex-direction:column; justify-content:center; align-items:center;">'
    
    if "simulink" in p_lower or "block diagram" in p_lower:
        # Simulink style blocks
        html += f'''
        <svg viewBox="0 0 400 150" style="width:100%; height:auto;">
          <!-- Wires -->
          <path d="M 80 75 L 140 75" stroke="{accent3}" stroke-width="2" fill="none"/>
          <path d="M 220 75 L 280 75" stroke="{accent3}" stroke-width="2" fill="none"/>
          <polygon points="140,75 130,70 130,80" fill="{accent3}"/>
          <polygon points="280,75 270,70 270,80" fill="{accent3}"/>
          
          <!-- Blocks -->
          <rect x="20" y="50" width="60" height="50" rx="4" fill="var(--bg4)" stroke="{accent1}" stroke-width="2"/>
          <text x="50" y="79" fill="var(--text)" font-size="10" font-family="monospace" text-anchor="middle">Source</text>
          
          <rect x="140" y="40" width="80" height="70" rx="4" fill="var(--bg4)" stroke="{accent2}" stroke-width="2"/>
          <text x="180" y="75" fill="var(--text)" font-size="10" font-family="monospace" text-anchor="middle">Controller</text>
          <text x="180" y="90" fill="var(--muted)" font-size="8" text-anchor="middle">Subsystem</text>
          
          <rect x="280" y="50" width="60" height="50" rx="4" fill="var(--bg4)" stroke="var(--gold)" stroke-width="2"/>
          <text x="310" y="79" fill="var(--text)" font-size="10" font-family="monospace" text-anchor="middle">Scope</text>
        </svg>
        '''
    elif "graph" in p_lower or "curve" in p_lower or "plot" in p_lower:
        # Line Chart
        html += f'''
        <svg viewBox="0 0 400 200" style="width:100%; height:auto;">
          <!-- Grid -->
          <path d="M 50 150 L 350 150" stroke="{stroke}" stroke-dasharray="4" stroke-width="1"/>
          <path d="M 50 100 L 350 100" stroke="{stroke}" stroke-dasharray="4" stroke-width="1"/>
          <path d="M 50 50 L 350 50" stroke="{stroke}" stroke-dasharray="4" stroke-width="1"/>
          
          <!-- Axes -->
          <path d="M 50 20 L 50 180 L 350 180" stroke="var(--text2)" stroke-width="2" fill="none"/>
          
          <!-- Curves -->
          <path d="M 50 170 C 150 170, 200 40, 350 30" stroke="{accent1}" stroke-width="3" fill="none"/>
          <path d="M 50 40 L 150 60 L 250 120 L 350 160" stroke="{accent2}" stroke-width="2" fill="none"/>
        </svg>
        '''
    elif "flow" in p_lower or "diagram" in p_lower:
        # Flowchart
        html += f'''
        <svg viewBox="0 0 400 200" style="width:100%; height:auto;">
          <circle cx="200" cy="100" r="60" fill="var(--bg4)" stroke="{accent2}" stroke-width="2" opacity="0.3"/>
          <circle cx="200" cy="100" r="40" fill="var(--bg4)" stroke="{accent1}" stroke-width="2" opacity="0.5"/>
          
          <rect x="60" y="85" width="60" height="30" rx="15" fill="none" stroke="{accent3}" stroke-width="2"/>
          <rect x="280" y="85" width="60" height="30" rx="15" fill="none" stroke="var(--red)" stroke-width="2"/>
          
          <path d="M 120 100 L 180 100" stroke="{accent3}" stroke-width="2" fill="none" stroke-dasharray="4"/>
          <path d="M 220 100 L 280 100" stroke="{accent3}" stroke-width="2" fill="none" stroke-dasharray="4"/>
          
          <polygon points="180,100 175,95 175,105" fill="{accent3}"/>
          <polygon points="280,100 275,95 275,105" fill="{accent3}"/>
        </svg>
        '''
    else:
        # Generic generic
        html += f'''
        <svg viewBox="0 0 400 150" style="width:100%; height:auto;">
          <rect x="150" y="25" width="100" height="100" rx="10" fill="none" stroke="{accent2}" stroke-width="4" stroke-dasharray="10 5" opacity="0.5">
            <animate attributeName="stroke-dashoffset" from="0" to="100" dur="10s" repeatCount="indefinite" />
          </rect>
          <circle cx="200" cy="75" r="20" fill="{accent1}" opacity="0.8"/>
        </svg>
        '''
        
    html += f'<div style="margin-top:10px; font-size:11px; color:var(--muted); text-align:center; font-style:italic;">Visual: {prompt[:80]}...</div>'
    html += '</div>'
    return html

def main():
    path = r"d:\EV_LAB\Smart Mobiltiy Session\SmartMobilityPPT\EV_Workshop_Day4_Presentation.html"
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    # 1. Update Footer
    for sf in soup.find_all("div", class_="sf"):
        text = sf.get_text()
        if "PowerNetPro Pvt.Ltd." not in text:
            sf.string = text + " | PowerNetPro Pvt.Ltd."
            
    # 2. Replace Placeholders
    for ph in soup.find_all("div", class_="img-placeholder"):
        prompt_tag = ph.find("p", class_="img-prompt")
        prompt_text = prompt_tag.get_text() if prompt_tag else "Diagram placeholder"
        svg_html = make_svg(prompt_text)
        
        new_tag = BeautifulSoup(svg_html, "html.parser").div
        ph.replace_with(new_tag)
        
    # 3. Merge Slides (Only regular slides)
    slides = soup.find_all("section", class_=lambda c: c and "slide" in c.split())
    # Group standard slides by data-section
    groups = {}
    for s in slides:
        classes = s.get("class", [])
        if "hero-slide" in classes or "divider-slide" in classes:
            continue
        
        ds = s.get("data-section", "none")
        if ds not in groups:
            groups[ds] = []
        groups[ds].append(s)
        
    # Inject CSS for merging
    style_tag = soup.find("style")
    if style_tag:
        style_tag.append("""
        .merged-slide-container { display:flex; flex-direction:row; gap:40px; justify-content:space-between; width:100%; height:100%; align-items:flex-start; margin-top: 10px; }
        .merged-col { flex:1; min-width:0; display:flex; flex-direction:column; overflow:visible; }
        .merged-col .st { font-size: 24px; margin-bottom: 12px; }
        .merged-col .two-col { grid-template-columns: 1fr; gap: 16px; margin: 8px 0; }
        .merged-col .card-grid.c3 { grid-template-columns: 1fr; gap: 12px; }
        .slide { padding: 40px 50px; }
        """)
        
    for ds, group_slides in groups.items():
        # Merge every 2 slides
        for i in range(0, len(group_slides), 2):
            if i + 1 < len(group_slides):
                s1 = group_slides[i]
                s2 = group_slides[i+1]
                
                # Create merged container
                container = soup.new_tag("div", attrs={"class": "merged-slide-container"})
                
                col1 = soup.new_tag("div", attrs={"class": "merged-col"})
                col2 = soup.new_tag("div", attrs={"class": "merged-col"})
                
                # Move contents of s1
                for child in list(s1.children):
                    if child.name in ["span", "div"] and child.get("class"):
                        if "sn" in child.get("class", []) or "sf" in child.get("class", []):
                            continue # Leave sn and sf to the parent slide
                    col1.append(child.extract())
                    
                # Move contents of s2
                for child in list(s2.children):
                    if child.name in ["span", "div"] and child.get("class"):
                        if "sn" in child.get("class", []) or "sf" in child.get("class", []):
                            continue
                    col2.append(child.extract())
                    
                container.append(col1)
                container.append(col2)
                
                # Build new merged slide based on s1
                s1.append(container)
                
                # Remove s2
                s2.decompose()
                
    # 4. Renumber all remaining slides
    final_slides = soup.find_all("section", class_=lambda c: c and "slide" in c.split())
    total_slides = len(final_slides)
    for idx, s in enumerate(final_slides):
        sn = s.find("span", class_="sn")
        if sn:
            sn.string = f"{idx+1:02d}"
            
    # Modify <div id="slideCounter">
    counter = soup.find("div", id="slideCounter")
    if counter:
        counter.string = f"01 / {total_slides}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print(f"Done. Compressed presentation to {total_slides} slides.")

if __name__ == "__main__":
    main()
