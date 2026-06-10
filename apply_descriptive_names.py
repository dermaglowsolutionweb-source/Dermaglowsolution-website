import os

replacements = {
    # Active Pico Laser
    "Active Pico laser - Model 1": "BV Laser 07 Pico",
    "Active Pico laser - Model 2": "DermaGlowSolution Pico Laser",
    "Active Pico laser - Model 3": "Bestview Active Pico Laser",
    "Active Pico laser - Model 4": "BV Laser Pro Pico",

    # CO2 Fractional Laser
    "CO2 Fractional Laser - Model 1": "CO2 Laser System",
    "CO2 Fractional Laser - Model 2": "BV Laser CO2 Metal Tube Technology",
    "CO2 Fractional Laser - Model 3": "OFA CO2 Fractional Laser",
    "CO2 Fractional Laser - Model 4": "CO2 Fractional Laser (Rose Gold)",

    # Cryopilopysis
    "Cryopilopysis - Model 1": "Advanced Cryo System",
    "Cryopilopysis - Model 2": "CRYO Sculpting Machine",
    "Cryopilopysis - Model 3": "Professional Cryo Device",
    "Cryopilopysis - Model 4": "Premium Cryolipolysis",

    # Premium Hydra Machines
    "Premium Hydra machine - Model 1": "Professional Hydra Machine",
    "Premium Hydra machine - Model 2": "CRYO Hydra System",
    "Premium Hydra machine - Model 3": "Clinical Aqua Peeling",
    "Premium Hydra machine - Model 4": "Hydra Dermabrasion Pro",
    "Premium Hydra machine - Model 5": "Ultimate Skin Rejuvenation",

    # Laser Hair
    "Laser hair removal regrowth machine - Model 1": "Laser Hair Removal System",
    "Laser hair removal regrowth machine - Model 2": "Advanced Laser Hair Device",
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
        
print("Applied descriptive names successfully!")
