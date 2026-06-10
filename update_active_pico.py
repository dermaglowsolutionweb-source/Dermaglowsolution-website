import os

replacements = {
    "BV Laser 07 Pico": "Q - switched nd yag laser",
    "DermaGlowSolution Pico Laser": "crystal pico laser gear",
    "Bestview Active Pico Laser": "Active Pico Bv Laser"
}

for filepath in [r"C:\Users\Nikesh S\OneDrive\Documents\GitHub\dermaglow-solution\index.html", r"C:\Users\Nikesh S\OneDrive\Documents\GitHub\dermaglow-solution\admin\admin.js"]:
    if not os.path.exists(filepath): continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    for old_txt, new_txt in replacements.items():
        # Replace in HTML format
        content = content.replace(f">{old_txt}<", f">{new_txt}<")
        # Replace in JS format
        content = content.replace(f'"{old_txt}"', f'"{new_txt}"')
        content = content.replace(f"'{old_txt}'", f"'{new_txt}'")
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Updated Active Pico names successfully!")
