import streamlit as st
from textblob import TextBlob

st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🤖"
)

st.title("🤖 AI Sentiment Analyzer")
st.write("Enter a sentence and let the AI analyze its sentiment.")

text = st.text_area(
    "Enter your text:",
    placeholder="Example: I really enjoyed this movie!"
)

if st.button("Analyze Sentiment"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "😊 Positive"
        elif polarity < 0:
            sentiment = "😞 Negative"
        else:
            sentiment = "😐 Neutral"

        st.subheader("AI Prediction")
        st.success(sentiment)

        st.write("Sentiment Score:", round(polarity, 2))
