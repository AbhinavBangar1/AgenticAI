import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel(model_name='gemini-2.5-flash')
st.title("Not Chat GPT :)")
userInput=st.text_input("How can I help you")
if userInput:
    response = model.generate_content(userInput)
    st.text_area("AI's response : " , response.text , height=500)
    
