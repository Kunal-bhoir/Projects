import tweepy
import time

auth = tweepy.OAuthHandler('jIVplt8FYw4k71BPvBzYz1r3g', 'ENlAnahKsBUZL1i9DV74VnIZTvbSAWpRIkPZPlRZGkXaqt06vW')
auth.set_access_token('1264244279699894272-c2iqLv5qy0xmF1Hg1tX7OyccICv9ke', 'PW7uc7z6I4T7iQTVeSq5r9AhKaxGusUSXSD8mUe2aNPUP')

api = tweepy.API(auth)

user =api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep()    

search_string = "python"
numberoftweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberoftweets):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break    

