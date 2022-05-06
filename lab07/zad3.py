import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix

#    sepallength  sepalwidth  petallength  petalwidth   class
# 0          5.1         3.5          1.4         0.2  setosa
# 1          4.9         3.0          1.4         0.2  setosa
# 2          4.7         3.2          1.3         0.2  setosa
# 3          4.6         3.1          1.5         0.2  setosa
# 4          5.0         3.6          1.4         0.2  setosa

df = pd.read_csv("iris.csv")
# print(df.describe())

# a)
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=274988)

# sns.pairplot(df, hue='class')
# plt.show()

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

# b)
dtc = DecisionTreeClassifier()
# c)
dtc.fit(train_inputs, train_classes)
# d)
plot_tree(dtc)
# e)
print(dtc.score(test_inputs, test_classes))
# 0.9111111111111111 drzewo w zadaniu 2 jest lepsze :O
# f)
pred = dtc.predict(test_inputs)
# print(pred)
# print(test_classes)
print(confusion_matrix(test_classes, pred, labels=["setosa", "virginica", "versicolor"]))
# [[12  0  0]
#  [ 0 12  1]
#  [ 0  3 17]]


plt.show()
