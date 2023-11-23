import sys
from collections import deque

input = sys.stdin.readline

q = deque()
l = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

q.append([x1, y1, 0])
visited = []

while q:
    i, j, depth = q.popleft()

    if i == x1 and j == y2:
        print(depth)
        exit()

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if ni < 0 or l <= ni or nj < 0 or l <= nj:
            continue

        if [ni, nj] not in visited:
            q.append([nj, ni, depth + 1])
            visited.append([ni, nj])
