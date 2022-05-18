import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

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

train_inputs = scaler.transform(train_inputs)
test_inputs = scaler.transform(test_inputs)

classifier = GaussianNB()
classifier.fit(train_inputs, train_classes)

y_pred = classifier.predict(test_inputs)

conf_matrix = confusion_matrix(test_classes, y_pred)

print(conf_matrix)
print(classification_report(test_classes, y_pred))

total_results = 0
for row in conf_matrix:
    for result in row:
        total_results += result

correct_results = 0
for i in range(0, len(conf_matrix)):
    correct_results += conf_matrix[i][i]

print("Accuracy: ", correct_results / total_results)

# Accuracy:  0.9555555555555556
