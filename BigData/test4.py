import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(1234)
df = pd.DataFrame(randn(10,4))
print(df)
print()
