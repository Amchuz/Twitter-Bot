import tweepy
import time
# Authenticate to Twitter
CONSUMER_KEY = 5tdn6cRUteqVfLDPFp0nu2um9
CONSUMER_SECRET = GKf9osiqCRRRMyZte8OICBPhG5RQ5zcswEjECJkN9BjXdrTCbM
ACCESS_KEY = 1283441859159666688-CwEpvhHoxbOR9bFIbYYtrRSTOjIhNs
ACESS_SECRET = 1w3pO2CIusLhwqy0jEjFAeX1xxsVa0itBX6U1LyWDhlRE
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACESS_SECRET)
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

