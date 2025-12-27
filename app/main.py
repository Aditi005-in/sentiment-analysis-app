from fastapi import FastAPI
from app.predict import predict_sentiment

app = FastAPI(title="Sentiment Analysis API")

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running"}

@app.post("/predict")
def predict(text: str):
    sentiment = predict_sentiment(text)
    return {
        "input_text": text,
        "sentiment": sentiment
    }
