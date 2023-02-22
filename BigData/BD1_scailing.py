import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

df_raw = pd.read_csv("./BD_basics/FITNESS_정제.csv", encoding="euc-kr")
print(df_raw.head())