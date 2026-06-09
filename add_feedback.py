import os
import shutil

def setup_feedback():
    src_dir = r"C:\Users\Nikesh S\.gemini\antigravity\scratch\dermaglow-solution\Feedback"
    dest_dir = "images/feedback"
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    # Copy and rename images
    img_count = 0
    if os.path.exists(src_dir):
        for file in os.listdir(src_dir):
            if file.lower().endswith(('.jpeg', '.jpg', '.png')):
                img_count += 1
                ext = file.split('.')[-1]
                src_path = os.path.join(src_dir, file)
                dest_path = os.path.join(dest_dir, f"{img_count}.{ext}")
                shutil.copy2(src_path, dest_path)
    
    # --- Update index.html ---
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Generate HTML for the grid
    grid_html = ""
    for i in range(1, img_count + 1):
        grid_html += f"""
                <div class="feedback-item fade-in-up delay-{i % 5}">
                    <img src="images/feedback/{i}.jpeg" alt="Customer Feedback {i}" class="feedback-img" loading="lazy">
                </div>"""

    new_section_html = f"""
    <!-- Customer Feedback Section -->
    <section id="feedback" class="feedback-section section-padding">
        <div class="container">
            <div class="section-header fade-in-up">
                <h2 class="section-title">Trusted by Professionals</h2>
                <p class="section-description">See how our premium machines are empowering clinics and dermatologists nationwide.</p>
            </div>
            
            <div class="feedback-grid">
{grid_html}
            </div>
        </div>
    </section>
"""

    why_us_end = html.find('</section>', html.find('id="why-us"'))
    if why_us_end != -1:
        insert_pos = why_us_end + len('</section>') + 1
        html = html[:insert_pos] + new_section_html + html[insert_pos:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("index.html updated successfully.")
    else:
        print("Could not find Why Us section to insert after.")

    # --- Update styles.css ---
    with open('styles.css', 'r', encoding='utf-8') as f:
        css = f.read()

    new_css = """
/* Feedback Grid */
.feedback-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.feedback-item {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    aspect-ratio: 4/5;
}

.feedback-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

.feedback-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}
"""
    if '.feedback-grid' not in css:
        css += new_css
        with open('styles.css', 'w', encoding='utf-8') as f:
            f.write(css)
        print("styles.css updated successfully.")

if __name__ == '__main__':
    setup_feedback()
