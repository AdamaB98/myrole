import cv2
import streamlit as st
import numpy as np

def grayscale_image(image):
  """Converts an image to grayscale.

  Args:
      image: A NumPy array representing the image in BGR format.

  Returns:
      A NumPy array representing the grayscale version of the image.
  """
  return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def main():
  """Streamlit application for image processing."""
  st.title("Image Grayscale with OpenCV")
  
  # Upload image using file_uploader
  uploaded_file = st.file_uploader("Choose an image:", type="")

  if uploaded_file is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    grayscale_img = grayscale_image(image)
    
    # Display original and grayscale images using st.image()
    st.subheader("Original Image")
    st.image(image, channels="BGR")  # OpenCV uses BGR format
    st.subheader("Grayscale Image")
    st.image(grayscale_img, channels="grayscale")

if __name__ == "__main__":
  main()

