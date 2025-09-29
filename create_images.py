from PIL import Image, ImageDraw
import os

# Folder where images will be stored
IMAGE_FOLDER = "images"

def create_sample_images():
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)

    colors = ["red", "green", "blue", "yellow", "purple"]
    for i, color in enumerate(colors, start=1):
        img = Image.new("RGB", (800, 600), color=color)  # create solid color image
        draw = ImageDraw.Draw(img)
        draw.text((50, 50), f"Sample {i} - {color}", fill="white")
        filename = os.path.join(IMAGE_FOLDER, f"sample_{i}.jpg")
        img.save(filename)
        print(f"✅ Created {filename}")

if __name__ == "__main__":
    create_sample_images()
