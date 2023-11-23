import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for i, j in arr:
        q.append([i, j, 1])

    max_depth = 0
    cnt = 0
    while q:
        i, j, depth = q.popleft()
        max_depth = max(max_depth, depth)

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if ni < 0 or n <= ni or nj < 0 or m <= nj:
                continue

            if graph[ni][nj] == 0:
                graph[ni][nj] = 1
                cnt += 1
                q.append([ni, nj, depth + 1])
    print(max_depth - 1 if cnt == tomato else -1)


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

if tomato == 0:
    print(0)
    exit()

bfs(graph)
