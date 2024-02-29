import os
import subprocess
import shutil
from time import perf_counter
import streamlit as st

# Global namespace
dir_name = 'webp'
extensions = ('.png', '.jpg', '.jpeg')


def get_images(file_list):
    """Filter out images from the uploaded file list."""
    images = [file for file in file_list if file.name.lower().endswith(extensions)]
    return images


def convert_to_webp(image):
    """Convert the image to WebP format."""
    try:
        quality = 80
        output_file = f"{image.name.split('.')[0]}.webp"
        command = f'cwebp -q {quality} "{image.name}" -o "{output_file}"'
        subprocess.run(command, shell=True, check=True)
        return output_file
    except Exception as e:
        st.error(f"Error converting {image.name}: {e}")
        return None


def main():
    st.title("Image Converter to WebP")

    uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True)

    if uploaded_files:
        st.write("Converting...")

        start_time = perf_counter()
        webp_files = []
        for uploaded_file in uploaded_files:
            webp_file = convert_to_webp(uploaded_file)
            if webp_file:
                webp_files.append(webp_file)

        if webp_files:
            st.write("Conversion completed.")
            st.write("Download WebP files:")
            for webp_file in webp_files:
                st.write(f"[{webp_file}]({webp_file})")

        elapsed_time = perf_counter() - start_time
        st.write(f"Task completed in {elapsed_time:.4f}s")


if __name__ == "__main__":
    main()
