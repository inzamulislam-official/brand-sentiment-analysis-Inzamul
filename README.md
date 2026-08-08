# Brand Sentiment Analysis

A web application that analyzes public sentiment towards different brands using AI.

## Features
- Real-time sentiment analysis using RoBERTa model
- Positive / Negative / Neutral classification
- Interactive pie chart visualization
- Clean and user-friendly interface

## Tech Stack
- Frontend & Backend: Streamlit
- AI Model: cardiffnlp/twitter-roberta-base-sentiment-latest
- Visualization: Plotly

## How to Run Locally
```bash
pip install streamlit transformers torch pandas plotly
streamlit run app.py
