import os
import streamlit as st
from PIL import Image
import shutil
import tempfile


def convert_and_move_webp(input_files, output_folder):
    # Create a temporary directory to store converted files
    temp_dir = tempfile.mkdtemp()
    
    # Loop through all uploaded files
    for uploaded_file in input_files:
        # Read image data
        img = Image.open(uploaded_file)
        filename = uploaded_file.name

        # Check if the file is an image
        if uploaded_file.type.startswith('image'):
            # Convert and save as WebP
            output_path = os.path.join(temp_dir, os.path.splitext(filename)[0] + ".webp")
            img.save(output_path, "WEBP", quality=80)

    # Move converted files to the output folder
    shutil.move(temp_dir, output_folder)


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

        # Provide download links for each converted file
        converted_files = os.listdir(output_folder)
        for converted_file in converted_files:
            st.markdown(f"Download [converted file]({os.path.join(output_folder, converted_file)})")


if __name__ == "__main__":
    main()
