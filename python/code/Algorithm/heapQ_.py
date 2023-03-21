import heapq
"""
hq = [] : 빈 우선순위 큐 선언
heapq.heappush(hq, n) : hq에 n 삽입
heapq.heappop(hq) : hq에서 pop하여 반환
"""
t = int(input())
for _ in range(t):
    hq = []
    ans = []
    n = int(input())
    qry = list(map(int, input().split()))
    for q in qry:
        if q > 0:
            heapq.heappush(hq, q)
        else:
            ans.append(heapq.heappop(hq))
    print(*ans)