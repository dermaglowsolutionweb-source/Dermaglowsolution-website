def add_cryo_product():
    # --- Update index.html ---
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_product_html = """
                <!-- Product 4 -->
                <div class="product-card glass-card fade-in-up delay-3">
                    <div class="product-image-container">
                        <img src="images/Cryopilopysis/4.jpeg" alt="Advanced Cryopilopysis Machine" class="product-img" loading="lazy">
                        <div class="product-icon laser-icon"><i class="fa-solid fa-snowflake"></i></div>
                    </div>
                    <h3 class="product-title">Advanced Cryopilopysis Machine</h3>
                    <ul class="feature-list">
                        <li><i class="fa-solid fa-check"></i> Advanced Body Sculpting</li>
                        <li><i class="fa-solid fa-check"></i> Precise Fat Freezing</li>
                        <li><i class="fa-solid fa-check"></i> Non-Invasive Treatment</li>
                        <li><i class="fa-solid fa-check"></i> Safe & Effective Body Contouring</li>
                    </ul>
                    <a href="https://wa.me/919152261957?text=Hi%2C%20I%27m%20interested%20in%20the%20Advanced%20Cryopilopysis%20Machine" class="btn btn-whatsapp-card" target="_blank">
                        <i class="fa-brands fa-whatsapp"></i> Get Pricing
                    </a>
                </div>
"""

    # Find the end of the 3rd product in Cryopilopysis
    target = 'Get Pricing\n                      </a>\n                  </div>'
    cryo_start = html.find('id="cryopilopysis"')
    if cryo_start != -1:
        # Find product 3 inside cryo section
        prod3_title = html.find('10 IN 1 80K SLIMMING MACHINE', cryo_start)
        if prod3_title != -1:
            prod3_end = html.find('</div>', html.find('</a>', prod3_title))
            # The closing </div> of Product 3
            insert_pos = prod3_end + 6
            html = html[:insert_pos] + new_product_html + html[insert_pos:]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print("index.html updated successfully.")
        else:
            print("Product 3 not found.")
    else:
        print("Cryopilopysis section not found.")


    # --- Update admin.js ---
    with open('admin/admin.js', 'r', encoding='utf-8') as f:
        admin = f.read()

    new_admin_product = "    { name: 'Advanced Cryopilopysis Machine', category: 'Cryopilopysis', image: '../images/Cryopilopysis/4.jpeg' },\n"
    
    # Find the last Cryo product and insert after
    admin_target = "{ name: '10 IN 1 80K SLIMMING MACHINE', category: 'Cryopilopysis', image: '../images/Cryopilopysis/3.jpeg' },"
    if admin_target in admin:
        admin = admin.replace(admin_target, admin_target + "\n" + new_admin_product)
        with open('admin/admin.js', 'w', encoding='utf-8') as f:
            f.write(admin)
        print("admin.js updated successfully.")
    else:
        print("admin target not found.")

if __name__ == '__main__':
    add_cryo_product()
