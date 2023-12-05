import sys
from collections import deque
input = sys.stdin.readline

N, K, T = map(int,input().rstrip().split())

arr = sorted(list(map(int,input().rstrip().split())))

cnt = 1
q=deque(arr)
size = T

while q[0] < size :
    eat = q.popleft()
size += eat
cnt += 1