import matplotlib.pyplot as plt
import nltk
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

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

articles = ["school_shooting.txt", "gun_control.txt", "depp_vs_heard.txt"]


def delete_stop_words_and_lematize(titles):
    lematized_articles = []
    for title in titles:
        with open(title) as f:
            article = f.read()

        tokens = nltk.word_tokenize(article)
        tokens = [w.lower() for w in tokens]

        stop_words = set(stopwords.words("english"))
        signs = {'``', "''", ".", ",", "-", "$", "?", "!", "the"}
        stop_words = stop_words.union(signs)

        filtered_tokens = []
        for word in tokens:
            if word not in stop_words:
                filtered_tokens.append(word)

        lem = WordNetLemmatizer()

        lematized_tokens = []
        for word in filtered_tokens:
            lematized_tokens.append(lem.lemmatize(word, "v"))

        lematized_articles.append(str(lematized_tokens))

    return lematized_articles


converted_articles = delete_stop_words_and_lematize(articles)

school_shooting = articles[0]
gun_control = articles[1]
depp_vs_heard = articles[2]

print(converted_articles)

cv = CountVectorizer()
cv_matrix = cv.fit_transform(converted_articles)
count_array = cv_matrix.toarray()

df = pd.DataFrame(data=count_array, columns=cv.get_feature_names_out())

# macierz tf
tf = df.div(df.sum(axis=1), axis=0)
print(tf)

# macierz tfidf
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(converted_articles)
tfidf_array = tfidf_matrix.toarray()

df_tfidf = pd.DataFrame(data=tfidf_array, columns=tfidf.get_feature_names_out())

print(df_tfidf)


# cosinus podobienstwa
cos_sim = cosine_similarity(cv_matrix)

print(cos_sim)
