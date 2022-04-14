#connect w twitter 
#list of profiles we want to scrap data from
#sorting out posts we're interested in
#scope of keywords 
#importing scope from coinmarketcap
#counting specific keywords 

import tweepy
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
x=config['Twitter']['consumer_key']
print(x)

#auth = tweepy.OAuth1UserHandler(
#consumer_key, consumer_secret, access_token, access_token_secret
#)

#api = tweepy.API(auth)

#public_tweets = api.home_timeline()
# for tweet in public_tweets:
# print(tweet.text)