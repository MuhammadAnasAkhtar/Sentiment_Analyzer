import torch
import gradio as gr
from transformers import pipeline

# Initialize the sentiment-analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Define a function to analyze text sentiment
def analyze_sentiment(input_text):
    # Get the result from the pipeline
    result = sentiment_analysis(input_text)
    # Extract label (e.g., Positive/Negative) and confidence score
    label = result[0]['label']
    confidence = round(result[0]['score'] * 100, 2)
    return f"Sentiment: {label} (Confidence: {confidence}%)"

# Set up the Gradio interface
gr.close_all()

Demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=[gr.Textbox(label="Enter Text for Sentiment Analysis", lines=5)],
    outputs=[gr.Textbox(label="Sentiment Analysis Result", lines=2)],
    title="Sentiment Analysis App",
    description="This application performs sentiment analysis to determine whether the text is positive or negative."
)

# Launch the app with a public link
Demo.launch()
