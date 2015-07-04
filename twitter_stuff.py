# coding: utf-8

import os
from flask import session
from flask_oauthlib.client import OAuth

_oauth = OAuth()
_flask_oauthlib_twitter = _oauth.remote_app('twitter',
    consumer_key = os.getenv('TWITTER_CONSUMER_KEY'),
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET'),
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    request_token_url='https://api.twitter.com/oauth/request_token',
    base_url='https://api.twitter.com/1.1/')

twitter = _flask_oauthlib_twitter

# https://flask-oauthlib.readthedocs.org/en/latest/client.html
@twitter.tokengetter
def get_twitter_token():
    return session.get('user', {}).get('twitter_credentials')

# https://flask-oauthlib.readthedocs.org/en/latest/client.html
def log_session_in():
    """ Save OAuth AT/ATS info into session. """
    resp = twitter.authorized_response()
    at, ats = resp['oauth_token'], resp['oauth_token_secret']
    session['user'] = {'twitter_credentials': (at, ats)}
