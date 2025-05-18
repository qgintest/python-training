import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

if not uploaded_image:
    with st.expander("Start Camera"):
        # launched camera
        camera_image = st.camera_input("Camera")
        print(camera_image)

    if camera_image:
        # create pillow image instance
        img = Image.open(camera_image)

        # convert the pillow image to greyscale
        gray_img = img.convert("L")

        # Render the greyscale image on the webpage
        st.image(gray_img)
else:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)




