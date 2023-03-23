def fibo_recursive(n):        
    if n <= 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

t = int(input())
for i in range(t):
    print(fibo_recursive(i))
