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

with open('school_shooting.txt') as f:
    article = f.read()

# print(article)

# b)
tokens = nltk.word_tokenize(article)
# Changing all upper case letters to lower case ones
tokens = [w.lower() for w in tokens]
# print(tokens)
# print(len(tokens))
# Words: 900

# c)
stop_words = set(stopwords.words("english"))
# print(stop_words)

filtered_tokens = []
for word in tokens:
    if word not in stop_words:
        filtered_tokens.append(word)

# print(len(filtered_tokens))
# Words: 587
# d)
signs = {'``', "''", ".", ",", "-", "$", "?", "!", "the"}
stop_words = stop_words.union(signs)

filtered_tokens = []
for word in tokens:
    if word not in stop_words:
        filtered_tokens.append(word)

# print(filtered_tokens)
# print(len(filtered_tokens))
# Words: 462

# e)
lem = WordNetLemmatizer()

lematized_tokens = []
for word in filtered_tokens:
    lematized_tokens.append(lem.lemmatize(word, "v"))

print(lematized_tokens)
# print(len(lematized_tokens))
# Words: 462

# f)
fdist = FreqDist(lematized_tokens)
fdist.plot(10, cumulative=False)
plt.show()

# g)
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", scale=3).generate(article)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("cloud.png")
