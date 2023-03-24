na = 23456789
score = [0] * 1000001
score[0] = 1
score[1] = 0
score[2] = 1
score[3] = 1

for i in range(4, 1000001):
    score[i] = (score[i-2] + score[i-3]) % na
for _ in range(int(input())):
    n = int(input())
    print(score[n])