# coding: utf-8

import os
from rauth import OAuth1Service

twitter = OAuth1Service(
    consumer_key = os.getenv('TWITTER_CONSUMER_KEY'),
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET'),
    name='twitter',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    request_token_url='https://api.twitter.com/oauth/request_token',
    base_url='https://api.twitter.com/1/')
