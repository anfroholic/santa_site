import os
from PIL import Image

# === Configuration ===
INPUT_DIR = 'src/static/pics'          # Folder containing original images
OUTPUT_DIR = 'src/static/tmbs'        # Folder to save processed thumbnails
TARGET_SIZE = (320, 256)            # Final size (width, height)

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def center_crop(image):
    width, height = image.size
    new_edge = min(width, height)
    left = (width - new_edge) // 2
    top = (height - new_edge) // 2
    right = left + new_edge
    bottom = top + new_edge
    return image.crop((left, top, right, bottom))

def process_image(filepath):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    ext = ext.lower().strip('.')

    if ext not in ['jpg', 'jpeg', 'png', 'webp', 'bmp']:
        print(f"Skipping unsupported file type: {filename}")
        return

    try:
        with Image.open(filepath) as img:
            img = img.convert('RGB')
            img = center_crop(img)
            img = img.resize(TARGET_SIZE, Image.LANCZOS)

            output_filename = f"{name}-tmb.{ext}"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            img.save(output_path)
            # print(f"Saved thumbnail: {output_filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

def main():
    for file in os.listdir(INPUT_DIR):
        filepath = os.path.join(INPUT_DIR, file)
        if os.path.isfile(filepath):
            process_image(filepath)

if __name__ == "__main__":
    main()
    print(os.listdir('src/static/pics'))
