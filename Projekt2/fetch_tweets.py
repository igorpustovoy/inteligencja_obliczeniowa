import json
import time

import snscrape.modules.twitter as twitterScraper

# first_date = '2021-12-18'
# second_date = '2021-12-27'
first_date = '2022-05-10'
second_date = '2022-05-12'
scraper = twitterScraper.TwitterHashtagScraper(
    'luna exclude:retweets lang:en since:' + first_date + ' until:' + second_date)


tweet_amount = 10000
tweets = []
start = time.time()
for i, tweet in enumerate(scraper.get_items()):
    print(f"{i}/{tweet_amount} --- {tweet.date}")
    print(tweet.content)
    if i < tweet_amount:
        tweets.append(tweet.content)
    else:
        break

f = open("tweets_all_time_high.json", "w")
j = json.dumps(tweets)
f.write(j)
f.close()

end = time.time()
print("Program ran for: ", end - start)
