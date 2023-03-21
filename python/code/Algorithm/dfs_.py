import os, sys
sys.setrecursionlimit(1000000)

def DFS(v, List, Check) :
    print(v, end = ' ')
    Check[v] = True
    for i in List[v] :
        if Check[i] == False :
            DFS(i, List, Check)
            
t = int(input())
for _ in range(t) :
    N, M = map(int, input().split())
    List = [[] for _ in range(N)]
    for i in range(M) :
        u, v = map(int, input().split())
        List[u].append(v)
        List[v].append(u)
    for i in range(N) :
        List[i].sort()
        
    Check = [False] * N
    DFS(0, List, Check)
    print('')