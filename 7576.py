import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(graph, i, j):
    q_1 = deque()
    q_1.append([0, 0, 1])

    q_2 = deque()

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]


k = 0
arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            k += 1
        if graph[i][j] == 1:
            arr.append([i, j])

print(arr)

bfs()
