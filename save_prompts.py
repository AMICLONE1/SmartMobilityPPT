import re

path = r"d:\EV_LAB\Smart Mobiltiy Session\SmartMobilityPPT\EV_Workshop_Day4_Presentation.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

prompts = re.findall(r'<p class="img-prompt">(.*?)</p>', html, flags=re.DOTALL)
with open("extracted_prompts.txt", "w", encoding="utf-8") as f:
    for idx, p in enumerate(prompts):
        f.write(f"{idx+1}: {p.strip()}\n")
