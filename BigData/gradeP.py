import pandas as pd
df = pd.read_csv("../postech/BD/1BD/성적.csv", encoding="euc-kr")
tb = {"성명": ["홍길동", "이순신", "강감찬", "이성계", "정약용"],
"국어성적": [90, 95, 85, 90, 95],
"영어성적": [90, 85, 90, 95, 95],
"수학성적": [95, 90, 85, 75, 90]}
df = pd.DataFrame(tb)
print(df)
