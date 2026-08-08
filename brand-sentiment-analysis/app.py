import streamlit as st
from transformers import pipeline
import pandas as pd
import plotly.express as px

# পেজ কনফিগ
st.set_page_config(page_title="Brand Sentiment Analysis", page_icon="📊", layout="wide")

st.title("📊 Brand Sentiment Analysis")
st.write("কোনো ব্র্যান্ডের নাম দিলে তার সম্পর্কে ইউজার রিভিউ/মতামতের সেন্টিমেন্ট অ্যানালাইসিস দেখাবে।")

# মডেল লোড (একবারই লোড হবে)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

classifier = load_model()

# ইউজার ইনপুট
brand = st.text_input("ব্র্যান্ডের নাম লিখুন (উদাহরণ: Samsung, Nike, Grameenphone)", "Samsung")

# স্যাম্পল রিভিউ (রিয়েল API না নিয়ে স্যাম্পল দিয়ে দ্রুত কাজ করানো হয়েছে)
sample_reviews = {
    "Samsung": [
        "Samsung Galaxy is amazing, best camera ever!",
        "Battery life is terrible, drains so fast.",
        "Great value for money, highly recommended.",
        "Software updates are slow and buggy.",
        "Love the design and display quality.",
        "Customer service is very poor.",
        "Outstanding performance, no lag at all.",
        "Overheating issue is very annoying.",
        "Best smartphone I have ever used.",
        "Not worth the price, many better options."
    ],
    "Nike": [
        "Nike shoes are super comfortable and stylish.",
        "Quality has gone down recently.",
        "Perfect for running, highly durable.",
        "Too expensive for what you get.",
        "Love the new collection!",
        "Sole started coming off after 2 months.",
        "Best sports brand ever.",
        "Sizing is inconsistent.",
        "Great for gym workouts.",
        "Not as good as Adidas."
    ]
}

if st.button("Analyze Sentiment", type="primary"):
    with st.spinner("Analyzing..."):
        reviews = sample_reviews.get(brand, sample_reviews["Samsung"])
        
        results = []
        for review in reviews:
            res = classifier(review)[0]
            label = res['label']
            score = res['score']
            
            # লেবেল ম্যাপ
            if label == "positive":
                sentiment = "Positive"
            elif label == "negative":
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
                
            results.append({
                "Review": review,
                "Sentiment": sentiment,
                "Confidence": round(score * 100, 2)
            })
        
        df = pd.DataFrame(results)
        
        # সামারি
        positive = len(df[df["Sentiment"] == "Positive"])
        negative = len(df[df["Sentiment"] == "Negative"])
        neutral = len(df[df["Sentiment"] == "Neutral"])
        total = len(df)
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Reviews", total)
        col2.metric("Positive", f"{positive} ({positive/total*100:.1f}%)")
        col3.metric("Negative", f"{negative} ({negative/total*100:.1f}%)")
        col4.metric("Neutral", f"{neutral} ({neutral/total*100:.1f}%)")
        
        # চার্ট
        fig = px.pie(
            names=["Positive", "Negative", "Neutral"],
            values=[positive, negative, neutral],
            title=f"{brand} Sentiment Distribution",
            color_discrete_sequence=["#00C853", "#D50000", "#FFD600"]
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # টেবিল
        st.subheader("Detailed Analysis")
        st.dataframe(df, use_container_width=True)