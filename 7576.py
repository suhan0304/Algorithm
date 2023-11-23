import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, i, j):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for i, j in arr:
        q.append([i, j, 1])

    while q:
        i, j, depth = q.popleft()


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()

tomato = 0
arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            tomato += 1
        if graph[i][j] == 1:
            arr.append([i, j])

bfs()
