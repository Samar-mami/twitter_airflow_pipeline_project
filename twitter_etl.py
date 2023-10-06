import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv


def get_credentials():
    # Load environment variables
    load_dotenv()
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    return consumer_key, consumer_secret, access_token, access_token_secret


def connect_twitter_api(consumer_key, consumer_secret, access_token, access_token_secret):
    # Twitter authentication
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    return auth


def get_tweets(auth, tweets_filename):
    # Creating an API object
    api = tweepy.API(auth)
    tweets = pd.read_csv(tweets_filename, header=0)
    return tweets
