from textblob import TextBlob as tb
import streamlit as st
import pandas as pd
import numpy as np
import cleantext

# Create a placeholder DataFrame for testing
data = {'Column1': np.random.rand(10), 'Column2': np.random.randint(0, 100, 10)}
my_data = pd.DataFrame(data)

# Title
st.title("Sentiment Analizer App")

# Sidebar
st.sidebar.header("Settings")
st.sidebar.text_input("Enter a key word")

# Main content

with st.expander('Analyze text'):
    text=st.text_input('Text here: ')
    if text:
        blob=tb(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))

    

def score(paragraph):
    sentences = tb(paragraph).sentences
    # Analyze sentiment for each sentence
    sentence_polarities = [sentence.sentiment.polarity for sentence in sentences]
    return  sum(sentence_polarities) / len(sentence_polarities)

def analyze(x):
    if x>=0.5:
        return 'Great'
    elif x<=-0.5:
        return 'Bad'
    elif x>-0.5 and x<0:
        return 'Mid'
    elif x==0:
        return 'Neutral'
    else:
        return 'good'
    
with st.expander('Analyze csv'):
    file=st.file_uploader('Upload file: ')
    if file:
        dataFrame=pd.read_excel(file)
        dataFrame['score']= dataFrame['tweets'].apply(score)
        dataFrame['analysis']=dataFrame['score'].apply(analyze)
        st.write(dataFrame.head())
        

