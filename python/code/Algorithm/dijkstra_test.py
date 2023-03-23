import heapq

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v, c = map(int, input().split())
        graph[u].append([v,c])

    visited = [False] * N
    dist = [-1] * N
    hq = list()
    heapq.heappush(hq, (0,0))

    while len(hq) > 0:
        d, u = heapq.heappop(hq)
        if visited[u] == False:
            visited[u] = True
            dist[u] = d
            for i in graph[u]:
                if visited[i[0]] == False:
                    heapq.heappush(hq, [d + i[1], i[0]])
    print(dist[-1])