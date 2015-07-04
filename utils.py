# coding: utf-8

from functools import wraps
from flask import redirect, url_for
from flask import session, request

def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if not 'user' in session:
            return redirect(url_for('login'))
        else:
            return view(*args, **kwargs)
    return wrapper

