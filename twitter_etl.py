import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Twitter authentification
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

# Creating an API object
api = tweepy.API(auth)
api.user_timeline(user_id='@elonmusk',
                  count=200)