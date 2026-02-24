import streamlit as st
import requests

def get_essay_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}})
    
    return response.json()['output']['content']


def get_poem_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", json={"input": {"topic": input_text}})
    
    return response.json()['output']


#streamlit

st.title("Langchain API Client")
input_text = st.text_input("Enter your essay topic here")
input_text1 = st.text_input("Enter your poem topic here")

if input_text:
    st.write(get_essay_response(input_text))
    
if input_text1:
    st.write(get_poem_response(input_text1))    
    
    
