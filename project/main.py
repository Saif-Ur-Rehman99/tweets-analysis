import os
import tweepy
import time
from dotenv import load_dotenv


load_dotenv()

# Set your Twitter API credentials]
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# print(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN)

client = tweepy.Client(
    bearer_token=BEARER_TOKEN, 
    consumer_key=API_KEY, 
    consumer_secret=API_SECRET_KEY, 
    access_token=ACCESS_TOKEN, 
    access_token_secret=ACCESS_TOKEN_SECRET
    )

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create an API object
api = tweepy.API(auth)

print(api)
search_terms = ['bitcoin', 'etherium', 'luna']

# Specify the username of the account you want to follow
target_username = 'username_to_follow'

# Stream listener to handle incoming tweets
class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print('connected')

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)

            time.sleep(0.2)

# Defining streaming rule
rule = tweepy.StreamRule("(#etherium OR #bitcoin) (-is:retweet -is:reply)")

stream = MyStream(bearer_token=BEARER_TOKEN)


# for term in search_terms:
#     stream.add_rules(tweepy.StreamRule(term))

stream.add_rules(rule, dry_run=True)

# Filter tweets based on the specified username
# my_stream.filter(track=[target_username])
stream.filter()
# stream.filter(tweet_fields=["referenced_tweets"])


# # Create a stream listener
# my_listener = MyStreamListener()
# my_stream = tweepy.Stream(auth=api.auth, listener=my_listener)


# Stop the stream after a certain time or when needed
# stream.disconnect()
