import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    q = deque()
    l = int(input())

    graph = [[False for _ in range(l)] for _ in range(l)]

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    di = [-2, -2, 2, 2, -1, -1, 1, 1]
    dj = [-1, 1, -1, 1, -2, 2, -2, 2]

    q.append([x1, y1, 0])
    visited = []

    while q:
        i, j, depth = q.popleft()

        if i == x2 and j == y2:
            print(depth)
            break

        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]

            if ni < 0 or l <= ni or nj < 0 or l <= nj:
                continue

            if [ni, nj] not in visited:
                q.append([nj, ni, depth + 1])
                visited.append([ni, nj])
