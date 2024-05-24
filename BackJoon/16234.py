import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(n)] for _ in range(n)]

def bfs(sx, sy) :
    u = []
    q = deque((sx, sy))
    u.append((sx, sy))

    while q :
        x, y = q.popleft()
        visited[x][y] = True

        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r :
                    q.append((nx, ny))
                    u.append((nx, ny))
                    visited[nx][ny] = True

    if len(u) <= 1 :
        return 0
    result = sum(graph[x][y] for x,y in u) // len(u)
    for x, y in u :
    
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] == -1 :
                graph[i][j] = sum//cnt

                        
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            bfs(i, j)

for g in graph :
    print(*g)