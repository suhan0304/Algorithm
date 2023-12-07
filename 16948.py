import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
r1, c1, r2, c2 = map(int,input().rstrip().split())

dr = [-2, -2, 0, 0, 2, 2] 
dc = [-1, 1, -2, 2, -1, 1]

visited = [[-1 for _ in range(N)] for _ in range(N)]

def bfs() :
    q = deque()
    q.append((r1, c1))
    visited[r1][c1] = 0
    
    while q :
        r, c = q.popleft()
        
        if r==r2 and c==c2 :
            print(visited[r][c])
            exit(0)
        
        for d in range(6) :
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == -1 :
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
                
bfs()
print(-1)