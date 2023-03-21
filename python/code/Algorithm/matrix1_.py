t = int(input())

for _ in range(t) :
    N, M = map(int, input().split())
    mat = [[0]*N for _ in range(N)]
    
    for _ in range(M) :
        u, v, c = map(int, input().split())        
        mat[u][v] = c
    
    for i in range(N) :
        print(*mat[i])