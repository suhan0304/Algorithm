import sys
from collections import deque

input = sys.stdin.readline

s = input().strip()

ans = 0


q = deque()
for i in range(len(s)):
    if s[i] == "(":
        q.append(s[i])
    if s[i] == ")":
        if s[i - 1] == "(":  # 레이저
            q.pop()
            ans += len(q)
        else:
            q.pop()
            ans += 1

print(ans)
