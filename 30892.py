import sys
from collections import deque
input = sys.stdin.readline

N, K, T = map(int,input().rstrip().split())

arr = sorted(list(map(int,input().rstrip().split())))

sharks = deque(arr)
can_eat = deque()

for i in range(K) :
    while sharks and sharks[0] < T :
        can_eat.append(sharks.popleft())
    if not can_eat :
        break
    T += can_eat.pop()

print(T)