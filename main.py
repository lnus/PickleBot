import tweepy
import time

# Gets the keys from my key file
# Won't upload that for obvious reasons.
 
from keys import *

# Initial setup and connecting to the API

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#TODO: Make some shit
