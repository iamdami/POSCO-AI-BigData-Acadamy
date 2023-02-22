import pandas as pd
import numpy as np

seoulPop = pd.read_csv("./BD_basics/서울인구통계.txt", sep = "\t", thousands=",", skiprows=2, encoding="utf=8")
# print(seoulPop.head())
pop1 = seoulPop[["자치구", "계", "계.1", "계.2","65세이상고령자"]]
seoulPop = pop1.drop([0])
print(seoulPop.head())