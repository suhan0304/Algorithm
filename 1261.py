import sys
from collections import deque
input = sys.stdin.readline

# input
m, n = map(int,input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# bfs
def bfs() :
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    
    q = deque()
    q.append([0, 0, 0])
    while q :
        i, j, wall = q.popleft()

        if i == n-1 and j == m-1 :
            return wall
        
        for d in range(4) :
            ni = i + di[d]
            nj = j + dj[d]
            
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] :
                visited[ni][nj] = True
                if graph[ni][nj] == '0' :
                    q.appendleft([ni,nj,wall])
                if graph[ni][nj] == '1' :
                    q.append([ni,nj,wall+1])
                    
print(bfs())