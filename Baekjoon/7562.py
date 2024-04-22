import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())


def bfs():
    di = [-1, 1, 2, 2, 1, -1, -2, -2]
    dj = [2, 2, 1, -1, -2, -2, -1, 1]

    q = deque()
    q.append((x1, y1))
    while q:
        i, j = q.popleft()
        if i == x2 and j == y2:
            return graph[i][j] - 1
        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < l and 0 <= nj < l and graph[ni][nj] == 0:
                graph[ni][nj] = graph[i][j] + 1
                q.append((ni, nj))


for _ in range(t):
    l = int(input().rstrip())
    x1, y1 = map(int, input().rstrip().split())
    x2, y2 = map(int, input().rstrip().split())
    graph = [[0] * l for _ in range(l)]
    graph[x1][y1] = 1
    print(bfs())
