#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:22:32 2020

@author: adrian
"""

import tweepy
import time
import pandas as pd

# api key
api_key = "QrFdrVejrlikh44hJJebgOstE"
api_secret_key = "yTJQnI1eUNZ7OCmALlCUaHSRDmrvkNEcq7RmGOkfhSgfQuTTkK"

# token access
access_token = "867182616-CNGvpvl2D3TCbdt18wSEFHSf8aOtz9PqIn9lVKeu"
access_token_secret = "ktt1kej9Y0ijMCaaxcKzhsZVJcjLWshSg4zdy9q8fagON"

# athorize the API key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the API
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_tweets(query):
    """ This function will take the parameter 'query' and return 50 tweets 
        related to that particular query """

    # list to store tweets
    tweets = []
    
    # nº of tweets
    count = 50
    
    try:
        # Pulling individual tweets from query
        for tweet in tweepy.Cursor(api.search,
                           q=query,
                           count=count,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
            print(tweet.text)
            # Adding to the list
            tweets.append({'created_at': tweet.created_at, 
                           'id': tweet.id,
                           'text': tweet.text})
            return pd.DataFrame.from_dict(tweets)
        
    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
        
        
        