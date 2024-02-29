import os
import shutil
import streamlit as st
from PIL import Image


def convert_and_move_webp(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            # Convert and save as WebP
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".webp")
            convert_to_webp(input_path, output_path)

        elif filename.lower().endswith(".webp"):
            # Move WebP files directly to the output folder
            output_path = os.path.join(output_folder, filename)
            shutil.copy(input_path, output_path)


def convert_to_webp(input_path, output_path):
    # Load the image
    img = Image.open(input_path)

    # Save as WebP
    img.save(output_path, "WEBP", quality=80)


def main():
    st.title("Image Converter to WebP")

    input_folder = st.sidebar.selectbox("Select Input Folder", os.listdir())
    output_folder = st.sidebar.text_input("Output Folder", "converted")

    if st.sidebar.button("Convert"):
        if not input_folder:
            st.error("Please select an input folder.")
            return
        if not os.path.exists(input_folder):
            st.error("Input folder does not exist.")
            return

        convert_and_move_webp(input_folder, output_folder)
        st.success("Conversion completed.")


if __name__ == "__main__":
    main()
