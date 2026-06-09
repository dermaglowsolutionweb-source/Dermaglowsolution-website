import os
from PIL import Image

def optimize_images(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                filepath = os.path.join(root, file)
                try:
                    img = Image.open(filepath)
                    # Save optimized
                    img.save(filepath, format='PNG', optimize=True)
                    print(f"Optimized {file}")
                except Exception as e:
                    print(f"Failed to optimize {file}: {e}")

if __name__ == '__main__':
    optimize_images('images')
