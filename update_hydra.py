import os

replacements = {
    # Active Pico Laser #4
    "BV Laser Pro Pico": "q sswitched nd yag laser",

    # Premium Hydra Machines
    "Professional Hydra Machine": "17 IN 1 Hydra Facial Machine",
    "CRYO Hydra System": "17 IN 1 Hydra plus Machine",
    "Clinical Aqua Peeling": "13 in 1 oxygen pdt dynamic hydra",
    "Hydra Dermabrasion Pro": "10 in 1 oxygen hydra alice superubble",
    "Ultimate Skin Rejuvenation": "8 in 1 alice superbubble max hydra",
    "Advanced Aqua Peeling": "7 in 1 alice super bubble oxygen hydra mechine"
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
        
print("Updated requested names successfully!")
