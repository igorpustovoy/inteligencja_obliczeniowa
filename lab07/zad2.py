import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=274988)


def classify_iris(sl, sw, pl, pw):
    if pl >= 5:
        return "virginica"
    elif pw <= 0.5:
        return "setosa"
    else:
        return "versicolor"


print(train_set[train_set[:, 4].argsort()])

good_predictions = 0
len = test_set.shape[0]
for i in range(len):
    if classify_iris(test_set[i][0], test_set[i][1], test_set[i][2], test_set[i][3]) == test_set[i][4]:
        good_predictions += 1

print(good_predictions)
print(good_predictions / len * 100, "%")
# 42
# 93.33333333333333 %
