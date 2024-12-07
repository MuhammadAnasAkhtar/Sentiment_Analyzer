import torch
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

analyzer = pipeline("text-classification",
                model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def sentiment_analyzer(review):
    # Check if the review is a valid string
    if pd.isna(review) or not isinstance(review, str):
        return "NEUTRAL"  # Return neutral for invalid inputs
    try:
        sentiment = analyzer(review)
        return sentiment[0]['label']
    except:
        return "NEUTRAL"  # Return neutral for any errors

def sentiment_bar_chart(df):
    sentiment_counts = df['Sentiment'].value_counts()
    
    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%', 
            colors=['lightgreen', 'lightcoral', 'lightgray'])
    plt.title('Review Sentiment Distribution')
    return plt.gcf()

def read_reviews_and_analyze_sentiment(file_object):
    try:
        # Load the Excel file into a DataFrame
        df = pd.read_excel(file_object)
        
        # Check if 'Review' column is in the DataFrame
        if 'Review' not in df.columns:
            raise ValueError("Excel file must contain a 'Review' column.")
        
        # Convert Review column to string type and handle NaN values
        df['Review'] = df['Review'].astype(str)
        
        # Apply the sentiment_analyzer function to each review
        df['Sentiment'] = df['Review'].apply(sentiment_analyzer)
        
        # Create the chart
        chart_object = sentiment_bar_chart(df)
        
        return df, chart_object
    except Exception as e:
        raise gr.Error(f"Error processing file: {str(e)}")

# Create the Gradio interface
demo = gr.Interface(
    fn=read_reviews_and_analyze_sentiment,
    inputs=[gr.File(file_types=["xlsx"], label="Upload your review comment file")],
    outputs=[
        gr.Dataframe(label="Sentiments"),
        gr.Plot(label="Sentiment Analysis")
    ],
    title="@GenAILearniverse Project 3: Sentiment Analyzer",
    description="THIS APPLICATION WILL BE USED TO ANALYZE THE SENTIMENT BASED ON FILE UPLOADED."
)

if __name__ == "__main__":
    demo.launch()
