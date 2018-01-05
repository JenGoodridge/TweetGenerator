
import os
import sys
from twitter import *
import twitter.oauth_dance
import config
class Fetch():
	def __init__(self):
		self.tweetsOfUser = ''
		self.setUp()
				
	def cleanUp(self, text):
			text = list(text.split(' '))
			newText = ''
			for x in text:
				if 'http' in x:
					pass
				else: 
					x = x.strip('.%&:;,\n_?!()…\''"")
					x = x.lower()
					newText += ' ' + x
			return newText

	def setUp(self):
		CONSUMER_KEY    = config.CONSUMER_KEY
		CONSUMER_SECRET = config.CONSUMER_SECRET

		CREDENTIAL_STORAGE = os.path.expanduser('~/.jtwitter')
		if not os.path.exists(CREDENTIAL_STORAGE):
			oauth_dance("JGoodridge's Tweet Generator", CONSUMER_KEY, CONSUMER_SECRET, CREDENTIAL_STORAGE)
			
		OAUTH_TOKEN, OAUTH_SECRET = read_token_file(CREDENTIAL_STORAGE)
		twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
		timeline = twitter.statuses.user_timeline(screen_name="realDonaldTrump", tweet_mode="extended")


		for (i, t) in enumerate(timeline):
			try:
				tweet = t['retweeted_status']
			except KeyError:
				tweet = t
			self.tweetsOfUser += ' ' + (self.cleanUp(tweet['full_text']))
	def returnTweets(self):
		return self.tweetsOfUser
		
		
