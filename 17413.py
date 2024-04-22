import sys
from collections import deque

input = sys.stdin.readline

s = input().strip()
backward = True

ans = []
q = deque()

i = 0

while i < len(s):
    if s[i] == "<":
        while q:
            ans.append(q.pop())
        while s[i] != ">":
            ans.append(s[i])
            i += 1
        ans.append(s[i])
        i += 1
    else:
        if s[i] == " ":
            while q:
                ans.append(q.pop())
            ans.append(s[i])
        else:
            q.append(s[i])
        i += 1
while q:
    ans.append(q.pop())
print("".join(ans))
