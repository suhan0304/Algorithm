import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

visited = [[False] * n for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = -1
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if (
                    0 <= ni < n
                    and 0 <= nj < n
                    and not visited[ni][nj]
                    and graph[ni][nj] == 0
                ):
                    graph[ni][nj] = 1
                    visited[ni][nj] = True
                    q.append([ni, nj])

for g in graph:
    print(g)

while q:
    i, j = q.popleft()

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < n and 0 <= nj < n:
            if graph[ni][nj] == 0:
                q.append([ni, nj])
                graph[ni][nj] = graph[i][j] + 1
            elif graph[ni][nj] > 0:
                for g in graph:
                    print(g)

                print(i, j, ni, nj)
                print(graph[i][j] + graph[ni][nj])
                exit()
