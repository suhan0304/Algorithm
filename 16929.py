import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 하 우 상 좌
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def dfs(i, j, start):
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == start:
            if not visited[ni][nj]:
                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] + 1
                dfs(ni, nj, start)
            elif visited[ni][nj] and dist[ni][nj] >= dist[i][j] + 3:
                print(dist)
                print("Yes")
                exit()


graph = []

for _ in range(n):
    graph.append(input().strip())

dist = [[0 for _ in range(m)] for _ in range(n)]

visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, graph[i][j])

print("No")
