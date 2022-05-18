import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("iris.csv")

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

scaler = StandardScaler()
scaler.fit(train_inputs)

# Scaling data
train_inputs = scaler.transform(train_inputs)
test_inputs = scaler.transform(test_inputs)

# creating a classifier from the model:
mlp = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=1000)

# let's fit the training data to our model
mlp.fit(train_inputs, train_classes)

# predictions_train = mlp.predict(train_inputs)
# print(accuracy_score(predictions_train, train_classes))
 predictions_test = mlp.predict(test_inputs)
print(accuracy_score(predictions_test, test_classes))

# print(confusion_matrix(predictions_train, train_classes))
print(confusion_matrix(predictions_test, test_classes))

print(classification_report(predictions_test, test_classes))

