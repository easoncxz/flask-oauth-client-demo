#!/usr/bin/env python
# coding: utf-8

import os
from functools import wraps
from flask import Flask, render_template, redirect, url_for, abort
from flask import request, session

from utils import login_required

app = Flask(__name__)

@app.route('/')
@login_required
def index():
    username = session['user']['name']
    return render_template('home.html',
            user=dict(display_name=username))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        session['user'] = dict(name=username)
        return redirect(request.args.get('next', '/'))

@app.route('/logout/')
def logout():
    if 'user' in session:
        del session['user']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    print("App secret key: {}".format(app.secret_key))
    app.run(debug=True)
