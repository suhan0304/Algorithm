import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

def bfs(start_x, start_y) :
    q = deque()
    q.append((start_x, start_y))

    sum = graph[start_x][start_y]
    cnt = 1

    while q :
        x, y = q.popleft()
        graph[x][y] = -1
        sum += graph[x][y]
        cnt += 1
        visited[x][y] = True

        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r :
                    q.append((nx, ny))
    
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