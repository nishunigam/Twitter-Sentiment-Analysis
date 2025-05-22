import streamlit as st
import tweepy
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download and cache NLTK resources
@st.cache_resource
def load_nltk_resources():
    nltk.download('vader_lexicon')
    return SentimentIntensityAnalyzer()

# Twitter API authentication (Replace with your credentials)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"


auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Fetch tweets using Tweepy
def fetch_tweets(username):
    try:
        tweets = api.user_timeline(screen_name=username, count=5, tweet_mode="extended")
        return [tweet.full_text for tweet in tweets]
    except tweepy.errors.TweepyException as e:  # Updated error handling
        return f"Error fetching tweets: {e}"


# Predict sentiment using VADER
def predict_sentiment(text, analyzer):
    sentiment_score = analyzer.polarity_scores(text)["compound"]
    return "Positive 😊" if sentiment_score > 0 else "Negative 😞"

# Function to create a colored card
def create_card(tweet_text, sentiment):
    color = "green" if sentiment.startswith("Positive") else "red"
    card_html = f"""
    <div style="background-color: {color}; padding: 10px; border-radius: 5px; margin: 10px 0;">
        <h5 style="color: white;">{sentiment}</h5>
        <p style="color: white;">{tweet_text}</p>
    </div>
    """
    return card_html

# Main app logic
def main():
    st.title("Twitter Sentiment Analysis 🚀")

    # Load sentiment analyzer
    analyzer = load_nltk_resources()

    # User input: either text input or Twitter username
    option = st.selectbox("Choose an option", ["Input text", "Get tweets from user"])

    if option == "Input text":
        text_input = st.text_area("Enter text to analyze sentiment")
        if st.button("Analyze"):
            sentiment = predict_sentiment(text_input, analyzer)
            st.write(f"**Sentiment:** {sentiment}")

    elif option == "Get tweets from user":
        username = st.text_input("Enter Twitter username")
        if st.button("Fetch Tweets"):
            tweets = fetch_tweets(username)

            if isinstance(tweets, str):  # Error handling
                st.write(f"⚠️ {tweets}")
            else:
                for tweet_text in tweets:
                    sentiment = predict_sentiment(tweet_text, analyzer)
                    card_html = create_card(tweet_text, sentiment)
                    st.markdown(card_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()