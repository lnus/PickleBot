import tweepy
import time
import schedule
import markovify

# Reads from my keys.py file
# Won't upload that for obvious reasons.
 
from keys import *

# Initial setup and connecting to the API

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# Main bot class

class PickleBot(object):
    def __init__(self):
        print("### PickleBot 1.0 up and running ###")
    
    def generate_tweet(self):
        with open("rick_transcripts.txt") as f:
            text = f.read()
            f.close()
        text_model = markovify.Text(text)
        return(text_model.make_short_sentence(140))

    def post_tweet(self):
        tweet = self.generate_tweet()
        api.update_status(tweet)
        print(tweet)
        print(time.ctime())


if __name__ == '__main__':
    p = PickleBot()

    # Sends initial tweet
    p.post_tweet()

    # Sets up a schedule
    schedule.every(15).minutes.do(p.post_tweet)

    # Runs the schedule for timed posts
    while True:
        schedule.run_pending()
        time.sleep(1)
