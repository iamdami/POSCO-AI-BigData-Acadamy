import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(1234)
df = pd.DataFrame(randn(10,2), columns=['A', 'B'])

# slice
# print(df['A']) # 열(sr반환)
# print(df[('A')]) # 열(DF반환)
# print(df[0:5]) # 행

# loc
# print(df.loc[0:7, ['A']])

print(df[df.A > df.B])