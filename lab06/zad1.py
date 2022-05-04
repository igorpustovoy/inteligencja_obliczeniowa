# Importing libraries
import pandas as pd
import numpy as np
from difflib import SequenceMatcher

# Read csv file into a pandas dataframe

# Making a list of missing value types
missing_values = ["n/a", "na", "--", "-"]
df = pd.read_csv("iris_with_errors.csv", na_values=missing_values)

# Take a look at the first few rows
# print(df.head())

# sepal.length sepal.width  petal.length  petal.width variety
# 0          5.1         3.5           1.4          0.2  Setosa
# 1          4.9           3           1.4          0.2  Setosa
# 2          4.7         3.2           1.3          0.2  Setosa
# 3          4.6         3.1           1.5          0.2  Setosa
# 4            5         3.6           1.4          0.2  Setosa

# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(df['sepal.length'])
#     print(df['sepal.length'].isnull())

# a)
print("Lączna liczba brakujących lub nieuzupełnionych danych:\n", df.isnull().sum().sum())
# 5
print("Statystki błedów:\n", df.isnull().sum())
# sepal.length    2
# sepal.width     1
# petal.length    1
# petal.width     1
# variety         0

# Uzupełniamy brakujące dane:
# Replace using median
median = df['sepal.length'].median()
df['sepal.length'].fillna(median, inplace=True)

median = df['sepal.width'].median()
df['sepal.width'].fillna(median, inplace=True)

median = df['petal.length'].median()
df['petal.length'].fillna(median, inplace=True)

median = df['petal.width'].median()
df['petal.width'].fillna(median, inplace=True)

# b)
numeric_columns = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']

for column in numeric_columns:
    cnt = 0
    for row in df[column]:
        try:
            int(row)
            median = df[column].median()
            if row < 0 or row > 15:
                df.loc[cnt, column] = median
        except ValueError:
            pass
        cnt += 1

# c)

flower_names = ["Setosa", "Versicolor", "Virginica"]

cnt = 0
for row in df['variety']:
    if flower_names.count(row) == 0:
        similiarity = []
        for flower in flower_names:
            similiarity.append(SequenceMatcher(None, row, flower).ratio())
            maxi = max(similiarity)
            index = similiarity.index(maxi)
            df.loc[cnt, 'variety'] = flower_names[index]
    cnt += 1

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)

df.to_csv('corrected_iris_with_errors.csv')
