import os
import glob
from rembg import remove
from PIL import Image

def process_images():
    image_dir = r"C:\Users\Nikesh S\OneDrive\Documents\GitHub\dermaglow-solution\images"
    pattern = os.path.join(image_dir, "ai_*.png")
    images = glob.glob(pattern)
    
    print(f"Found {len(images)} AI images to process.")
    for img_path in images:
        print(f"Processing {img_path}...")
        try:
            # Read image
            input_image = Image.open(img_path).convert("RGBA")
            
            # Remove background
            output_image = remove(input_image)
            
            # Create a white background image of the same size
            white_bg = Image.new("RGBA", output_image.size, "WHITE")
            
            # Composite the foreground over the white background
            final_image = Image.alpha_composite(white_bg, output_image)
            
            # Convert to RGB
            final_image = final_image.convert("RGB")
            
            # Save back as PNG
            final_image.save(img_path, "PNG")
            print(f"Successfully updated {img_path}")
            
        except Exception as e:
            print(f"Error processing {img_path}: {e}")

if __name__ == "__main__":
    process_images()
