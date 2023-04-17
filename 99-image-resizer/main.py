import argparse
import os

from PIL import Image

parser = argparse.ArgumentParser(description="Resize an image")
parser.add_argument("--image-path", help="Image path to resize", required=True)
parser.add_argument("--output-path", help="Image path to resize", required=True)

if __name__ == "__main__":
    args = parser.parse_args()
    image = Image.open(args.image_path)
    # Create Output dir if not exists
    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    # Resize 16x16, 48x48, 128x128
    img_16 = image.resize((16, 16))
    img_48 = image.resize((48, 48))
    img_128 = image.resize((128, 128))

    # Save
    img_16.save(f"{args.output_path}/icon_16.png")
    img_48.save(f"{args.output_path}/icon_48.png")
    img_128.save(f"{args.output_path}/icon_128.png")
