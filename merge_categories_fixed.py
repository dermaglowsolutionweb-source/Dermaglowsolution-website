def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Nav Link
    content = content.replace('                <a href="#hydra-facial">Hydra Facial</a>\n', '')

    # Extract Hydra Facial Products
    hf_start = content.find('<!-- Category 2: Hydra Facial Machines -->')
    hf_end = content.find('<!-- Category: AI face analyser -->')
    hf_section = content[hf_start:hf_end]

    # Delete HF section from content
    content = content[:hf_start] + content[hf_end:]

    # Get the products from HF section
    grid_start_idx = hf_section.find('<div class="product-grid">') + len('<div class="product-grid">')
    grid_end_idx = hf_section.find('<div class="text-center section-cta')
    hf_products = hf_section[grid_start_idx:grid_end_idx]
    hf_products = hf_products.rsplit('</div>', 1)[0] # remove the closing div of product-grid

    # Extract Premium Hydra section
    # Wait, the comment is <!-- Category 1: Premium Hydra Machines -->, let's find it.
    ph_start = content.find('<!-- Category 1: Premium Hydra Machines -->')
    if ph_start == -1:
        # Fallback to id
        ph_start = content.find('<section id="premium-hydra"')
        # Go back to the comment
        ph_start = content.rfind('<!--', 0, ph_start)

    ph_end = content.find('<!-- Category: Electric Derma bed -->')
    ph_section = content[ph_start:ph_end]

    # Delete PH section from its current place
    content = content[:ph_start] + content[ph_end:]

    # Insert the hf_products into ph_section
    ph_grid_end_idx = ph_section.find('<div class="text-center section-cta')
    ph_grid_end_idx = ph_section.rfind('</div>', 0, ph_grid_end_idx)

    new_ph_section = ph_section[:ph_grid_end_idx] + hf_products + ph_section[ph_grid_end_idx:]

    # Now place new_ph_section right after Diode + Pico
    dp_start = content.find('<!-- Category: Diode + Pico Laser -->')
    dp_end = content.find('<!-- Category: Cryopilopysis -->', dp_start)

    # Insert between dp_end and whatever is there
    content = content[:dp_end] + new_ph_section + content[dp_end:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html successfully merged")

if __name__ == '__main__':
    update_index()
