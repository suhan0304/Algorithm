import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

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
        graph[x][y] = result
    return 1

ans = 0
while 1 :
    flag = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                visited[i][j] = True
                flag += bfs(i, j)
    if flag == 0 :
        break
    ans += 1
print(ans)
