import tweepy
import sys
import os
import flask
import random
import requests

consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
spoonacular_key = os.environ.get("SPOONACULAR_KEY")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

recipeNames = set(open('dishes.txt').read().split())

app = flask.Flask(__name__)

@app.route('/')
def index():
    currDish = random.choice(tuple(recipeNames))
    urlStr = "https://api.spoonacular.com/recipes/complexSearch?query="+currDish+"&apiKey="+spoonacular_key
    content = requests.get(urlStr)
    content_json = content.json()
    random_recipe = random.choice(tuple(content_json['results']))['id']
    
    infoUrl = "https://api.spoonacular.com/recipes/"+str(random_recipe)+"/information?apiKey="+spoonacular_key
    print(infoUrl)
    infoContent = requests.get(infoUrl).json()

    tweets = tweepy.Cursor(twitter_api.search,
                       q=currDish,
                       tweet_mode='extended',
                       lang="en").items(5)
    
    currTweet = random.choice(list(tweets))
    return flask.render_template(
        "index.html",
        currentDish = currDish,
        relevantTweet = currTweet.full_text,
        tweetDate = str(currTweet.created_at),
        tweetAuthor = str(currTweet.author.name),
        tweetUrl = str(currTweet.id),
        recipeTitle = infoContent['title'],
        recipeURL = infoContent['sourceUrl'],
        recipeImage = infoContent['image'],
        recipeServings = infoContent['servings'],
        recipePrepTime = infoContent['']
    )

app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = True
)
