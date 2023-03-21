def fivo_recursive(n):        
    if n <= 1:
        return 1
    return fivo_recursive(n - 1) + fivo_recursive(n - 2)

t = int(input())
for i in range(t):
    print(fivo_recursive(i))