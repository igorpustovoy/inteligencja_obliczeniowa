import json
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist
from wordcloud import WordCloud

nltk.download([
    "names",
    "stopwords",
    "state_union",
    "averaged_perceptron_tagger",
    "vader_lexicon",
    "punkt",
    "wordnet",
    "omw-1.4"
])

# Importing tweets
raw_tweets = []
f = open('tweets_crash.json')
file = json.load(f)
for tweet in file:
    raw_tweets.append(tweet)
f.close()

# Creating bag of words
all_words = ""
for tweet in raw_tweets:
    all_words = f"{all_words} {tweet}"

tokens = nltk.word_tokenize(all_words)
# Changing all upper case letters to lower case ones
tokens = [w.lower() for w in tokens]

# Filtering out hashtags, links and unnecessary words
tokens = [w for w in tokens if not w.startswith("#") and not w.startswith("http") and not w.startswith("/")
          and not w.startswith("https") and not w.startswith("@") and not w.startswith("RT")
          and not w.startswith("luna") and not w.startswith("lu") and not w.startswith("crypto")
          and not w.startswith("terra") and not w.startswith("bscs") and not w.isdigit()
          and w.encode('utf-8').isalnum()]


stop_words = set(stopwords.words("english"))
signs = {'``', "''", ".", ",", "-", "$", "?", "!", "@", "#", ":", ";", "&", "*", "^", "~", "`", "|", "\\", "/",
         "\"", "'", "=", "(", ")", "[", "]", "{", "}", ">", "<", "%", "`", "'", "'s", "n't", "...", '’', '“', '”', '..'}
unnecessary_words = {'cryptocurrency', 'terra', 'bitcoin', 'ethereum', 'luna', 'crypto', 'btc', 'eth', 'ust', 'the',
                     'xrp', 'bnb', 'sol', 'ada', 'usdt', 'solana'}
stop_words = stop_words.union(signs)
stop_words = stop_words.union(unnecessary_words)

filtered_tokens = []
for word in tokens:
    if word not in stop_words:
        filtered_tokens.append(word)

# print(filtered_tokens)

# Lematizing words
lem = WordNetLemmatizer()

lematized_tokens = []
for word in filtered_tokens:
    lematized_tokens.append(lem.lemmatize(word, "v"))

print(lematized_tokens)

fdist = FreqDist(lematized_tokens)
fdist.plot(20, cumulative=False)
plt.show()

# Create one big string from lematized tokens
all_words = ""
for token in lematized_tokens:
    all_words = f"{all_words} {token}"

wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", scale=3).generate(all_words)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("cloud.png")
