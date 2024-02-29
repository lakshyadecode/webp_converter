import os
import streamlit as st
from PIL import Image
import shutil


def convert_and_move_webp(input_files, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List of supported file extensions
    supported_extensions = (".png", ".jpg", ".jpeg", ".webp", ".png", ".jpeg", ".jpg", ".gif")

    # Loop through all uploaded files
    for uploaded_file in input_files:
        # Read image data
        img = Image.open(uploaded_file)
        filename = uploaded_file.name

        # Check if the file extension is supported
        if filename.lower().endswith(supported_extensions):
            # Convert and save as WebP
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".webp")
            img.save(output_path, "WEBP", quality=80)


def main():
    st.title("Image Converter to WebP")

    # Allow user to select input folder and upload multiple files
    input_files = st.file_uploader("Select Input Folder", type=["png", "jpg", "jpeg", "webp", "PNG", "JPEG", "JPG", "GIF"], accept_multiple_files=True)
    output_folder = st.text_input("Output Folder", "converted")

    if st.button("Convert"):
        if not input_files:
            st.error("Please select an input folder.")
            return

        # Ensure output folder is provided
        if not output_folder:
            st.error("Please specify an output folder.")
            return

        # Convert and save images
        convert_and_move_webp(input_files, output_folder)
        st.success("Conversion completed.")


if __name__ == "__main__":
    main()
