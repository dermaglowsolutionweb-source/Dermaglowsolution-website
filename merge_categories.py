import re

def update_admin():
    with open('admin/admin.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace category 'Hydra Facial' with 'Premium Hydra'
    content = content.replace("category: 'Hydra Facial'", "category: 'Premium Hydra'")
    
    with open('admin/admin.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("admin.js updated")

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove hydra-facial nav link
    content = re.sub(r'<a href="#hydra-facial">Hydra Facial</a>\s*', '', content)
    
    # Extract the Hydra Facial products
    # We will grab all .product-card elements inside #hydra-facial
    hydra_facial_section_match = re.search(r'<!-- Category 2: Hydra Facial Machines -->.*?<section id="hydra-facial".*?<div class="product-grid">(.*?)</div>.*?<\/section>', content, re.DOTALL)
    if not hydra_facial_section_match:
        print("Could not find hydra-facial section")
        return
        
    hydra_facial_products = hydra_facial_section_match.group(1)
    
    # Extract the Premium Hydra section
    premium_hydra_match = re.search(r'(<!-- Category 1: Premium Hydra Machines -->\s*<section id="premium-hydra".*?<div class="product-grid">.*?)(</div>\s*<div class="text-center section-cta fade-in-up delay-3">.*?<\/section>)', content, re.DOTALL)
    if not premium_hydra_match:
        print("Could not find premium-hydra section")
        return
        
    # Remove the hydra-facial section entirely from the document
    content = re.sub(r'\s*<!-- Category 2: Hydra Facial Machines -->.*?<\/section>\s*', '\n\n', content, flags=re.DOTALL)
    
    # Add the extracted products to the premium hydra section
    # Note: We append the hydra_facial_products before the closing </div> of the product-grid
    premium_start = premium_hydra_match.group(1)
    premium_end = premium_hydra_match.group(2)
    new_premium_section = premium_start + '\n' + hydra_facial_products + '\n' + premium_end
    
    # Now we need to remove the old premium hydra section and place the new one right after Diode + Pico
    # First, delete old premium hydra
    # wait, instead of deleting and inserting, let's just delete the old one first
    old_premium_hydra_pattern = r'\s*<!-- Why Choose Us -->\s*<!-- Category 1: Premium Hydra Machines -->.*?<\/section>\s*'
    content = re.sub(r'\s*<!-- Category 1: Premium Hydra Machines -->.*?<\/section>\s*', '\n\n', content, flags=re.DOTALL)
    
    # Also wait, the old one had <!-- Why Choose Us --> right above it, wait no, line 710 was <!-- Why Choose Us --> but the section itself is below it. Let's make sure we didn't break that. 
    # Let's clean up that specific match. Let's just find and remove the exact text of the old premium hydra section.
    full_premium_hydra_match = re.search(r'\s*<!-- Category 1: Premium Hydra Machines -->.*?<\/section>\s*', content, flags=re.DOTALL)
    if full_premium_hydra_match:
        content = content.replace(full_premium_hydra_match.group(0), '\n\n')
        
    # Now we want to insert `new_premium_section` after Diode + Pico Laser section
    diode_pico_match = re.search(r'(<!-- Category: Diode \+ Pico Laser -->.*?<\/section>)', content, flags=re.DOTALL)
    if diode_pico_match:
        diode_pico_full = diode_pico_match.group(1)
        # We append new_premium_section after it
        content = content.replace(diode_pico_full, diode_pico_full + '\n\n    <!-- Category: Premium Hydra Machines -->\n' + new_premium_section)
    else:
        print("Could not find diode+pico section")
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated")

if __name__ == '__main__':
    update_admin()
    update_index()
