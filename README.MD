# Recipe Fetcher
This web app is a simple app that retrieves a random recipe. It's currently configured to only show various desserts, but it could be easily configured to display a selection of different dishes. Along with retrieving a recipe, it also fetches a random tweet of twitter that includes the dish's name in the tweet. Both of these are displayed on the page.
## Technologies Used
`Tweepy` - A twitter wrapper that works with Python, used to retrieve the random tweet.
`Spoonacular API` - Used to fetch the random recipe, as long with the ingredients and an image.
`Flask` - The microframework off which the site is built off of.
`HTML/CSS` - Used to lay out and beautify the site.
`Heroku` - Used to deploy the app.

## How to run your own instance
1. Sign up for a Twitter Developer account and generate your own set of API Keys/Access Tokens.
2. Sign up for Spoonacular as well, generate an API Key there as well.
3. Clone the repository and create a file named `auth.env`
4. Copy the following template to the `auth.env` file, fill in the API Keys and Access Tokens that you generated. (Replace the TODO's)
```
export TWITTER_CONSUMER_KEY=TODO
export TWITTER_CONSUMER_SECRET=TODO
export TWITTER_ACCESS_TOKEN=TODO
export TWITTER_ACCESS_TOKEN_SECRET=TODO
export SPOONACULAR_KEY=TODO
```
5. Type in the command `source auth.env` to load in the environment variables that you just created.
6. Run the app by using the command `python main.py`

## Issues
### CSS Styling
**Problem:** When attempting to style the css, it wouldn't refresh on the actual website. The HTML would stop reflecting the CSS. I tried troubleshooting this by replacing the file and deleting the file entirely, but nothing seemed to work.
**Solution:** After some more troubleshooting and a consultation with the TA, we found out that it was chrome caching the old version of the CSS. No matter what you do, or if you delete the whole css file, chrome has saved the previous version of the CSS file and keeps it loaded. This can be fixed by hard refreshing (`Shift+Click` the Refresh button) the page.