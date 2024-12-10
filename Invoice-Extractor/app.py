from dotenv import load_dotenv

load_dotenv() # load all env variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

# Load gemini model
model= genai.GenerativeModel("gemini-1.5-flash")

# Function to get response
def get_gemini_response(input, image, prompt):
    response= model.generate_content([input, image[0], prompt])
    return response.text

# Function to interpret image uploaded

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data= uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file Uploaded")


# Streamlit application
st.set_page_config(page_title= "Multilanguage Invoice extractor")
st.header("Multilanguage Invoice extractor")

input = st.text_input("What can I do for you?", key="input")
uploaded_file= st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

image=""

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption= "Uploaded Image", use_container_width=True)

submit= st.button("Go forth and answer my query friend")

input_prompt = """
Role: You are an expert in understanding invoices. Client will upload an image as invoices and you will 
have to answer any question based on the uploaded invoice image.
"""

if submit:
    image_data = input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt, image_data, input)
    st.subheader("The response:")
    st.write(response)