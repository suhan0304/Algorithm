import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

di = [1,0,-1,0]
dj = [0,1,0,-1]

visited = [[Fale] * n for _ in range(n)]

q = deque
for i in range(n) :
    for j in range(n) :
        for d in range(4) :
            ni = i + di[d]
            nj = j + dj[d] 


def bfs() :

    while q :