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
            if 0<=ni<h and 0 <= nj < w and graph[ni][nj] != '#'  :
                fire_q.append([ni, nj])
                graph[ni][nj] = '*'
    
def bfs() :
    while q :
        fire_bfs()
        for _ in range(len(q)) :
            i, j, depth = q.popleft()
            if i == 0 or i == h-1 or j == 0 or j == w-1 :
                print(depth+1)
                return
            
            for d in range(4) :
                ni = i + di[d]
                nj = j + dj[d]
                if 0<=ni<h and 0 <= nj < w and graph[ni][nj] == '.' :
                    q.append([ni,nj,depth+1])
                    graph[ni][nj] = '-'
            
            #for g in graph :
            #    print("".join(g))
            #print()
        
    print('IMPOSSIBLE')
        
t = int(input().rstrip())
for _ in range(t) : 
    w, h = map(int, input().rstrip().split())
    graph = [list(input().rstrip()) for _ in range(h)]

    q = deque()
    fire_q = deque()

    for i in range(h) :
        for j in range(w) :
            if graph[i][j] == '@' :
                q.append([i,j,0])
                graph[i][j] = '-'
            elif graph[i][j] == '*' :
                fire_q.append([i, j]) 
                
    bfs()