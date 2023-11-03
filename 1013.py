import sys

input = sys.stdin.readline


T = int(input())

from collections import deque

ans = True
for _ in range(T):
    q = deque(input()[:-1])
    while len(q) >= 2:
        if len(q) >= 3 and q[0] == "1" and q[1] == "0" and q[2] == "0":
            for _ in range(3):
                q.popleft()
            while q[0] == "0":
                q.popleft()
            if len(q) >= 3 and q[0] == "1" and q[1] == "0" and q[2] == "0":
                ans = False
                break
            elif q and q[0] == "1":
                while q and q[0] == "1":
                    q.popleft()
            else:
                ans = False
                break
        elif q[0] == "0" and q[1] == "1":
            for _ in range(2):
                q.popleft()
        else:
            ans = False
            break

    if len(q) != 0:
        ans = False

    print("YES" if ans else "NO")
