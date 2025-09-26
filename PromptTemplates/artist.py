import os
from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate




load_dotenv()
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]

model=init_chat_model(model="gpt-4o-mini",model_provider="openai")

prompt_template=PromptTemplate(
    input_variables=["country","number_of_words"],
    template="""
    You are a professional songwriter/singer from {country}.
You create music that blends local culture with modern styles like Afrobeat, R&B
 your voice should reflect the accent and emotion typical of singers from {country}.
your song should be actual song blending english with traditional language from {country}. your song should not be more than {number_of_words} words.
answer the question: create a chorus for my smooth melodic afrobeat club song. Avoid giving the chorus for fictional or non existent countries, if the country is finctional or doesnt exist; simply answer "I appreciate the curiosity but i cannot create the song from that place lol"
    
    """
)

st.title("ask your AI writer/singer")

country=st.text_input("Enter your country and press enter")
number_of_words=st.number_input("enter no of words for ur song", min_value=1,max_value=40)

if country and number_of_words:
    response=model.invoke(prompt_template.format(country=country,number_of_words=number_of_words))
    st.write(response.content)

