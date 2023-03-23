for _ in range(int(input())):
    N, M = map(int, input().split())

    data = list()
    for i in range(N):
        data.append(list(map(int, input().split())))

    kan = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:     
                kan[i][j] = data[i][j]
            elif i == 0:                 
                kan[i][j] = kan[i][j-1] + data[i][j]
            elif j == 0:               
                kan[i][j] = kan[i-1][j] + data[i][j]
            else:                    
                kan[i][j] = min(kan[i][j-1], kan[i-1][j], kan[i-1][j-1]) + data[i][j]
                
    print(kan[N-1][M-1])              