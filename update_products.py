import os
import re
import urllib.parse

base_path = r"C:\Users\Nikesh S\.gemini\antigravity\scratch\dermaglow-solution\wa.b"
html_file = r"C:\Users\Nikesh S\.gemini\antigravity\scratch\dermaglow-solution\index.html"

categories = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

html_content = ""

for i, category in enumerate(sorted(categories)):
    cat_path = os.path.join(base_path, category)
    images = [f for f in os.listdir(cat_path) if f.endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    
    bg_class = " alt-bg" if i % 2 == 1 else ""
    cat_id = category.lower().replace(" ", "-").replace("+", "plus")
    
    html_content += f'''
    <section id="{cat_id}" class="category-section section-padding{bg_class}">
        <div class="container">
            <div class="section-header fade-in-up">
                <h2 class="section-title">{category}</h2>
                <p class="section-description">Premium equipment for professional clinical use.</p>
            </div>
            
            <div class="product-grid">
'''
    
    for j, img in enumerate(sorted(images)):
        img_url = f"wa.b/{urllib.parse.quote(category)}/{urllib.parse.quote(img)}"
        product_name = f"{category}"
        if len(images) > 1:
            product_name += f" - Model {j+1}"
            
        whatsapp_msg = urllib.parse.quote(f"Hi, I'm interested in the {product_name}")
        html_content += f'''
                <div class="product-card glass-card fade-in-up">
                    <div class="product-image-container">
                        <img src="{img_url}" alt="{product_name}" class="product-img" loading="lazy">
                    </div>
                    <h3 class="product-title">{product_name}</h3>
                    <a href="https://wa.me/919152261957?text={whatsapp_msg}" class="btn btn-whatsapp-card" target="_blank">
                        <i class="fa-brands fa-whatsapp"></i> Get Pricing
                    </a>
                </div>
'''
    
    html_content += '''
            </div>
        </div>
    </section>
'''

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace existing categories up to "Why Choose Us"
pattern = r'<!-- Category 1: Premium Hydra Machines -->.*?(<!-- Why Choose Us -->)'

def repl(match):
    return "<!-- Dynamic Categories -->\n" + html_content + "\n    " + match.group(1)

new_content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html successfully with correct regex.")
