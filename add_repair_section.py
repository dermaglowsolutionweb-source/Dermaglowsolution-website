def add_repair_section():
    # --- Update index.html ---
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_section_html = """
    <!-- Repair Service Section -->
    <section id="repair-service" class="category-section section-padding" style="background: linear-gradient(135deg, var(--bg-dark) 0%, #1a1f2e 100%);">
        <div class="container">
            <div class="section-header fade-in-up">
                <h2 class="section-title" style="color: var(--primary-color);">We Repair All Types of Aesthetic Machines</h2>
                <p class="section-description" style="color: var(--text-muted);">Expert technical support and professional repair services. Fast, reliable, and trusted by clinics.</p>
            </div>
            
            <div class="repair-grid">
                <div class="repair-card fade-in-up">
                    <i class="fa-solid fa-bolt"></i>
                    <h3>Diode Laser</h3>
                </div>
                <div class="repair-card fade-in-up delay-1">
                    <i class="fa-solid fa-burst"></i>
                    <h3>Pico Laser</h3>
                </div>
                <div class="repair-card fade-in-up delay-2">
                    <i class="fa-solid fa-droplet"></i>
                    <h3>Hydra Facial</h3>
                </div>
                <div class="repair-card fade-in-up delay-3">
                    <i class="fa-solid fa-wave-square"></i>
                    <h3>HIFU</h3>
                </div>
                <div class="repair-card fade-in-up delay-4">
                    <i class="fa-solid fa-plug-circle-bolt"></i>
                    <h3>EMS</h3>
                </div>
                <div class="repair-card fade-in-up delay-5">
                    <i class="fa-solid fa-wand-magic-sparkles"></i>
                    <h3>CO2 Laser</h3>
                </div>
            </div>

            <div class="text-center section-cta fade-in-up delay-6" style="margin-top: 3rem;">
                <a href="https://wa.me/919152261957?text=Hi%2C%20I%20need%20repair%20service%20for%20my%20aesthetic%20machine." class="btn btn-primary btn-lg" target="_blank">
                    <i class="fa-solid fa-screwdriver-wrench" style="margin-right: 8px;"></i> Request Repair Service
                </a>
            </div>
        </div>
    </section>
"""

    why_us_start = html.find('<section id="why-us"')
    if why_us_start != -1:
        html = html[:why_us_start] + new_section_html + html[why_us_start:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("index.html updated successfully.")
    else:
        print("Why Us section not found.")


    # --- Update styles.css ---
    with open('styles.css', 'r', encoding='utf-8') as f:
        css = f.read()

    new_css = """
/* Repair Grid */
.repair-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.repair-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 2rem 1rem;
    text-align: center;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

.repair-card:hover {
    transform: translateY(-5px);
    background: rgba(255, 255, 255, 0.08);
    border-color: var(--primary-color);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.repair-card i {
    font-size: 2.5rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
    filter: drop-shadow(0 0 10px rgba(229, 184, 11, 0.3));
}

.repair-card h3 {
    color: white;
    font-size: 1.1rem;
    font-weight: 500;
    margin: 0;
}
"""
    if '.repair-grid' not in css:
        css += new_css
        with open('styles.css', 'w', encoding='utf-8') as f:
            f.write(css)
        print("styles.css updated successfully.")

if __name__ == '__main__':
    add_repair_section()
