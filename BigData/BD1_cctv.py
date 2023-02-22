import pandas as pd
import numpy as np

cctv = pd.read_excel("BD_basics/서울시CCTV.xlsx", skiprows = 2, names=['기관명', '소계', '2011년 이전', '2012년', '2013년', '2014년', '2015년', '2016년', '2017년', '2018년', '2019년', '2020년', '2021년'])
print(cctv)