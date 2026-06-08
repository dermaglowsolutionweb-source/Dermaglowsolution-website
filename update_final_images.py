import re

html_path = r"C:\Users\Nikesh S\.gemini\antigravity\scratch\dermaglow-solution\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = {
    "wa.b/Diode%20%2B%20pico%20machine/p4.png": "images/ai_diode_pico_4_1780924557591.png",
    "wa.b/Diode%201000W/p%201.png": "images/ai_diode_1000w_1_1780924573578.png",
    "wa.b/Diode%201000W/p2.png": "images/ai_diode_1000w_2_1780924587656.png",
    "wa.b/Electric%20Derma%20bed/p1.png": "images/ai_derma_bed_1_1780924615768.png",
    "wa.b/Electric%20Derma%20bed/p2.png": "images/ai_derma_bed_2_1780924628217.png",
    "wa.b/Electric%20Derma%20bed/p3.png": "images/ai_derma_bed_3_1780924641316.png",
    "wa.b/HIFU/p1.png": "images/ai_hifu_1_1780924655511.png",
    "wa.b/HIFU/p2.png": "images/ai_hifu_2_1780924671247.png",
    "wa.b/HIFU/p3.png": "images/ai_hifu_3_1780924687699.png"
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML updated with final images successfully")
