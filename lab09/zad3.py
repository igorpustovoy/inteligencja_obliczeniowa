from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize


negative_opinion = "location everything else! the room has no window, smelly, tv didn’t work, no el-socket by the " \
                   "bed, fridge didn’t work, the water tap badly fixed, they didn’t answer the phone even they accept " \
                   "my arrival time and the door was locked, the owner took the only phone on booking.com of his " \
                   "hotel with him and left on holiday!!!!"

positive_opinion = "This was my second time at this hotel and it is rapidly becoming my favorite place in Cairo. They " \
                   "actually listened to my special request and gave me exactly what I asked for, which is so rare. " \
                   "It was super quiet and the temperature was good (not too cold like some places during winter). I " \
                   "slept really well and enjoyed the hot shower. The breakfast includes a boiled egg and some cheese " \
                   "in addition to the usual bread and coffee/tea. It's also great that they provide towels, " \
                   "which many places don't. The only thing I would improve would be to fix the toilet so it doesn't " \
                   "run all the time and waste water. I noticed that in the other room I stayed in too. I pointed it " \
                   "out, but they don't seem to think it's a problem. They could save a lot of water by having a good " \
                   "plumber give this hotel a tune-up. "

opinions = [negative_opinion, positive_opinion]

for opinion in opinions:
    sid = SentimentIntensityAnalyzer()
    print(opinion)
    ss = sid.polarity_scores(opinion)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()

    # d)
    # Są zgodne z oczekiwaniami
