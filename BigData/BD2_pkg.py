import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.rc("font", family = "NanumGothic")
matplotlib.rc("axes", unicode_minus = False)

dfF = pd.read_csv("./BD_basics/FITNESS.csv", encoding="euc=kr")
# print(dfF.head())

dfCnt = dfF["GENDER"].value_counts()
# print(dfCnt.plot.bar())
print(sns.countplot(x = "AGEGROUP", hue = "GENDER", data = dfF))