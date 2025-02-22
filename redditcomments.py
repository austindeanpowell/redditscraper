import praw
import os
import time
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER for sentiment analysis
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Using environment variables (Recommended for security)
# Do NOT fill in actual client/secret values if running locally and scraper is using localhost8080
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# inspect the page search for postid "tw_12345" remove the tw
post_id = "1dik5ya"
submission = reddit.submission(id="1dik5ya")
submission = reddit.submission(id=post_id)
submission.comments.replace_more(limit=None)  # Load all nested comments

# This is to extract comment data on reddit thread
comments_data = []
for comment in submission.comments.list():
    sentiment_score = sia.polarity_scores(comment.body)["compound"]
    comments_data.append([comment.id, comment.body, sentiment_score])
    time.sleep(1)  

# Convert to DataFrame to prepare for CSV
df = pd.DataFrame(comments_data, columns=["Comment_ID", "Text", "Sentiment_Score"])

# Save to CSV with timestamp
import datetime
filename = f"reddit_sentiment_analysis_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(filename, index=False)

print(f"CSV file saved: {filename}")