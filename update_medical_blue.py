import re

css_path = r"C:\Users\Nikesh S\.gemini\antigravity\scratch\dermaglow-solution\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace root variables to classic Medical Blue
css = re.sub(r'--bg-dark:\s*#[a-fA-F0-9]{6};', '--bg-dark: #0a1128;', css)
css = re.sub(r'--bg-card:\s*rgba\([^)]+\);', '--bg-card: rgba(16, 30, 60, 0.6);', css)
css = re.sub(r'--bg-alt:\s*#[a-fA-F0-9]{6};', '--bg-alt: #0f1c3f;', css)

css = re.sub(r'--primary:\s*#[a-fA-F0-9]{6};', '--primary: #0071c5;', css)
css = re.sub(r'--primary-light:\s*#[a-fA-F0-9]{6};', '--primary-light: #3399ff;', css)
css = re.sub(r'--primary-dark:\s*#[a-fA-F0-9]{6};', '--primary-dark: #004d8c;', css)
css = re.sub(r'--primary-glow:\s*rgba\([^)]+\);', '--primary-glow: rgba(0, 113, 197, 0.5);', css)

css = re.sub(r'--secondary:\s*#[a-fA-F0-9]{6};', '--secondary: #00b4d8;', css)
css = re.sub(r'--secondary-glow:\s*rgba\([^)]+\);', '--secondary-glow: rgba(0, 180, 216, 0.3);', css)

# Replace hardcoded RGBA values from the previous cyan theme (6, 182, 212) -> Medical Blue (0, 113, 197)
css = css.replace("6, 182, 212", "0, 113, 197")
css = css.replace("6,182,212", "0,113,197")

# Replace dark bg overlays (0, 18, 25) -> Deep Navy (10, 17, 40)
css = css.replace("0, 18, 25", "10, 17, 40")
css = css.replace("0,18,25", "10,17,40")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Theme updated to Medical Blue successfully")
