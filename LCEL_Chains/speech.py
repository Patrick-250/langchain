import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]

llm=init_chat_model(model="gpt-4o-mini",model_provider="openai")

title_template=PromptTemplate(
    input_variables=["topic"],
    template="""
    you are an expert in speech writing. you must craft an impactful title for a speech on {topic}.
    provide exacly just the  title for the speech

    """
)

speech_template=PromptTemplate(
    input_variables=["title"],
    template="""
    you are an expert in speech writing.you need to write a powerful speech of 200 words for the following title: {title}
    
    """


)



first_chain=title_template | llm | StrOutputParser()
second_chain=speech_template | llm 
final_chain=first_chain | second_chain 

st.title("Speech Generator")
topic=st.text_input("Enter the topic")



if topic:
    response=final_chain.invoke({"topic":topic})
    st.write(response.content)