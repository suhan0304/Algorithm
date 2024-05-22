from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n) :
    graph.append(input().rstrip())

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 'R' :
            rx, ry = i, j
        elif graph[i][j] == 'B' :
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by) :
    q = deque()
    q.append((rx,ry,bx,by))
    visited = []
    visited.append((rx,ry,bx,by))
    cnt = 0
    while q :
        for _ in range(len(q)) :
            rx, ry, bx, by = q.popleft()
            if cnt > 10 :
                print(-1)
                break
            if graph[rx][ry] == 'O' :
                print(cnt)
                return
            for d in range(4) :
                
                nrx, nry = rx, ry
                while True :
                    nrx = nrx + dx[d]
                    nry = nry + dy[d]
                    if graph[nrx][nry] == '#' :
                        nrx -= dx[d]
                        nry -= dy[d]
                        break
                    if graph[nrx][nry] == 'O' :
                        break

                nbx, nby = bx, by
                while True :
                    nbx = nbx + dx[d]
                    nby = nby + dy[d]
                    if graph[nbx][nby] == '#' : 
                        nbx -= dx[d]
                        nby -= dy[d]
                        break
                    if graph[nbx][nby] == 'O' :
                        break

                if graph[nbx][nby] == 'O' :  continue

                if nrx == nbx and nry == nby :
                    if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by) :
                        nrx -= dx[d]
                        nry -= dy[d]
                    else :
                        nbx -= dx[d]
                        nby -= dy[d]
                if (nrx,nry,nbx,nby) not in visited :
                    visited.append((nrx,nry,nbx,nby))
                    q.append((nrx,nry,nbx,nby))
        cnt += 1
    print(-1)
    
bfs(rx, ry, bx, by)