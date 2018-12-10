#This is the file where collect 10,000 tweets that contain either of the terms "NBA", or "#NBA"(case insensitive), through the twitter API.

# -*- coding: utf-8 -*-
"""NBA10000.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B-6a4IbtxBoUXm52KVRx0A4_qCK8Jcpv
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


#This is a basic listener that just prints received tweets to stdout.

MAX_NUM_TWEETS = 10000
class StdOutListener(StreamListener):
    def __init__(self):
        self.count = 0

    def on_data(self, data):
        self.count += 1
        print data
        if self.count > MAX_NUM_TWEETS:
            return False
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['#NBA','nba'])

