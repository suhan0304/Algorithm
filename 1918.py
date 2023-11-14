import sys
from collections import deque

input = sys.stdin.readline

s = input().strip()

q = deque()

ans = []
for c in s:
    if c in ["+", "-", "*", "/", "(", ")"]:
        if c == ")":
            while q[-1] != "(":
                ans.append(q.pop())
            q.pop()
        elif c in ["*", "/"]:
            while q and q[-1] in ["*", "/"]:
                ans.append(q.pop())
            q.append(c)
        elif c in ["+", "-"]:
            while q and q[-1] in ["+", "-", "*", "/"]:
                ans.append(q.pop())
            q.append(c)
        else:
            q.append(c)
    else:
        ans.append(c)
while q:
    ans.append(q.pop())

print("".join(ans))
