A Twitter OAuth Consumer application, in Flask
==============================================

Environment variables needed:

- `TWITTER_CONSUMER_KEY`
- `TWITTER_CONSUMER_SECRET`
- `FLASK_SECRET_KEY`: Just use a long random string

Run:

    $ virtualenv .venv
    $ source .venv/bin/activate
    (.venv)$ pip install -r requirements.txt
    (.venv)$ python flitter.py
