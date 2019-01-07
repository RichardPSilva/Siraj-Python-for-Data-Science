# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:28:03 2019

@author: 749445
"""

import tweepy
from textblob import TextBlob

consumer_key = '5lyARxJkILH6zFlQj2FlzapTM'
consumer_secret = 'uUe6IbwoGneoZV5BHObhKhEnM6QRpdzLWOaDmHorbAHrCltLZg'

access_token = '1080503530371383296-3r8kYuHtnu57dLxSzWnCDc9uVMXBVz'
access_token_secret = 'WZrctFNNkbYGoaqyGrCDYPH8GtVtSX7vvhv6oEb1ODTLE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    