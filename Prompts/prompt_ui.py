from langchain_openai import OpenAIEmbeddings
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header('Research Tool')
user_input = st.text_input("Enter your research query here:")

if st.button("Submit"):
    st.text('Some random text')
