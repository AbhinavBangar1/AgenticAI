import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#print(os.getenv("GEMINI_API_KEY"))

'''

model = genai.GenerativeModel(model_name='gemini-2.5-flash')
while True :
    userInput=input("How can I help you : ")
    if (userInput=="q" or "Q" or "Quit" or "quit"):
         break
    response = model.generate_content(userInput)
    print(respone.text)

'''

model = genai.GenerativeModel(model_name='gemini-2.5-flash')
st.title("Not Chat GPT :)")
#while True :
userInput=st.text_input("How can I help you")
    # if (userInput=="q" or "Q" or "Quit" or "quit"):
    #     break
if userInput:
    response = model.generate_content(userInput)
    st.text_area("AI's response : " , response.text , height=500)
    
