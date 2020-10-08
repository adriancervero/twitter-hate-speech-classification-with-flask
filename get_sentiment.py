#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:44:26 2020

@author: adrian
"""

from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from get_tweets import get_tweets

# load pipeline object
pipeline = load("text_classification.joblib")

def requestResults(name):
    """ Get the tweets for the requested query and use the pipeline on it
        to get the labels and return the final results to send. """
        
    # get the tweets text
    tweets = get_tweets(name)
    
    # get the prediction
    tweets['prediction'] =  pipeline.predict(tweets['text'])
    
    # get the value counts of different labels predicted 
    data = str(tweets.prediction.value_counts()) + '\n\n'
    
    return data + str(tweets)

# start flask
app = Flask(__name__)

# render default page
@app.route('/')
def home():
    return render_template('index.html')

# when the post method detect, the redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))
    
# get the data for the requested query
@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + "</xmp>"


if __name__ == '__main__':
    app.run(debug=True)






















