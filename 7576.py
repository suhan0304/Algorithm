import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(graph, i, j):
    global ans

    q = deque()
    q.append([0, 0])

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    while q:
        i, j = q.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if ni < 0 or n <= ni or nj < 0 or m <= nj:
                continue

            if graph[ni][nj] == 0:
                ans += 1
                graph[ni][nj] = 1
                q.append([ni, nj])


cnt = 0
arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1
        if graph[i][j] == 1:
            arr.append([i, j])

ans = 0
for i, j in arr:
    bfs(graph, i, j)
