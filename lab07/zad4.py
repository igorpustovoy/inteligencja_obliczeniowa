import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix

df = pd.read_csv("diabetes.csv")
# print(df.describe())

# a)
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=274988)
# sns.pairplot(df, hue='class')
# plt.show()
columns = df.shape[1]
train_inputs = train_set[:, 0:columns - 1]
train_classes = train_set[:, columns - 1]
test_inputs = test_set[:, 0:columns - 1]
test_classes = test_set[:, columns - 1]
#
# b)
dtc = DecisionTreeClassifier()
# c)
dtc.fit(train_inputs, train_classes)
# d)
plot_tree(dtc)
# e)
print(dtc.score(test_inputs, test_classes))
# 0.696969696969697
# f)
pred = dtc.predict(test_inputs)
# print(pred)
# print(test_classes)
print(confusion_matrix(test_classes, pred, labels=["tested_positive", "tested_negative"]))
# [[ 49  26]
#  [ 49 107]]


plt.show()