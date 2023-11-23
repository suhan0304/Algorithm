import sys
from collections import deque
import copy

input = sys.stdin.readline

def bfs(g) :
    g_index = 0
    q = deque()
    q.append([0,0,0,0,0])
    
    graph = []
    graph.append(copy.deepcopy(g))
    graph[0][0][0] = "-"
    while q :
        i, j, wall, dist, g_index = q.popleft()
        
        if i == n-1 and j == m-1 :
            print(dist+1)
            exit()
            
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        
        for d in range(4) :
            ni = i + di[d]
            nj = j + dj[d]
            
            if ni < 0 or n<= ni or nj < 0 or m <= nj :
                continue
            
            if graph[g_index][ni][nj] == '0' :
                graph[g_index][ni][nj] = "-"
                q.append([ni, nj, wall, dist+1, g_index])
                
            if graph[g_index][ni][nj] == '1' and wall == 0:
                graph.append(copy.deepcopy(graph[0]))
                graph[g_index+1][ni][nj] = "-"
                q.append([ni, nj, 1, dist+1, g_index+1])
        
    print(-1)
    

n, m = map(int,input().split())
g = []

for _ in range(n) :
    g.append(list(input().strip()))

bfs(g)