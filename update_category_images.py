import re

def update_images():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    categories = [
        ('id="adss"', 'Adss', 3),
        ('id="co2-fractional-laser"', 'CO2 Fractional Laser', 4),
        ('id="pico-laser"', 'Active Pico Laser', 4),
        ('id="cryopilopysis"', 'Cryopilopysis', 3),
        ('id="premium-hydra"', 'Premium Hydra Machines', 5)
    ]
    
    for section_id, folder_name, count in categories:
        start_idx = html.find(section_id)
        if start_idx == -1:
            print(f"Section {section_id} not found in index.html")
            continue
            
        # Find the end of the section
        end_idx = html.find('</section>', start_idx)
        if end_idx == -1:
            end_idx = len(html)
            
        section_html = html[start_idx:end_idx]
        
        # Replace images sequentially
        for i in range(1, count + 1):
            new_path = f"images/{folder_name}/{i}.jpeg"
            # Encode URL properly for spaces
            new_path = new_path.replace(' ', '%20')
            
            # Find the i-th <img src="..."> in this section
            # We use a non-greedy regex to match src="..."
            pattern = r'(<img[^>]*?src=")([^"]+?)("[^>]*?>)'
            
            # We need to replace only the i-th occurrence.
            # Using re.finditer to find all occurrences
            matches = list(re.finditer(pattern, section_html))
            if len(matches) >= i:
                match = matches[i-1]
                # Replace the src with new_path
                section_html = section_html[:match.start(2)] + new_path + section_html[match.end(2):]
                
        html = html[:start_idx] + section_html + html[end_idx:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated successfully.")

    # Now update admin.js
    with open('admin/admin.js', 'r', encoding='utf-8') as f:
        admin = f.read()

    # We will do a simple string replacement based on product names.
    # We need to map products to the new images.
    admin_updates = [
        # ADSS
        ('ADSS Diode Laser 600W | 4 Wavelength', 'Adss/1.jpeg'),
        ('ADSS 4D Tech laser USA FDA 1600w2400w - Model 1', 'Adss/2.jpeg'),
        ('ADSS 4D Tech laser USA FDA 1600w2400w - Model 2', 'Adss/3.jpeg'),
        # CO2
        ('Fractional CO2 Laser (White)', 'CO2 Fractional Laser/1.jpeg'),
        ('BV Laser CO2 (Dark Blue)', 'CO2 Fractional Laser/2.jpeg'),
        ('CO2 Laser Metal Tube (White)', 'CO2 Fractional Laser/3.jpeg'),
        ('BV Laser CO2 (Rose Gold)', 'CO2 Fractional Laser/4.jpeg'),
        # Pico
        ('Crystal pico laser', 'Active Pico Laser/1.jpeg'),
        ('active pico bv laser', 'Active Pico Laser/2.jpeg'),
        ('Q-Switched Nd:YAG Laser (Advanced)', 'Active Pico Laser/3.jpeg'),
        ('Q-Switched Nd:YAG BV Laser', 'Active Pico Laser/4.jpeg'),
        # Cryo
        ('360 CRYO + EMS + 40K + RF', 'Cryopilopysis/1.jpeg'),
        ('360 CRYO PILOPYSIS', 'Cryopilopysis/2.jpeg'),
        ('10 IN 1 80K SLIMMING MACHINE', 'Cryopilopysis/3.jpeg'),
        # Hydra
        ('10 in 1 Oxygen Hydra Machine', 'Premium Hydra Machines/1.jpeg'),
        ('13 in 1 Oxygen PDT Dynamic Hydra', 'Premium Hydra Machines/2.jpeg'),
        ('17 in 1 Hydra Plus Machine', 'Premium Hydra Machines/3.jpeg'),
        ('17 in 1 Hydra Facial Machine', 'Premium Hydra Machines/4.jpeg'),
        ('10 in 1 Hydra Facial Machine', 'Premium Hydra Machines/5.jpeg')
    ]

    for name, img_path in admin_updates:
        # We look for a line containing this name
        # Ex: { name: 'ADSS Diode Laser 600W | 4 Wavelength', category: 'ADSS', image: '../images/ai_adss_diode_600w.png' },
        # We use regex to replace the image path
        pattern = re.escape(name) + r"([^}]*?image:\s*')([^']+?)(')"
        new_path = f"../images/{img_path}".replace(' ', '%20')
        admin = re.sub(pattern, lambda m: m.group(0).replace(m.group(2), new_path), admin)

    with open('admin/admin.js', 'w', encoding='utf-8') as f:
        f.write(admin)
    print("admin.js updated successfully.")

if __name__ == '__main__':
    update_images()
