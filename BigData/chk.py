import pandas as pd

df = pd.read_csv("../postech/BD/1BD/FITNESS.csv", encoding="euc-kr")
print(df.head())
print(df.describe())
print(df.count())
print(df.groupby(["NAME", "GENDER"]).median())
print(df.groupby(["NAME", "GENDER"]).mean())