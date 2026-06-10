import os

replacements = {
    # ADSS
    "ADSS Diode Laser 600W | 4 Wavelength": "ADSS 4D Tech laser USA FDA 1600w",
    "ADSS 4D Tech laser USA FDA 1600w2400w - Model 1": "ADSS 4D Tech laser USA FDA 2400w",
    "ADSS 4D Tech laser USA FDA 1600w2400w - Model 2": "ADSS 4D Tech laser",

    # Active Pico Laser
    "Crystal pico laser": "BV Laser 07 Pico",
    "active pico bv laser": "DermaGlowSolution Pico Laser",
    "Q-Switched Nd:YAG Laser (Advanced)": "Active Pico BV Laser",
    "Q-Switched Nd:YAG BV Laser": "BV Laser Pro",

    # CO2 Fractional Laser
    "Fractional CO2 Laser (White)": "CO2 Laser Pro",
    "BV Laser CO2 (Dark Blue)": "CO2 Laser Advanced",
    "CO2 Laser Metal Tube (White)": "OFA CO2 Laser",
    "BV Laser CO2 (Rose Gold)": "Professional CO2 Laser",

    # Cryopilopysis
    "360 CRYO + EMS + 40K + RF": "Advanced Cryo System",
    "360 CRYO PILOPYSIS": "CRYO Sculpting Machine",
    "10 IN 1 80K SLIMMING MACHINE": "Professional Cryo Device",
    "Advanced Cryopilopysis Machine": "Premium Cryolipolysis",

    # Premium Hydra Machines
    "10 in 1 Oxygen Hydra Machine": "Professional Hydra Machine",
    "13 in 1 Oxygen PDT Dynamic Hydra": "Advanced HydraFacial System",
    "17 in 1 Hydra Plus Machine": "Clinical Aqua Peeling",
    "17 in 1 Hydra Facial Machine": "Hydra Dermabrasion Pro",
    "10 in 1 Hydra Facial Machine": "Ultimate Skin Rejuvenation",
    "12 in 1 Hydra Facial Machine": "Advanced Aqua Peeling",
    "14 in 1 Hydra Facial Machine": "Premium Hydra Device",

    # Laser Hair
    "Laser Hair Removal Regrowth Machine - Model 1": "Laser Hair Removal System",
    "Laser Hair Removal Regrowth Machine - Model 2": "Advanced Laser Hair Device",
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
        
print("Updated successfully!")
