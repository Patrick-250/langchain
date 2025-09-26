import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate
import streamlit as st

load_dotenv()
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]

model=init_chat_model(model="gpt-4o-mini",model_provider="openai")

prompt_template=PromptTemplate(
    input_variables=["job_title","job_description","years_of_experience"],



    template="""
    you are an expert interview helper to help people prepare for their interviews based on {job_description}
    you will use {job_title}, {years_of_experience} and {job_description} to provide the interviewee with areas of focus and sample interview questions and answers.


    """

)

job_title=st.text_input("enter job title")
job_description=st.text_area("enter job description")
years_of_experience=st.number_input("enter years of experience")

chain=prompt_template | model

if job_title and job_description and years_of_experience:
    response=chain.invoke({"job_title":job_title,"job_description":job_description,"years_of_experience":years_of_experience})
    st.write(response.content)
