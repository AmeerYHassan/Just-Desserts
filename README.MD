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
4. Using the following template, fill in the API Keys and Access Tokens
5. 
## Issues