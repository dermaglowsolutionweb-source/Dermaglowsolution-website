def update_why_us():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_section = """<section id="why-us" class="why-us-section section-padding alt-bg">
        <div class="container">
            <div class="section-header fade-in-up">
                <h2 class="section-title">Why Choose DermaGlowSolution?</h2>
            </div>
            
            <div class="checklist-container fade-in-up">
                <ul class="custom-checklist">
                    <li><i class="fa-solid fa-square-check"></i> Pan India Delivery</li>
                    <li><i class="fa-solid fa-square-check"></i> Installation Support</li>
                    <li><i class="fa-solid fa-square-check"></i> Training Support</li>
                    <li><i class="fa-solid fa-square-check"></i> Spare Parts Availability</li>
                    <li><i class="fa-solid fa-square-check"></i> Technical Service Team</li>
                    <li><i class="fa-solid fa-square-check"></i> Doorstep Pickup & Drop</li>
                    <li><i class="fa-solid fa-square-check"></i> Warranty Support</li>
                </ul>
            </div>
        </div>
    </section>"""

    start_idx = html.find('<section id="why-us"')
    if start_idx != -1:
        end_idx = html.find('</section>', start_idx) + len('</section>')
        html = html[:start_idx] + new_section + html[end_idx:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("index.html updated successfully.")
    else:
        print("Why Us section not found.")


    with open('styles.css', 'r', encoding='utf-8') as f:
        css = f.read()

    new_css = """
/* Custom Checklist */
.checklist-container {
    max-width: 800px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 16px;
    padding: 2.5rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    backdrop-filter: blur(10px);
}

.custom-checklist {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
}

.custom-checklist li {
    font-size: 1.25rem;
    color: var(--text-dark);
    display: flex;
    align-items: center;
    font-weight: 500;
}

.custom-checklist li i {
    color: #00d26a; /* Bright Green */
    font-size: 1.5rem;
    margin-right: 15px;
}
"""

    if '.checklist-container' not in css:
        css += new_css
        with open('styles.css', 'w', encoding='utf-8') as f:
            f.write(css)
        print("styles.css updated successfully.")

if __name__ == '__main__':
    update_why_us()
