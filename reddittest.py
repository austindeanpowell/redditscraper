import praw
import os

# Using environment variables (Recommended for security)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Test if the connection works
try:
    submission = reddit.submission(id="1dik5ya")  # Replace with a real post ID
    print("✅ Reddit API connection successful!")
    print(f"Title: {submission.title}")
    print(f"Upvotes: {submission.score}")
    
except Exception as e:
    print("❌ Reddit API connection failed!")
    print(e)

 