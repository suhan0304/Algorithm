import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    queue = deque()
    queue.append([0, 0])
    graph[0][0] = "0"

    cnt = 1

    while queue:
        i, j = queue.popleft()
        cnt += 1

        if i == n - 1 and j == m - 1:
            print(dist[i][j])
            exit()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if ni < 0 or n <= ni or nj < 0 or m <= nj:
                continue

            if graph[ni][nj] == "1":
                dist[ni][nj] = dist[i][j] + 1
                queue.append([ni, nj])
                graph[ni][nj] = "0"
    return


n, m = map(int, input().split())
graph = []
dist = [[0 for _ in range(m)] for _ in range(n)]
dist[0][0] = 1

for _ in range(n):
    graph.append(list(input().strip()))

bfs(graph)
