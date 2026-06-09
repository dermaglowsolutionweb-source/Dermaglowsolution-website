def add_laser_hair_removal():
    # --- Update index.html ---
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_section_html = """
    <!-- Category: Laser hair removal regrowth machine -->
    <section id="laser-hair-removal" class="category-section section-padding alt-bg">
        <div class="container">
            <div class="section-header fade-in-up">
                <h2 class="section-title">Laser hair removal regrowth machine</h2>
                <p class="section-description">Advanced solutions for permanent hair reduction and stimulated regrowth.</p>
            </div>
            
            <div class="product-grid">
                <!-- Product 1 -->
                <div class="product-card glass-card fade-in-up">
                    <div class="product-image-container">
                        <img src="images/Laser%20hair%20removal%20regrowth%20machine/1.jpeg" alt="Laser Hair Removal Regrowth Machine - Model 1" class="product-img" loading="lazy">
                        <div class="product-icon laser-icon"><i class="fa-solid fa-bolt"></i></div>
                    </div>
                    <h3 class="product-title">Laser Hair Removal Regrowth Machine - Model 1</h3>
                    <ul class="feature-list">
                        <li><i class="fa-solid fa-check"></i> Advanced Laser Technology</li>
                        <li><i class="fa-solid fa-check"></i> Fast and Effective Results</li>
                        <li><i class="fa-solid fa-check"></i> Safe for All Skin Types</li>
                        <li><i class="fa-solid fa-check"></i> Premium Performance</li>
                    </ul>
                    <a href="https://wa.me/919152261957?text=Hi%2C%20I%27m%20interested%20in%20the%20Laser%20Hair%20Removal%20Regrowth%20Machine%20Model%201" class="btn btn-whatsapp-card" target="_blank">
                        <i class="fa-brands fa-whatsapp"></i> Get Pricing
                    </a>
                </div>

                <!-- Product 2 -->
                <div class="product-card glass-card fade-in-up delay-1">
                    <div class="product-image-container">
                        <img src="images/Laser%20hair%20removal%20regrowth%20machine/2.jpeg" alt="Laser Hair Removal Regrowth Machine - Model 2" class="product-img" loading="lazy">
                        <div class="product-icon laser-icon"><i class="fa-solid fa-bolt"></i></div>
                    </div>
                    <h3 class="product-title">Laser Hair Removal Regrowth Machine - Model 2</h3>
                    <ul class="feature-list">
                        <li><i class="fa-solid fa-check"></i> Enhanced Precision Controls</li>
                        <li><i class="fa-solid fa-check"></i> Comfortable Treatment</li>
                        <li><i class="fa-solid fa-check"></i> High Power Output</li>
                        <li><i class="fa-solid fa-check"></i> Reliable & Durable Design</li>
                    </ul>
                    <a href="https://wa.me/919152261957?text=Hi%2C%20I%27m%20interested%20in%20the%20Laser%20Hair%20Removal%20Regrowth%20Machine%20Model%202" class="btn btn-whatsapp-card" target="_blank">
                        <i class="fa-brands fa-whatsapp"></i> Get Pricing
                    </a>
                </div>
            </div>
            
            <div class="text-center section-cta fade-in-up delay-2">
                <a href="https://wa.me/919152261957" class="btn btn-primary" target="_blank">Contact WhatsApp for Product Information & Pricing</a>
            </div>
        </div>
    </section>
"""

    # We will insert it after cryopilopysis section ends
    cryo_start = html.find('id="cryopilopysis"')
    if cryo_start != -1:
        cryo_end = html.find('</section>', cryo_start)
        if cryo_end != -1:
            insert_pos = cryo_end + len('</section>') + 1
            html = html[:insert_pos] + new_section_html + html[insert_pos:]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print("index.html updated successfully.")
        else:
            print("End of Cryopilopysis section not found.")
    else:
        print("Cryopilopysis section not found.")


    # --- Update admin.js ---
    with open('admin/admin.js', 'r', encoding='utf-8') as f:
        admin = f.read()

    new_admin_products = """    { name: 'Laser Hair Removal Regrowth Machine - Model 1', category: 'Laser hair removal regrowth machine', image: '../images/Laser%20hair%20removal%20regrowth%20machine/1.jpeg' },
    { name: 'Laser Hair Removal Regrowth Machine - Model 2', category: 'Laser hair removal regrowth machine', image: '../images/Laser%20hair%20removal%20regrowth%20machine/2.jpeg' },
"""
    
    # We will insert it before the closing bracket of PRODUCTS array. 
    # Let's find the end of PRODUCTS array. We can just insert it after Cryopilopysis products.
    # To be safe, insert before 'AI face analyser - Model 1'
    admin_target = "{ name: 'AI face analyser - Model 1', category: 'AI Face Analyser'"
    if admin_target in admin:
        admin = admin.replace(admin_target, new_admin_products + "    " + admin_target)
        with open('admin/admin.js', 'w', encoding='utf-8') as f:
            f.write(admin)
        print("admin.js updated successfully.")
    else:
        print("admin target not found.")

if __name__ == '__main__':
    add_laser_hair_removal()
