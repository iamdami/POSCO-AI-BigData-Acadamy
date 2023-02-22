import pandas as pd

df = pd.read_csv("./BD_basics/auto_mpg.csv")
gBy = df.groupby(["modelyear", "cylinders"]).agg(["mean", "median"])
print(gBy)