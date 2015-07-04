#!/usr/bin/env python
# coding: utf-8

import os
from functools import wraps
from flask import Flask, render_template, redirect, url_for, abort
from flask import request, session

from utils import login_required
from twitter_stuff import twitter, log_session_in

app = Flask(__name__)

@app.route('/')
@login_required
def index():
    resp = twitter.get('account/verify_credentials.json')
    screen_name = resp.data['screen_name']
    return render_template('home.html',
            user={'screen_name': screen_name})

@app.route('/login/')
def login():
    next = request.args.get('next', url_for('index'))
    return twitter.authorize(
            callback=url_for('oauth_callback', next=next))

@app.route('/oauth_callback/')
def oauth_callback():
    log_session_in()
    next = request.args.get('next', url_for('index'))
    return redirect(next)

@app.route('/logout/')
def logout():
    if 'user' in session:
        del session['user']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = os.getenv('FLASK_SECRET_KEY') or os.urandom(24)
    app.run(debug=True)
