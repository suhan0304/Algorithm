import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dist = [[0 for _ in range(n)] for _ in range(n)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

visited = [[False] * n for _ in range(n)]

island_q = deque()
q = deque()

island_num = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            island_num += 1
            visited[i][j] = True
            island_q.append([i, j])
            while island_q:
                i, j = island_q.popleft()
                graph[i][j] = island_num

                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                        visited[ni][nj] = True
                        if graph[ni][nj] == 1:
                            graph[ni][nj] = island_num
                            island_q.append([ni, nj])
                        if graph[ni][nj] == 0:
                            dist[ni][nj] = 1
                            graph[ni][nj] = island_num
                            q.append([ni, nj, island_num])

while q:
    i, j, island = q.popleft()

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < n and 0 <= nj < n:
            if not visited[ni][nj]:
                graph[ni][nj] = island
                dist[ni][nj] = dist[i][j] + 1
                visited[ni][nj] = True
                q.append([ni, nj, island])

            if visited[ni][nj] and graph[ni][nj] != island:
                print(dist[i][j] + dist[ni][nj])
                exit()
