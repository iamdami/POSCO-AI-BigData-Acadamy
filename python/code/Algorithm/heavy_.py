for t in range(int(input())) :
    N, C = map(int, input().split())
    liquidLs = list()
    
    for i in range(N) :
        w, v = map(int, input().split())
        liquidLs.append((w / v, w, v)) 
    liquidLs.sort(reverse = True)
    
    maxW = 0
    for i in range(N) :
        if C >= liquidLs[i][2] :  
            maxW += liquidLs[i][1]
            C -= liquidLs[i][2]
        else : # all 
            maxW += C * (liquidLs[i][0])
            break
            
    print(int(maxW))