#!/usr/bin/env python
# coding: utf-8

import os
from functools import wraps
from flask import Flask, render_template, redirect, url_for, abort
from flask import request, session

from utils import login_required
from twitter_stuff import twitter

app = Flask(__name__)

@app.route('/')
@login_required
def index():
    at, ats = session['user']['twitter_credentials']
    oauth_sess = twitter.get_session(token=(at, ats))
    resp = oauth_sess.get('account/verify_credentials.json')
    screen_name = resp.json()['screen_name']
    return render_template('home.html',
            user=dict(
                screen_name=screen_name,
                at=at,
                ats=ats))

@app.route('/login/')
def login():
    rt, rts = twitter.get_request_token(
            data={'oauth_callback': url_for(
                    'oauth_callback',
                    _external=True)})
    session['twitter_temporary_credentials'] = rt, rts
    return redirect(twitter.get_authorize_url(rt))

@app.route('/oauth_callback/')
def oauth_callback():
    rt = request.args.get('oauth_token')
    veri = request.args.get('oauth_verifier')
    if rt is None or veri is None:
        abort(404)
    rt_, rts = session['twitter_temporary_credentials']
    assert rt == rt_
    at, ats = twitter.get_access_token(rt, rts, method="POST",
            data={'oauth_verifier': veri})
    del session['twitter_temporary_credentials']
    session['user'] = dict(twitter_credentials=(at, ats))
    # Hacky: Should redirect back to original url!
    return redirect(url_for('index'))

@app.route('/logout/')
def logout():
    if 'user' in session:
        del session['user']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    print("App secret key: {}".format(app.secret_key))
    app.run(debug=True)
