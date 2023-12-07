import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

pos, neg = [], []
for _ in range(N) :
    k = int(input())
    if k > 0 :
        pos.append(k)
    else :
        neg.append(k)

pos.sort()
neg.sort()

pos = deque(pos)
neg = deque(neg)

ans = 0
while len(pos) >= 2 :
    a, b= pos.pop() * pos.pop()
    if a == 1 or b == 1 or a == 0 or b == 0:
        ans += a + b
    else :
        ans += a * b
