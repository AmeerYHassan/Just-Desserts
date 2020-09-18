import tweepy
import sys
import os
import flask
import random
from datetime import datetime, date, time, timedelta

consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

recipeNames = {"Cake", "Cookie", "Cookies", "Ice Cream", "Pastry", "Sweet", "Dessert", "Cupcake", "Muffin", "Candy", "Caramel", "Cheesecake", "Chocolate", "Cobbler"}

app = flask.Flask(__name__)
@app.route('/')
def index():
    currDish = random.choice(tuple(recipeNames))
    tweets = tweepy.Cursor(twitter_api.search,
                       q=currDish,
                       lang="en").items(5)
                       
    return flask.render_template(
        "index.html",
        currentDish = currDish,
        relevantTweet = random.choice(list(tweets)).text
    )

app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = True
)
