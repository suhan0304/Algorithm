import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()

for _ in range(n):
    ps = input().strip()
    ans = ""
    q.clear()
    for c in ps:
        if c == "(":
            q.append("(")
        elif c == ")":
            if not q:
                ans = "NO"
                break
            else:
                q.pop()
    if q:
        ans = "NO"
    print(ans if ans == "NO" else "YES")
