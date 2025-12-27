import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sentiment Analysis Platform",
    page_icon="🧠",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

.main {
    background-color: #f5f7fb;
}

.title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    color: #1f2937;
}

.subtitle {
    font-size: 18px;
    text-align: center;
    color: #6b7280;
    margin-bottom: 40px;
}

.card {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 14px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06);
    margin-bottom: 30px;
}

.result-positive {
    background-color: #e6f9f0;
    color: #067647;
    padding: 18px;
    border-radius: 12px;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
}

.result-negative {
    background-color: #fdecea;
    color: #b42318;
    padding: 18px;
    border-radius: 12px;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
}

.result-neutral {
    background-color: #eef2ff;
    color: #3730a3;
    padding: 18px;
    border-radius: 12px;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
}

.footer {
    text-align: center;
    font-size: 14px;
    color: #6b7280;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>🧠 Sentiment Analysis Platform</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>AI-powered sentiment classification using NLP & Machine Learning</div>",
    unsafe_allow_html=True
)

# ---------------- INPUT CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📝 Analyze Text")

user_text = st.text_area(
    "Enter text below",
    placeholder="Example: The movie was average but had great visuals.",
    height=140
)

analyze = st.button("Analyze Sentiment", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RESULT ----------------
if analyze:
    if user_text.strip() == "":
        st.warning("Please enter some text for analysis.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                params={"text": user_text},
                timeout=10
            )

            sentiment = response.json()["sentiment"].lower()

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("📊 Result")

            if sentiment == "positive":
                st.markdown("<div class='result-positive'>😊 Positive Sentiment</div>", unsafe_allow_html=True)
            elif sentiment == "negative":
                st.markdown("<div class='result-negative'>😞 Negative Sentiment</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='result-neutral'>😐 Neutral Sentiment</div>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        except Exception:
            pass

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>Built this using NLP · FastAPI · Machine Learning · Python</div>",
    unsafe_allow_html=True
)

