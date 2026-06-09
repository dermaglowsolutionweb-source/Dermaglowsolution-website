import os
from PIL import Image

def resize_images(directory, max_size=(500, 500)):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                filepath = os.path.join(root, file)
                try:
                    img = Image.open(filepath)
                    # Check if resizing is needed
                    if img.width > max_size[0] or img.height > max_size[1]:
                        img.thumbnail(max_size, Image.Resampling.LANCZOS)
                        img.save(filepath, format='PNG', optimize=True)
                        print(f"Resized {file}")
                except Exception as e:
                    print(f"Failed to resize {file}: {e}")

if __name__ == '__main__':
    resize_images('images')
