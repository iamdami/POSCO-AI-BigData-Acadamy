import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

dfC = pd.read_csv("./BD_basics/환율.csv", encoding="euc=kr")
dfCP = dfC.pivot(index="APPL_DATE", columns="CURRENCY", values="STD_RATE")
# print(dfCP.head())

# print(dfCP["CNY"].plot())
# print(dfCP[["JPY", "USD"]].plot())
