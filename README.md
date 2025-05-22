# Twitter Sentiment Analysis using Tweepy & Machine Learning

## 📌 Overview
This project analyzes Twitter sentiment using Tweepy (Twitter API) and a trained ML model with TfidfVectorizer & Logistic Regression. It fetches tweets in real time, cleans text, and classifies sentiment via an interactive Streamlit web app.

## 🛠️ Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/twitter-sentiment-analysis.git  
cd twitter-sentiment-analysis
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```  



## ⚙️ Usage
### 1️⃣ Running the Web App
```sh
streamlit run app.py  
```  

### 2️⃣ Training the Model
```sh
python train_model.py  
```  


## 📜 Code Overview
### 1️⃣ App.py — Twitter Sentiment Analysis
- Fetches real-time tweets using the Twitter API (Tweepy)
- Uses a pre-trained ML model for sentiment analysis
- Implements Streamlit UI components for interactivity
### 2️⃣ Training Script — Model Training
- Cleans and preprocesses text using NLTK stopwords & PorterStemmer
- Converts text to numerical features using TfidfVectorizer
- Trains a Logistic Regression model for sentiment prediction

## 📊 Model Training Details
### ✔ Dataset Preprocessing
✔ Removes special characters using Regex
✔ Applies stemming for improved classification accuracy
✔ Filters stopwords using NLTK
### ✔ Training the Sentiment Model
✔ Splits data into train-test sets
✔ Uses TfidfVectorizer for feature extraction
✔ Trains a Logistic Regression classifier

## 🔑 API Configuration
```sh
To use Twitter API, replace credentials in app.py:
API_KEY = "your_api_key"  
API_SECRET = "your_api_secret"  
ACCESS_TOKEN = "your_access_token"  
ACCESS_SECRET = "your_access_secret"
```  


## 📜 License
This project is open-source under the MIT License.

## 📞 Contact
For questions or contributions:
📧 Email: nishchalanigam6291@gmail.com
🐦 Twitter: @Nishchala17

