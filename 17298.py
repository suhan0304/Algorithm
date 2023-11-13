import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

q = deque()
ans = []

for i in range(n - 1, -1, -1):
    while q and q[-1] <= a[i]:
        q.pop()
    if not q:
        ans.append(-1)
    else:
        ans.append(q[-1])
    q.append(a[i])
ans.reverse()
print(*ans)
