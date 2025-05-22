# Twitter Sentiment Analysis using Tweepy & Machine Learning

📌 Overview
This project analyzes Twitter sentiment using Tweepy (Twitter API) and a trained ML model with TfidfVectorizer & Logistic Regression. It fetches tweets in real time, cleans text, and classifies sentiment via an interactive Streamlit web app.

🛠️ Installation
1️⃣ Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/twitter-sentiment-analysis.git  
cd twitter-sentiment-analysis  


2️⃣ Install Dependencies
pip install -r requirements.txt  



⚙️ Usage
1️⃣ Running the Web App
streamlit run app.py  


2️⃣ Training the Model
python train_model.py  



📜 Code Overview
1️⃣ App.py — Twitter Sentiment Analysis
- Fetches real-time tweets using the Twitter API (Tweepy)
- Uses a pre-trained ML model for sentiment analysis
- Implements Streamlit UI components for interactivity
2️⃣ Training Script — Model Training
- Cleans and preprocesses text using NLTK stopwords & PorterStemmer
- Converts text to numerical features using TfidfVectorizer
- Trains a Logistic Regression model for sentiment prediction

📊 Model Training Details
✔ Dataset Preprocessing
✔ Removes special characters using Regex
✔ Applies stemming for improved classification accuracy
✔ Filters stopwords using NLTK
✔ Training the Sentiment Model
✔ Splits data into train-test sets
✔ Uses TfidfVectorizer for feature extraction
✔ Trains a Logistic Regression classifier

🔑 API Configuration
To use Twitter API, replace credentials in app.py:
API_KEY = "your_api_key"  
API_SECRET = "your_api_secret"  
ACCESS_TOKEN = "your_access_token"  
ACCESS_SECRET = "your_access_secret"  



📜 License
This project is open-source under the MIT License.

📞 Contact
For questions or contributions:
📧 Email: your.email@example.com
🐦 Twitter: @yourhandle

🚀 Ready to Go!
Copy and paste this directly into GitHub, and you’re set! 🎯
Let me know if you need any last-minute tweaks! 🚀😊

This project analyzes Twitter sentiment using Tweepy (Twitter API) and a trained ML model with TfidfVectorizer &amp; Logistic Regression. It fetches tweets in real-time, cleans text, and classifies sentiment via an interactive Streamlit web app. Let me know if you'd like any tweaks! 🚀😊
