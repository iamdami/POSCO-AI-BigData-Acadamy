import collections

t = int(input())
for _ in range(t):
    queue = collections.deque([])
    ans = []
    n = int(input())
    qry = list(map(int, input().split()))
    for q in qry:
        if q > 0:
            queue.append(q)
        else:
            ans.append(queue.popleft())
    print(*ans)