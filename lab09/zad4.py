import snscrape.modules.twitter as twitterScraper

scraper = twitterScraper.TwitterHashtagScraper('amberheard')

limit = 100
tweets = []
for i, tweet in enumerate(scraper.get_items()):
	if i < limit and tweet.lang == 'en':
		tweets.append(tweet.content)
	if i >= limit:
		break


print(tweets)


