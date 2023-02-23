import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.rc("font", family = "NanumGothic")
matplotlib.rc("axes", unicode_minus = False)

dfF = pd.read_csv("./BD_basics/FITNESS.csv", encoding="euc=kr")

dfC = dfF["AGEGROUP"].value_counts()
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13,10))
plt.tight_layout(w_pad=5, h_pad=5)

axes[0,0].hist(dfF["OXY"])
axes[0,0].set_title("Histogram", fontsize = 15)
axes[0,0].set_xlabel("혈당 산소 요구량", fontsize=12)

axes[0,1].pie(dfC, labels=dfC.index.tolist(), autopct="%.1f%%")
axes[0,1].set_title("Pie Chart", fontsize=15)
axes[0,1].set_xlabel("연령대", fontsize=12)

axes[1,0].plot("RUNTIME", "RUNPULSE", data = dfF, label = "맥박(운동)")
axes[1,0].plot("RUNTIME", "OXY", data = dfF, label = "혈당 산소 요구량")
axes[1,0].set_title("Trend", fontsize=15)
axes[1,0].set_xlabel("운동 시간", fontsize=12)
axes[1,0].legend()

axes[1,1].
axes[1,1].
axes[1,1].
axes[1,1].