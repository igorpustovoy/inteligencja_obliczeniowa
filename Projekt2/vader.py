import json

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Importing tweets
raw_tweets = []
f = open('tweets_crash.json')
file = json.load(f)
for tweet in file:
    raw_tweets.append(tweet)
f.close()

compound_sum = 0
neg_sum = 0
pos_sum = 0
for tweet in raw_tweets:
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(tweet)
    for k in sorted(ss):
        if k == 'compound':
            compound_sum += ss[k]
        elif k == 'neg':
            neg_sum += ss[k]
        elif k == 'pos':
            pos_sum += ss[k]

print(f"Compound average: {compound_sum / len(raw_tweets)}")
print(f"Pos average: {pos_sum / len(raw_tweets)}")
print(f"Neg average: {neg_sum / len(raw_tweets)}")

# All time high:
# Compound average: 0.3000518146607352
# Pos average: 0.1275326352029839
# Neg average: 0.020224788409123513

# Crash:
# Compound average: 0.05136983000000041
# Pos average: 0.0915941999999999
# Neg average: 0.07146689999999996
