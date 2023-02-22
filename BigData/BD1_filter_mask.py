import pandas as pd

df = pd.DataFrame({"ABC": ['A', 'B', 'C', 'A'],
'abc': ['a', 'b', 'c', 'c'], 
'gr1': ['g1', 'g2', 'g3', 'g4'],
'v1': [11, 12, 13, 14],
'v1_mod': [0.123, 0.243, 0.235, 0.456]})

print(df)