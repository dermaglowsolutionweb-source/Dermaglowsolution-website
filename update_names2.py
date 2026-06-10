import os

replacements = {
    # Active Pico Laser
    "BV Laser 07 Pico": "Active Pico laser - Model 1",
    "DermaGlowSolution Pico Laser": "Active Pico laser - Model 2",
    "Active Pico BV Laser": "Active Pico laser - Model 3",
    "BV Laser Pro": "Active Pico laser - Model 4",

    # CO2 Fractional Laser
    "CO2 Laser Pro": "CO2 Fractional Laser - Model 1",
    "CO2 Laser Advanced": "CO2 Fractional Laser - Model 2",
    "OFA CO2 Laser": "CO2 Fractional Laser - Model 3",
    "Professional CO2 Laser": "CO2 Fractional Laser - Model 4",

    # Cryopilopysis
    "Advanced Cryo System": "Cryopilopysis - Model 1",
    "CRYO Sculpting Machine": "Cryopilopysis - Model 2",
    "Professional Cryo Device": "Cryopilopysis - Model 3",
    "Premium Cryolipolysis": "Cryopilopysis - Model 4",

    # Premium Hydra Machines
    "Professional Hydra Machine": "Premium Hydra machine - Model 1",
    "Advanced HydraFacial System": "Premium Hydra machine - Model 2",
    "Clinical Aqua Peeling": "Premium Hydra machine - Model 3",
    "Hydra Dermabrasion Pro": "Premium Hydra machine - Model 4",
    "Ultimate Skin Rejuvenation": "Premium Hydra machine - Model 5",

    # Laser Hair
    "Laser Hair Removal System": "Laser hair removal regrowth machine - Model 1",
    "Advanced Laser Hair Device": "Laser hair removal regrowth machine - Model 2",
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
        
print("Updated model names successfully!")
