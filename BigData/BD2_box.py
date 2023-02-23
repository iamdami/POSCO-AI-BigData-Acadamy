import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.rc("font", family = "NanumGothic")
matplotlib.rc("axes", unicode_minus = False)

dfF = pd.read_csv("./BD_basics/FITNESS.csv", encoding="euc=kr")
# print(dfF.head())

# dfCnt = dfF["GENDER"].value_counts()
# print(dfCnt.plot.bar())
# print(sns.countplot(x = "AGEGROUP", hue = "GENDER", data = dfF))

# print(dfF.boxplot(column="OXY", by = ["GENDER", "AGEGROUP"]))

# print(dfF.hist(figsize=(10, 7)))

# print(dfF.hist(column="OXY", by = "GENDER", range=(35, 65)))

# print(plt.hist(dfF[dfF["GENDER"]=="남성"]["OXY"], label="남성", alpha = 1))
# print(plt.hist(dfF[dfF["GENDER"]=="여성"]["OXY"], label="여성", alpha = 0.5))

# dfFCnt = dfF["GENDER"].value_counts()
# print(dfFCnt.plot.pie(y = "OXY", autopct="%.1f%%"))

# dfF = dfF.groupby(["GENDER", "AGEGROUP"]).size()
# print(dfFCnt.plot.pie(y = "OXY", autopct="%.1f%%"))

# sns.pairplot(dfF)
# sns.pairplot(dfF, y_vars=["OXY"], x_vars=["RUNPULSE", "MAXPULSE", "RUNTIME"])

# print(sns.kdeplot(dfF["RUNTIME"], dfF["OXY"], shade=False))

# print(pd.plotting.parallel_coordinates(dfF, "GENDER", cols=["OXY", "WEIGHT", "RSTPULSE"], colormap="Accent"))