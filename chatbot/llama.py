from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT_NAME")

## prompt

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. please response to the query"),
        ("user", "Question: {question}")
    ]
)


# streamlit app

st.title("Langchain Ollama Chatbot")
input_text = st.text_input("Enter your question here")

# Ollama llm

llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))


