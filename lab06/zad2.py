import pandas as pd
import numpy as np
from difflib import SequenceMatcher

from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Read csv file into a pandas dataframe
df = pd.read_csv("iris.csv")

# Take a look at the first few rows
# print(df.head())

#    sepallength  sepalwidth  petallength  petalwidth   class
# 0          5.1         3.5          1.4         0.2  setosa
# 1          4.9         3.0          1.4         0.2  setosa
# 2          4.7         3.2          1.3         0.2  setosa
# 3          4.6         3.1          1.5         0.2  setosa
# 4          5.0         3.6          1.4         0.2  setosa

# b)
features = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth']
# Separating out the features
x = df.loc[:, features].values
# Separating out the target
y = df.loc[:, ['class']].values
# Standardizing the features
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents
                           , columns=['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df[['class']]], axis=1)

var = pca.explained_variance_ratio_
# Wariancja:
# [0.72770452 0.23030523 0.03683832 0.00515193]
# Widzimy że po usunięciu dwóch kolumn, wariancja wynosi:
# 0.72770452 + 0.23030523 = 0.95800975 > 80%
# A więc przyjmuje ona dopuszczalną ilość powyżej 80%

# Wzór ze slajdów oblicza iloraz wariancji kolumn które pozostały po zastosowaniu pca
# oraz ich łącznej początkowej ilości a następnie odejmuje ten iloraz od 1

print(finalDf.head())

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)
targets = ['setosa', 'versicolor', 'virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['class'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c=color
               , s=50)
ax.legend(targets)
ax.grid()
plt.show()
