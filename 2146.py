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
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if (
                    0 <= ni < n
                    and 0 <= nj < n
                    and not visited[ni][nj]
                    and graph[ni][nj] == 0
                ):
                    visited[ni][nj] = True
                    q.append([ni, nj, 1])

print("시작 지점들")
for v in visited:
    for a in v:
        print(0 if a else 1, end=" ")
    print()


print(q)
