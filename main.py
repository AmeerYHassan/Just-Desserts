import tweepy
import sys
import os
import flask
import random
import requests

# function to return a list of just ingredients and strips the rest of the information
def getIngredientList (extendedIngredients):
    ingredientList = []
    for ingredient in extendedIngredients:
        ingredientList.append(ingredient['originalString'])

    return ingredientList

# key declaration
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
spoonacular_key = os.environ.get("SPOONACULAR_KEY")

# twitter api authentication and access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

# a list of all the desserts that are parsed
recipeNames = set(open('dishes.txt').read().split("\n"))

app = flask.Flask(__name__)

@app.route('/')
def index():
    # generate a random dish from the list, generate the url, get the result and the id
    currDish = random.choice(tuple(recipeNames))
    urlStr = "https://api.spoonacular.com/recipes/complexSearch?query="+currDish+"&apiKey="+spoonacular_key
    content = requests.get(urlStr)
    content_json = content.json()
    random_recipe = random.choice(tuple(content_json['results']))['id']
    
    # retrieve more detailed information about the recipe
    infoUrl = "https://api.spoonacular.com/recipes/"+str(random_recipe)+"/information?apiKey="+spoonacular_key
    print(infoUrl)
    infoContent = requests.get(infoUrl).json()
    ingredients = infoContent['extendedIngredients']
    parsedIngredients = getIngredientList(ingredients)
    
    # search twitter for the latest 5 tweets concerning a dish
    tweets = tweepy.Cursor(twitter_api.search,
                       q=f"{currDish} -filter:retweets",
                       tweet_mode='extended',
                       lang="en").items(5)
    
    # choose a random dish from the list of tweets
    currTweet = random.choice(list(tweets))
    
    # send information to the html to be rendered
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
        prepTime = infoContent['readyInMinutes'],
        recipeSummary = infoContent['summary'],
        recipeIngredients = parsedIngredients,
        ingredientsLen = len(parsedIngredients)
    )

app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = True
)