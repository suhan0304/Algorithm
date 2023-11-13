import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

q = deque()

cnt = dict()
for i in range(len(a)):
    if a[i] not in cnt:
        cnt[a[i]] = a.count(a[i])

ans = []
for i in range(n - 1, -1, -1):
    while q and cnt[q[-1]] <= cnt[a[i]]:
        q.pop()
    if not q:
        ans.append(-1)
    else:
        ans.append(q[-1])
    q.append(a[i])
ans.reverse()

print(*ans)
ans = []
