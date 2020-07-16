import os
import tweepy
import time
# Authenticate to Twitter
CONSUMER_KEY=os.getenv(CONSUMER_KEY)
CONSUMER_SECRET=os.getenv(CONSUMER_SECRET)
ACCESS_KEY=os.getenv(ACCESS_KEY)
ACCESS_SECRET=os.getenv(ACCESS_SECRET)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = '#SNSD'
numTweet = 500
for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        print('Tweet Liked')
        tweet.favorite()
        print("Retweet done")
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

