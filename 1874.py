import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()

a = 1
ans = []
for i in range(1, n + 1):
    m = int(input())
    while a <= m:
        ans.append("+")
        q.append(a)
        a += 1
    if q.pop() != m:
        ans.append("NO")
        break
    else:
        ans.append("-")
if ans[-1] == "NO":
    print("NO")
else:
    print("\n".join(ans))
