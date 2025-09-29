import os
from PIL import Image

# Input and Output directories
INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"

# Desired size (width, height)
SIZE = (300, 300)  # change this as needed
FORMAT = "JPEG"    # convert all images to this format (JPEG, PNG, etc.)

def resize_images():
    # Create output folder if it doesn't exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Loop through all files in input folder
    for filename in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, filename)

        # Skip if not an image
        if not (filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif"))):
            continue

        try:
            # Open image
            img = Image.open(file_path)

            # Resize image
            img_resized = img.resize(SIZE)

            # Create new filename
            new_filename = os.path.splitext(filename)[0] + f".{FORMAT.lower()}"
            save_path = os.path.join(OUTPUT_FOLDER, new_filename)

            # Save resized & converted image
            img_resized.save(save_path, FORMAT)

            print(f"✅ Resized & saved: {save_path}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    resize_images()
