from PyPDF2 import PdfReader
import streamlit as st

st.title("PDF Reader")

pdf_file=st.file_uploader("Upload PDF file : ",type='pdf')
if pdf_file is not None:
    reader = PdfReader(pdf_file)
    text=''
    for page in reader.pages:
        text+=page.extract_text()
    
    st.text_area("Text Extracted from PDF file",text,height=500)

