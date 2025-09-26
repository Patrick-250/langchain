from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate
import streamlit as st

load_dotenv()
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]

model=init_chat_model(model="gpt-4o-mini",model_provider="openai")

prompt_template=PromptTemplate(
    input_variables=["country","budget","month"],
    template="""
    you are an experience travel guide to help tourists navigate and plan trips.
    you need to take into account of their destination {country},visiting {month}, and {budget} in US dollars. with this information, 
    suggest local food to try, useful phrases to navigate around,must visit attractions.
    
    """
)

st.title("Travel guide")
country=st.text_input("Enter your destination country")
budget=st.number_input("Enter your Budget")
month=st.text_input("enter the month u travelling")

if country and budget and month:
    response=model.invoke(prompt_template.format(country=country,budget=budget,month=month))
    st.write(response.content)




