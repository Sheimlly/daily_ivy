import tweepy
import os
from dotenv import load_dotenv

load_dotenv()
env = os.getenv

# Authenticate to Twitter
client = tweepy.Client(
        bearer_token=os.getenv('bearer_token'),
        consumer_key=os.getenv('consumer_key'),
        consumer_secret=os.getenv('consumer_secret'),
        access_token=os.getenv('access_token'),
        access_token_secret=os.getenv('access_token_secret')
        )

client.create_tweet(text='bot test')
