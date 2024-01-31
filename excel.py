# Writing to an excel
# sheet using Python
import pandas as pd
from textblob import TextBlob as tb
from xlwt import Workbook
import streamlit as st

def Excel(
    data: list,
    output: list
):
    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    for i, row in enumerate(output):
        sheet1.write(0, i, row)

    for i, row in enumerate(data):
        for j, cell in enumerate(output):
            sheet1.write(i+1, j, row[cell])
        print(row)

    wb.save('Excel.xls')
    # Replace 'Excel.xls' with the actual path to your Excel file
    process_excel_file('Excel.xls')


#sentiment analysis:
def score(paragraph):
    blobs = tb(paragraph).sentences
    # Analyze sentiment for each sentence
    sentence_polarities = [blob.sentiment.polarity for blob in blobs]
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
    

def process_excel_file(file_path: str):
    # Read the Excel file into a DataFrame
    dataFrame = pd.read_excel(file_path)

    # Apply the 'score' function to the 'tweets' column
    dataFrame['score'] = dataFrame['Text'].apply(score)

    # Apply the 'analyze' function to the 'score' column
    dataFrame['analysis'] = dataFrame['score'].apply(analyze)

    # Display the resulting DataFrame
    print(dataFrame.head())

