from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import os
load_dotenv()

import google.generativeai as genai
st.set_page_config(page_title="Drishti")
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


# --- SIDEBAR SECTION ---
with st.sidebar:
    st.title("About Drishti")
    st.write("Developed by **Disha**")
    st.info("Drishti resembles Vision . This tool uses Gemini 3.1 to provide a 'New Direction' to image analysis.")


    st.divider()
    st.markdown("### Connect with me:")
    # Replace these with your actual links before pushing to GitHub/LinkedIn
    st.markdown("[🔗 LinkedIn]https://www.linkedin.com/in/gecdhd-comp-disha-rasdhari/")
    st.markdown("[📂 GitHub]https://github.com/rasdharidisha-280306")

def get_gemini_response(input,image):
    model = genai.GenerativeModel("gemini-3.1-flash-lite")
    if input !="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


st.header("Drishti: Your Visual AI Guide")
input = st.text_input("Input Prompt:" , key = "input")
uploaded_file = st.file_uploader("Upload an image",type=["jpg","jpeg","png"])
image =""
if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
submit = st.button("Generate Response")


if submit:
    if input.strip() != "" or uploaded_file is not None:
        # 1. Shows the loading spinner to the user
        with st.spinner("Drishti is analyzing..."):
            try:
                # 2. Tries to call the Gemini AI
                response = get_gemini_response(input, image)
                st.subheader("Response:")
                st.write(response)
            except Exception as e:
                # 3. Catches quota/rate-limit errors gracefully without crashing
                if "429" in str(e) or "Quota" in str(e) or "quota" in str(e).lower():
                    st.error("Drishti is resting! The free AI quota limit was temporarily reached. Please try again later or tomorrow.")
                else:
                    st.error(f"An error occurred: {e}")
    else:
        st.warning("Please give a prompt or upload an image first!")