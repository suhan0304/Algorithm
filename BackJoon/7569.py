import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph) :
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    ans = 0
    cnt = 0
    while q :
        z, y, x, depth = q.popleft()
        ans = max(ans, depth)

        for d in range(6) :
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h :
                if graph[nz][ny][nx] == 0 :
                    cnt += 1
                    graph[nz][ny][nx] = 1
                    q.append([nz, ny, nx, depth+1])
    print(depth-1 if cnt == tomato_cnt else -1)


m, n, h = map(int, input().rstrip().split())

graph = [[] for _ in range(h)]
q = deque()

tomato_cnt = 0
for i in range(h) :
    for j in range(n) :
        graph[i].append(list(map(int,input().rstrip().split())))
        for k in range(m) :
            if graph[i][j][k] == 1 :
                q.append([i, j, k, 1])
            elif graph[i][j][k] == 0 :
                tomato_cnt += 1

#print(q, tomato_cnt)

if tomato_cnt == 0 :
    print(0)
else : 
    bfs(graph)