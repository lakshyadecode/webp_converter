from PIL import Image
import os
import shutil


def convert_and_move_webp(input_folder, output_folder, extensions):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        if filename.endswith(tuple(extensions)):
            # Convert and save as WebP
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".webp")
            convert_to_webp(input_path, output_path)

        elif filename.endswith(".webp"):
            # Move WebP files directly to the output folder
            output_path = os.path.join(output_folder, filename)
            shutil.copy(input_path, output_path)


def convert_to_webp(input_path, output_path):
    # Load the image
    img = Image.open(input_path)

    # Save as WebP
    img.save(output_path, "WEBP", quality=80)


if __name__ == "__main__":
    # Set your input and output folders
    input_folder = "/home/lakshya/Pictures/nakul"
    output_folder = "/home/lakshya/Pictures/converted"

    # Specify the image file extensions to convert
    image_extensions = [".png", ".jpg", ".JPEG", ".webp", ".WEBP", ".PNG", ".jpeg", ".JPG", ".gif", ".GIF"]

    convert_and_move_webp(input_folder, output_folder, image_extensions)
