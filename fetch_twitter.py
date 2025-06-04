
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_twitter(query='أخبار', count=10):
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)
    tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at','author_id'], max_results=count)

    results = []
    for tweet in tweets.data if tweets.data else []:
        results.append({
            "text": tweet.text,
            "created_at": tweet.created_at,
            "author_id": tweet.author_id
        })
    return results
