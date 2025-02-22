import os
import time
import praw
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Download VADER for sentiment analysis
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Reddit API Credentials (Use Environment Variables)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),       # Make sure this is set
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),  # Make sure this is set
    user_agent=os.getenv("REDDIT_USER_AGENT") 
)
# Define the post you want to analyze
post_id = "t3_wl5ft2"  # Replace with actual thread ID
submission = reddit.submission(id=post_id)
submission.comments.replace_more(limit=None)  # Load all nested comments