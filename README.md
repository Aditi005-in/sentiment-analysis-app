.

📊 Sentiment Analysis Application

An end-to-end Sentiment Analysis web application built using FastAPI for the backend and Streamlit for the frontend.
This project analyzes user-provided text and predicts the sentiment (Positive / Negative / Neutral) using NLP and machine learning techniques.

🚀 Features

Real-time sentiment prediction

REST API built with FastAPI

Interactive UI built with Streamlit

Clean project structure

Scalable and production-ready architecture

Dataset handled professionally (not included in repo due to size)

🛠 Tech Stack

Python

FastAPI – Backend API

Streamlit – Frontend UI

Scikit-learn – ML model

NLTK / NLP techniques – Text preprocessing

Git & GitHub – Version control

📂 Project Structure
sentiment_analysis/
│
├── backend/
│   ├── app/
│   │   └── main.py          # FastAPI application
│   ├── model/               # Trained ML model
│   ├── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py     # Streamlit UI
│   ├── requirements.txt
│
├── data/                    # Dataset folder (ignored in Git)
│
├── .gitignore
├── README.md

🧠 How the Project Works (Flow)

User enters text in the Streamlit UI

Streamlit sends the text to FastAPI using HTTP request

FastAPI:

Cleans the text (lowercasing, tokenization, stopwords removal, etc.)

Converts text into numerical features

Passes features to the trained ML model

Model predicts sentiment

Result is sent back to Streamlit

Sentiment is displayed to the user

📊 Dataset Information

Due to GitHub’s file size limitations, the dataset is not included in this repository.

Dataset Used

Large sentiment analysis dataset (CSV)

Example: Kaggle Twitter / Movie Review dataset

How to Add Dataset

Download the dataset from the original source

Place it inside:

data/


⚠️ The data/ folder is already added to .gitignore

⚙️ How to Run the Project (Local Setup)
1️⃣ Clone the Repository
git clone https://github.com/Aditi005-in/sentiment-analysis-app.git
cd sentiment-analysis

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

venv\Scripts\activate

3️⃣ Install Backend Dependencies
cd backend
pip install -r requirements.txt

4️⃣ Run FastAPI Backend
uvicorn app.main:app --reload


Backend will run at:

http://127.0.0.1:8000


API Docs:

http://127.0.0.1:8000/docs

5️⃣ Run Streamlit Frontend (New Terminal)
cd frontend
streamlit run streamlit_app.py


Frontend will run at:

http://localhost:8501

🔮 How to Run in Future (Very Important)

Whenever you want to run this project again:

Activate virtual environment

Start backend (FastAPI)

Start frontend (Streamlit)

Ensure dataset is present inside data/

That’s it ✅

🧪 Example API Request
{
  "text": "I really love this product"
}


Response:

{
  "sentiment": "Positive"
}

🧩 Future Improvements

Add authentication

Improve model accuracy

Add more sentiment classes

Dockerize application

Deploy on cloud (AWS / Render)

👤 Author

Aditi Singh
GitHub: https://github.com/Aditi005-in
