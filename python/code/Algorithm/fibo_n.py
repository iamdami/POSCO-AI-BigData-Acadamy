d = [0] * 1000

def fibo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n - 1) + fibo(n - 2)
    return d[n]

for _ in range(int(input())) :
    n = int(input())
    print(fibo(n))