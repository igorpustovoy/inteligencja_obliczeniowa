import snscrape.modules.twitter as twitterScraper

# 'exclude:retweets lang:en since:'+first_date+' until:'+second_date
scraper = twitterScraper.TwitterHashtagScraper('amberheard exclude:retweets lang:en')

limit = 100
tweets = []
for i, tweet in enumerate(scraper.get_items()):
	if i < limit:
		tweets.append(tweet.content)
	if i >= limit:
		break


print(tweets)


