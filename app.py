import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pandasai.llm.google_gemini import GoogleGemini
from pandasai import    SmartDataframe
import os

load_dotenv()

llm=GoogleGemini(api_key=os.getenv('GOOGLE_API_KEY'))

def chat_with_csv(df,prompt):
    pandas_ai = SmartDataframe(df,config={'llm':llm})
    result=pandas_ai.chat(prompt)
    return result
      
st.set_page_config(layout='wide')

st.title('ChatCSV powered by LLM')

input_csv=st.file_uploader('upload your csv file',type=['csv'])

if input_csv is not None:
    
    col1,col2=st.columns([1,1])

    with col1:
        st.info('CSV Uploaded successfully')

        data=pd.read_csv(input_csv)
        
        st.dataframe(data)

    with col2:
       st.info('Chat with CSV')

       input_text=st.text_area('Enter your query')

       if input_text is not None:
           if st.button('Chat with CSV'):
              st.info(f'Your query: {input_text}')
              result=chat_with_csv(data,input_text)
              st.success(result)
