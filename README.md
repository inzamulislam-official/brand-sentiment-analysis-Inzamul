# Brand Sentiment Analysis

A web application that analyzes public sentiment towards different brands using AI (Transformer-based model).

## Live Demo
**[Click here to use the app](https://brand-sentiment-analysis-inzamul-fvugdtzcwfynknwvrnmbfk.streamlit.app/)**

## Features
- Real-time sentiment analysis of brand-related reviews
- Classifies into **Positive**, **Negative**, and **Neutral**
- Confidence score for each prediction
- Interactive Pie Chart visualization
- Clean and simple user interface

## AI Model Used
- Model: `cardiffnlp/twitter-roberta-base-sentiment-latest`
- Type: RoBERTa-based Transformer model fine-tuned for sentiment analysis
- Framework: Hugging Face Transformers

## Tech Stack
- **Frontend + Backend**: Streamlit
- **AI/ML**: Hugging Face Transformers + PyTorch
- **Visualization**: Plotly
- **Deployment**: Streamlit Community Cloud

## How to Run Locally
```bash
pip install streamlit transformers torch pandas plotly
streamlit run app.py
