import seaborn as sns
import pandas as pd

titanic = sns.load_dataset("titanic")
print(titanic.isnull().sum())
titanic['age'] = round(titanic['age'].fillna(titanic['age'].median()))
print(titanic)
print(titanic['embarked'].value_counts(()))
titanic['embarked'] = titanic["embarked"].fillna('S')
titanic.to_csv("titanic.csv", index = False)