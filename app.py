import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ---------------------------
# Load the model
# ---------------------------
MODEL_PATH = "cat_dog_model.keras"

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(MODEL_PATH)
    return model

model = load_model()

# ---------------------------
# Preprocess image
# ---------------------------
def preprocess_image(image):
    image = image.resize((128, 128))  # MUST match your training size
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = img_array / 255.0      # normalize
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension
    return img_array

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("🐶🐱 Cat vs Dog Classifier")
st.write("Upload an image and the model will predict whether it's a **Cat** or a **Dog**.")

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Predict button
    if st.button("Predict"):
        img_array = preprocess_image(image)
        prediction = model.predict(img_array)[0][0]

        st.write("### Prediction Result:")
        if prediction >= 0.5:
            st.success("🐶 It's a **Dog**!")
        else:
            st.success("🐱 It's a **Cat**!")
