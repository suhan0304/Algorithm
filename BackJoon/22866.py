import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

ans = [[0, -1] for _ in range(n)]
q = []
for i in range(n) :
    if i == 0 :
        q.append((i, heights[i]))
        continue

    while q and q[-1][1] <= heights[i] :
        q.pop()

    if q :
        ans[i][0] += len(q)
        ans[i][1] = q[-1][0]
    q.append((i, heights[i]))

q = []
for i in range(n-1, -1, -1) :
    if i == n-1 :
        q.append((i, heights[i]))
        continue

    while q and q[-1][1] <= heights[i] :
        q.pop()

    if q :
        ans[i][0] += len(q)
        if ans[i][1] == -1 :
            ans[i][1] = q[-1][0]
        else :
            if abs(i-ans[i][1]) > abs(i-q[-1][0]) :
                ans[i][1] = q[-1][0]

    q.append((i, heights[i]))
    
for a, h in ans :
    if a == 0 :
        print(a)
    else :
        print(a, h+1)