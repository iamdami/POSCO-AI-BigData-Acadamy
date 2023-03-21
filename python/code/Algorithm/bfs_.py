from collections import deque

t = int(input())

for _ in range(t) :
    N, M = map(int, input().split())
    lst = [[] for _ in range(N)]
    
    for i in range(M) :
        u, v = map(int, input().split())
        lst[u].append(v)
        
    for i in range(N) :
        lst[i].sort()
        
    Check = [False] * N
    Queue = deque([0])
    
    
    while Queue :
        v = Queue.popleft()
        if Check[v] == True :
            continue
        Check[v] = True
        print(v, end = ' ')
        
        for i in lst[v] :
            if Check[i] == False :
                Queue.append(i)
                
    print('')