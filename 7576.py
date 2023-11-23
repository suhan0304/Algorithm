import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(graph, i, j):
    q = deque()
    q.append([0, 0])

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    while q:
        i, j = q.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

    return


cnt = 0
arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1
        if graph[i][j] == 1:
            arr.append([i, j])

for i, j in arr:
    bfs(graph, i, j)
