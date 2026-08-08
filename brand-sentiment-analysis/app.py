import streamlit as st
from transformers import pipeline
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Brand Sentiment Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Brand Sentiment Analysis")
st.write(
    "কোনো ব্র্যান্ড নির্বাচন করলে তার সম্পর্কে ইউজার রিভিউ/মতামতের "
    "সেন্টিমেন্ট অ্যানালাইসিস দেখাবে।"
)

# Model Load
@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )

classifier = load_model()

# Sample Reviews
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
    ],

    "Apple": [
        "iPhone has an amazing camera and smooth performance.",
        "The battery life is disappointing.",
        "Apple products are reliable and premium.",
        "The price is way too high.",
        "I love the new iPhone design.",
        "Customer support was extremely helpful.",
        "The latest update made my phone slower.",
        "Best smartphone experience I have had.",
        "The ecosystem is incredibly convenient.",
        "Very expensive compared to other phones."
    ],

    "Adidas": [
        "Adidas shoes are extremely comfortable.",
        "The quality is excellent for the price.",
        "The shoes started wearing out quickly.",
        "Great designs and very stylish.",
        "Sizing was completely wrong.",
        "Perfect shoes for everyday use.",
        "The new collection looks amazing.",
        "Too expensive for a pair of sneakers.",
        "Very durable and comfortable for running.",
        "I expected better quality."
    ],

    "Coca-Cola": [
        "Coca-Cola tastes refreshing and delicious.",
        "Too much sugar makes it unhealthy.",
        "My favorite soft drink for years.",
        "The taste is not as good as it used to be.",
        "Perfect drink with burgers and pizza.",
        "I love the classic Coca-Cola flavor.",
        "Too sweet for my taste.",
        "Great taste and refreshing experience.",
        "The price has increased too much.",
        "One of the best soft drinks ever."
    ],

    "Pepsi": [
        "Pepsi tastes really refreshing.",
        "I prefer Pepsi over other soft drinks.",
        "Way too sweet for me.",
        "Great taste when served cold.",
        "The flavor is not consistent.",
        "Perfect drink for parties.",
        "I love the new Pepsi campaign.",
        "Not worth the price anymore.",
        "Very refreshing on a hot day.",
        "Coca-Cola tastes better than Pepsi."
    ],

    "Grameenphone": [
        "Grameenphone has excellent network coverage.",
        "Internet speed is very slow in my area.",
        "Customer service was very helpful.",
        "Their data packages are too expensive.",
        "The network works well almost everywhere.",
        "I am disappointed with the call quality.",
        "Good internet speed and reliable service.",
        "Packages should offer more data.",
        "Best network coverage in Bangladesh.",
        "Customer support took too long to respond."
    ],

    "Daraz": [
        "Daraz has a huge variety of products.",
        "Delivery was very late.",
        "I received exactly what I ordered.",
        "Customer service was disappointing.",
        "Great discounts during the campaign.",
        "The product quality was excellent.",
        "The seller sent a completely different product.",
        "Easy shopping experience and fast delivery.",
        "Prices are sometimes higher than other stores.",
        "I am very happy with my purchase."
    ]
}

# Brand Selection
brand = st.selectbox(
    "ব্র্যান্ড নির্বাচন করুন",
    list(sample_reviews.keys()),
    index=0
)

# Analyze Button
if st.button("Analyze Sentiment", type="primary"):

    with st.spinner("Analyzing sentiment..."):

        reviews = sample_reviews[brand]

        results = []

        for review in reviews:

            res = classifier(review)[0]

            label = res["label"]
            score = res["score"]

            # Label Mapping
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

        # Summary
        positive = len(df[df["Sentiment"] == "Positive"])
        negative = len(df[df["Sentiment"] == "Negative"])
        neutral = len(df[df["Sentiment"] == "Neutral"])
        total = len(df)

        # Metrics
        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Reviews",
            total
        )

        col2.metric(
            "Positive",
            f"{positive} ({positive / total * 100:.1f}%)"
        )

        col3.metric(
            "Negative",
            f"{negative} ({negative / total * 100:.1f}%)"
        )

        col4.metric(
            "Neutral",
            f"{neutral} ({neutral / total * 100:.1f}%)"
        )

        # Sentiment Chart
        fig = px.pie(
            names=["Positive", "Negative", "Neutral"],
            values=[positive, negative, neutral],
            title=f"{brand} Sentiment Distribution",
            color_discrete_sequence=[
                "#00C853",
                "#D50000",
                "#FFD600"
            ]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Detailed Analysis
        st.subheader("Detailed Analysis")

        st.dataframe(
            df,
            use_container_width=True
        )