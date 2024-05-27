import sys
from collections import deque
input = sys.stdin.readline

n, a, b = map(int, input().split())

if a + b - 1 > n :
    print(-1)
    exit(0)

q_left = deque()
q_right = deque()

if a > b :

elif a < b :
    for i in range(1, a+1) :
        q_left.append(i)
    for j in range(1, b) :
        q_right.append(j)

    while q_right :
        q_left.append(q_right.pop())
else :

print(*list(q_left))