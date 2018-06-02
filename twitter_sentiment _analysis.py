import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient(object):

    def __init__(self):
	       consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

        try:
        	   self.auth=OAuthHandler(consumer_key,consumer_secret)
        	   self.auth.set_access_token(access_token,access_token_secret)
        	   self.api = tweepy.API(self.auth)
        except:
           	print("Authentication  Error!!!!!!!!!!!!!")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):

    	a= TextBlob(self.clean_tweet(tweet))

    	if a.sentiment.polarity > 0:
    		return 'pos'
    	elif a.sentiment.polarity < 0:
    		return 'neg'
    	else:
    		return 'neutral'


    def get_tweet(self, query, count=100):

    	tweets=[]
    	try:
    		fetch=self.api.search(q=query, count=count)

    		for tweet in fetch:
    			parsed_tweet={}
    			parsed_tweet['text']=tweet.text
    			parsed_tweet['sentiment']=self.get_tweet_sentiment(tweet.text)
    			if(tweet.retweet_count) > 0:
    				if parsed_tweet not in tweets:
    					tweets.append(parsed_tweet)
    			else:
    					tweets.append(parsed_tweet)
    		return tweets

    	except tweepy.TweepError as e:
    		print("Error Occured!!!!!!!!")

def main():
    	api=TwitterClient()
    	tweets=api.get_tweet(query="modi", count=1000)
	p=[]
	ng=[]
	ne=[]
	for tweet in tweets:
		if tweet['sentiment']=='pos':
			p.append(tweet)
			n=len(p)
	print('\nTotal number of positive tweets:')
	print(n)
	print('\n-------------------')
	for tweet in tweets:
		if tweet['sentiment']=='neg':
			ng.append(tweet)
			n=len(ng)
	print('\nTotal number of negative tweets:')
	print(n)
	print('\n-------------------')
	for tweet in tweets:
		if tweet['sentiment']=='neutral':
			ne.append(tweet)
			n=len(ne)
	print('\nTotal number of neutral tweets:')
	
	#for tweet in p:
	#	print(tweet['text'])
		
    	#ptweets=[tweet for tweet in tweets if tweet['sentiment']=='pos']
    	#print(ptweets)
    	ntweets=[tweet for tweet in tweets if tweet['sentiment']=='neg']
    	#print(ntweets)
    	netweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    	#print(netweets)

if __name__=="__main__":
    main()





