import pandas as pd

tb = {"일자": ['2019-01-01', '2019-01-04','2019-01-07','2019-01-10','2019-01-13'], 
"가격": [1000, 1500, 2000, 2500, 3000], 
"구매여부": ["F", "T", "T","T","T"],
"제품": ["gum", "snack", "beverage", "dongas", "icecream"]}
df = pd.DataFrame(tb)
print(df)