t = int(input())
for _ in range(t):
    stack = []
    ans = []
    n = int(input())
    qry = list(map(int, input().split()))
    for q in qry:
        if q > 0:
            stack.append(q)
        else:
            ans.append(stack.pop())
    print(*ans)