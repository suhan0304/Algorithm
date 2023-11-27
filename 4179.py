import sys
from collections import deque

input = sys.stdin.readline

di = [1,0,-1,0]
dj = [0,1,0,-1]

def fire_bfs() :
    for i in range(len(fire_q)) :
        i, j = fire_q.popleft()
        
        for d in range(4) :
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<R and 0 <= nj < C and graph[ni][nj] == '.'  :
                fire_q.append([ni, nj])
                graph[ni][nj] = 'F'
    
def bfs() :
    while q :
        fire_bfs()
        for _ in range(len(q)) :
            i, j, depth = q.popleft()
            if i == 0 or i == R-1 or j == 0 or j == C-1 :
                print(depth+1)
                return
            
            for d in range(4) :
                ni = i + di[d]
                nj = j + dj[d]
                if 0<=ni<R and 0 <= nj < C and graph[ni][nj] == '.' :
                    q.append([ni,nj,depth+1])
                    graph[ni][nj] = '-'
            
        
    print('IMPOSSIBLE')
        
R, C = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(R)]

q = deque()
fire_q = deque()

for i in range(R) :
    for j in range(C) :
        if graph[i][j] == 'J' :
            q.append([i,j,0])
            graph[i][j] = '-'
        elif graph[i][j] == 'F' :
            fire_q.append([i, j]) 
            
bfs()