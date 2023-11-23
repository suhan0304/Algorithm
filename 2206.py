import sys
from collections import deque

input = sys.stdin.readline

def bfs() :
    q = deque()
    q.append([0,0,0])
    
    dist = [[0 for _ in range(m)] for _ in range(n) ]
    graph[0][0] = "-"
        
    while q :
        i, j, wall = q.popleft()
        
        if i == n-1 and j == m-1 :
            print(dist[i][j]+1)
            exit()
            
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        
        for d in range(4) :
            ni = i + di[d]
            nj = j + dj[d]
            
            if ni < 0 or n<= ni or nj < 0 or m <= nj :
                continue
            
            if graph[ni][nj] == '0' :
                q.append([ni, nj, wall])
                graph[ni][nj] = "-"
                dist[ni][nj] = dist[i][j] + 1
            
            if graph[ni][nj] == '1' and wall == 0:
                q. append([ni, nj, 1])
                graph[ni][nj] = "-"
                dist[ni][nj] = dist[i][j] + 1
        
    print(-1)
    

n, m = map(int,input().split())
graph = []

for _ in range(n) :
    graph.append(list(input().strip()))

bfs()