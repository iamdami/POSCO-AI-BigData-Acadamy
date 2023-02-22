import pandas as pd
df = pd.read_csv("./BD_basics/FITNESS.csv", encoding="euc-kr")
print(df.head())
df=pd.read_excel("./BD_basics/성적처리.xlsx", sheet_name="Sheet1")
print(df.head())