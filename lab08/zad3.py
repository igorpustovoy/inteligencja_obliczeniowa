import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("iris.csv")

# c) normalising data
df_norm = df[['sepallength', 'sepalwidth', 'petallength', 'petalwidth']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
# df_norm.sample(n=5)

# b)
target = df[['class']].replace(['setosa', 'versicolor', 'virginica'], [0, 1, 2])
# setosa - 0, versicolor - 1, virginica - 2
# target.sample(n=5)

df = pd.concat([df_norm, target], axis=1)

#    sepallength  sepalwidth  petallength  petalwidth   class
# 0          5.1         3.5          1.4         0.2  setosa
# 1          4.9         3.0          1.4         0.2  setosa
# 2          4.7         3.2          1.3         0.2  setosa
# 3          4.6         3.1          1.5         0.2  setosa
# 4          5.0         3.6          1.4         0.2  setosa

(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=13)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

# scaler = StandardScaler()
# scaler.fit(train_inputs)
#
# # Scaling data
# train_inputs = scaler.transform(train_inputs)
# test_inputs = scaler.transform(test_inputs)

# creating a classifier from the model:
# d) 0.9555555555555556
# mlp = MLPClassifier(hidden_layer_sizes=(2,), max_iter=5000)
# g) 0.9777777777777777
# mlp = MLPClassifier(hidden_layer_sizes=(3,), max_iter=5000)
# h) 0.9777777777777777
mlp = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=5000)

# let's fit the training data to our model
mlp.fit(train_inputs, train_classes)

# predictions_train = mlp.predict(train_inputs)
# print(accuracy_score(predictions_train, train_classes))
predictions_test = mlp.predict(test_inputs)
print(mlp.predict(test_inputs))
# f)
print(accuracy_score(predictions_test, test_classes))

# print(confusion_matrix(predictions_train, train_classes))
print(confusion_matrix(predictions_test, test_classes))

print(classification_report(predictions_test, test_classes))

