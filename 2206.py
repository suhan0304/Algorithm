import sys
from collections import deque
import copy

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append([0, 0, 0, 0])

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    graph[0][0][0], graph[1][0][0] = "-", "-"

    while q:
        i, j, wall, dist = q.popleft()

        if i == n - 1 and j == m - 1:
            print(dist + 1)
            exit()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if ni < 0 or n <= ni or nj < 0 or m <= nj:
                continue

            if graph[wall][ni][nj] == "0":
                graph[wall][ni][nj] = "-"
                q.append([ni, nj, wall, dist + 1])

            if graph[wall][ni][nj] == "1" and wall == 0:
                graph[0][ni][nj] = "-"
                graph[1][ni][nj] = "-"

                q.append([ni, nj, 1, dist + 1])

    print(-1)


n, m = map(int, input().split())
temp = []
for _ in range(n):
    temp.append(list(input().strip()))


graph = [temp, copy.deepcopy(temp)]

bfs()
