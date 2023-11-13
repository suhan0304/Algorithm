import sys
from collections import deque

input = sys.stdin.readline

# 오른쪽에서 왼쪽으로 push하면서 진행
# 들어오는 숫자가 스택의 맨 위 숫자보다 크다면 pop


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

print(ans)
