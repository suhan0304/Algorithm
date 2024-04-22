import sys
from collections import deque
from collections import Counter

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

q = deque()

cnt = Counter(a)

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
