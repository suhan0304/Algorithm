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
            visited[i][j] = True
            q.append([i, j])
            island_num = 2
            while q:
                i, j = q.popleft()
                graph[i][j] = island_num

                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] == 1:
                        visited[ni][nj] = True
                        graph[ni][nj] = island_num
                        q.append([ni, nj])

            island_num += 1

for g in graph:
    print(g)


print()
for g in graph:
    print(g)
