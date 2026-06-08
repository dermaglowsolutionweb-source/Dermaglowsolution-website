import re

css_path = r"C:\Users\Nikesh S\.gemini\antigravity\scratch\dermaglow-solution\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace root variables
css = re.sub(r'--bg-dark:\s*#020813;', '--bg-dark: #001219;', css)
css = re.sub(r'--bg-card:\s*rgba\(10,\s*25,\s*47,\s*0\.4\);', '--bg-card: rgba(0, 35, 50, 0.4);', css)
css = re.sub(r'--bg-alt:\s*#051021;', '--bg-alt: #001f2b;', css)

css = re.sub(r'--primary:\s*#2563eb;', '--primary: #06b6d4;', css)
css = re.sub(r'--primary-light:\s*#3b82f6;', '--primary-light: #22d3ee;', css)
css = re.sub(r'--primary-dark:\s*#1e40af;', '--primary-dark: #0891b2;', css)
css = re.sub(r'--primary-glow:\s*rgba\(37,\s*99,\s*235,\s*0\.5\);', '--primary-glow: rgba(6, 182, 212, 0.5);', css)

# Replace hardcoded RGBA values for primary color
css = css.replace("37, 99, 235", "6, 182, 212")
css = css.replace("37,99,235", "6,182,212")

# Adjust the very dark background overlays to match the ocean theme
css = css.replace("2, 8, 19", "0, 18, 25")
css = css.replace("2,8,19", "0,18,25")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Theme updated successfully")
