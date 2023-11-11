import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()

i = 1
ans = []
while i < n:
    m = int(input())
    if i < m:
        while i <= m:
            ans.append("+")
            q.append(i)
            i += 1
    if q.pop() != m:
        print("NO")
    else:
        ans.append("-")

print(ans)
