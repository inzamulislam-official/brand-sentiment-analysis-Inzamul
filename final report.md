# Final Report

## Brand Sentiment Analysis Using Transformer-Based AI

### 1. Problem Solved

The project addresses the problem of manually interpreting large volumes of brand-related customer opinions. Manual sentiment classification is time-consuming, inconsistent, and difficult to scale. The implemented solution automates this process by applying a pre-trained Transformer-based Natural Language Processing (NLP) model to customer review text and classifying each review as **Positive, Negative, or Neutral**.

The final application provides both **individual review-level sentiment predictions** and an **aggregate brand-level sentiment summary**, allowing users to quickly interpret the overall sentiment distribution.

---

### 2. System Design and Architecture

The application was implemented in Python using **Streamlit** as the application layer. The system follows a simple sequential processing architecture:

**Brand Selection → Review Dataset → Transformer Model → Sentiment Classification → Data Processing → Visualization**

The application currently supports multiple predefined brands, including Samsung, Nike, Apple, Adidas, Coca-Cola, Pepsi, Grameenphone, and Daraz. Each brand contains a set of representative customer reviews used as the input dataset.

A `selectbox` interface was implemented instead of unrestricted text input. This design decision ensures that the selected brand always has an associated review dataset and prevents invalid brand names from producing misleading results.

---

### 3. AI Workflow

The core AI component uses the Hugging Face Transformers library with the pre-trained:

**`cardiffnlp/twitter-roberta-base-sentiment-latest`**

model.

The model is based on the RoBERTa Transformer architecture and is designed for sentiment classification of short, informal, and social-media-style text.

The implemented workflow is:

1. The Transformer sentiment-analysis pipeline is initialized.
2. The user selects a brand from the available dataset.
3. The corresponding review collection is loaded.
4. Each review is passed independently to the Transformer pipeline.
5. The model returns a sentiment label and confidence score.
6. The raw model output is mapped into the application-level labels:

   * `positive` → **Positive**
   * `negative` → **Negative**
   * `neutral` → **Neutral**
7. Confidence values are converted into percentages.
8. All predictions are stored in a Pandas DataFrame.
9. Aggregate sentiment statistics are calculated.
10. Results are displayed through Streamlit metrics, Plotly visualization, and a detailed analysis table.

The model is loaded through Streamlit's `@st.cache_resource` mechanism. This prevents the Transformer model from being repeatedly initialized during application reruns and improves application responsiveness.

---

### 4. Data Processing and Analysis

The current implementation uses a controlled sample-review dataset rather than a live external API. This was intentionally selected to keep the project focused on the AI inference pipeline and application architecture without introducing API dependency, authentication, rate-limit, or data-quality issues.

For every review, the system stores:

* Original review text
* Predicted sentiment
* Model confidence score

Pandas is used to structure and process the prediction results.

The application calculates:

**Positive Percentage**

`Positive Reviews / Total Reviews × 100`

**Negative Percentage**

`Negative Reviews / Total Reviews × 100`

**Neutral Percentage**

`Neutral Reviews / Total Reviews × 100`

These calculations provide an aggregate view of the selected brand's sentiment distribution.

---

### 5. Visualization and User Interface

The interface was developed using Streamlit to provide a lightweight interactive web application without requiring a separate frontend framework.

The dashboard contains four primary KPI metrics:

* **Total Reviews**
* **Positive Reviews**
* **Negative Reviews**
* **Neutral Reviews**

A Plotly pie chart provides a visual representation of the sentiment distribution, while a detailed DataFrame displays the prediction for every individual review along with its confidence score.

This combination provides both **high-level business interpretation** and **review-level technical transparency**.

The design prioritizes simplicity so that users without technical or NLP knowledge can understand the output while still exposing the underlying prediction results.

---

### 6. Technical Design Decisions

Several implementation decisions were made to balance functionality, development time, and technical reliability.

**Pre-trained Transformer instead of custom training:**
Training a sentiment model from scratch would require a large labeled dataset, model-training infrastructure, hyperparameter tuning, and considerably more development time. Using a pre-trained RoBERTa model allows the project to directly perform inference while demonstrating practical Transformer-based NLP implementation.

**Streamlit:**
Streamlit was selected because it allows the Python-based AI pipeline to be converted into an interactive web application without building a separate frontend and backend architecture.

**Cached model loading:**
`@st.cache_resource` was used to avoid repeatedly loading the Transformer model whenever Streamlit reruns the application.

**Pandas:**
Pandas provides a structured format for storing predictions and performing sentiment aggregation.

**Plotly:**
Plotly was selected for interactive visualization of sentiment distributions.

**Git/GitHub:**
Git was used for version control and GitHub for repository management, documentation, and maintaining the project source code.

---

### 7. Results

The completed system successfully performs automated sentiment inference across the implemented brand datasets.

For each selected brand, the system produces:

* Review-level sentiment classifications
* Confidence scores
* Positive/Negative/Neutral counts
* Sentiment percentages
* Interactive sentiment distribution visualization
* Detailed prediction table

The system therefore fulfills the core technical requirement of transforming unstructured review text into structured sentiment information through a Transformer-based AI model.

The implementation also demonstrates that a pre-trained NLP model can be integrated into a functional business-oriented application with relatively little infrastructure while maintaining a clear separation between **input data, AI inference, data processing, and presentation**.

---

### 8. Limitations and Future Improvement

The primary limitation of the current implementation is the use of predefined sample reviews rather than continuously collected real-world data. Consequently, the application currently demonstrates the sentiment-analysis workflow rather than providing real-time market sentiment monitoring.

A production-level version could extend the system by integrating review APIs, social media data sources, or a continuously updated database. Additional improvements could include multilingual sentiment analysis, larger datasets, sentiment trends over time, aspect-based sentiment analysis, keyword extraction, and brand-to-brand comparison.

Model evaluation could also be expanded using a labeled test dataset to measure accuracy, precision, recall, and F1-score instead of relying only on model confidence values.

---

### 9. Conclusion

The project successfully implements an end-to-end **Transformer-based Brand Sentiment Analysis system** using Python, Hugging Face Transformers, Streamlit, Pandas, and Plotly.

The final architecture demonstrates the complete pipeline from textual input to AI inference, structured data processing, statistical aggregation, and interactive visualization. The use of a pre-trained RoBERTa sentiment model provides the NLP intelligence, while Streamlit converts the model into a practical user-facing application.

Overall, the project demonstrates a practical application of modern Transformer-based NLP for converting customer opinions into structured and interpretable business insights.
