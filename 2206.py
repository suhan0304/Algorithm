import sys
from collections import deque
import copy

input = sys.stdin.readline


def bfs():
    dist = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]

    q = deque()
    q.append([0, 0, 0])

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    graph[0][0][0], graph[1][0][0] = "-", "-"

    while q:
        i, j, wall = q.popleft()

        if i == n - 1 and j == m - 1:
            print(dist[i][j][wall])
            exit

    return


n, m = map(int, input().split())
temp = []
for _ in range(n):
    temp.append(list(input().strip()))


graph = [temp, copy.deepcopy(temp)]

bfs()
