from textblob import TextBlob as tb
import streamlit as st
import pandas as pd
import numpy as np
import cleantext
from index import main,load_conf


# Title
st.title("Sentiment Analizer App")

# Sidebar
st.sidebar.header("Settings")
keyword=st.sidebar.text_input("Enter a key word")

# Main content

with st.expander('Analyze text'):
    text=st.text_input('Text here: ')
    if text:
        blob=tb(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))

    
    
with st.expander('Analyze csv'):
    file=st.file_uploader('Upload file: ')
    if file:
        dataFrame=pd.read_excel(file)
        #dataFrame['score']= dataFrame['tweets'].apply(score)
        #dataFrame['analysis']=dataFrame['score'].apply(analyze)
        st.write(dataFrame.head())
        
#linking test:
if st.button("Search"):
    st.write(keyword)
    with st.spinner('Searching...'):
        conf = load_conf()
        main(keyword, conf)