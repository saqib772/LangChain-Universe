#Integrate code with OpenAI
import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

#streamlit framework
st.title('Langchain Demo with OpenAI')
input_text=st.text_input('Search the topic U want ')

#openai LLMS

llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))


