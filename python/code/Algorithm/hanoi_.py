def Hanoi(n, start, mid, end) :
    if n == 0 :
        return 0
    Hanoi(n-1, start, end, mid)
    print(start, '->', end)
    Hanoi(n-1, mid, start, end)  
    
t = int(input())
for _ in range(t) :
    n = int(input())
    Hanoi(n, 'A', 'B', 'C')    