import sys
from collections import deque
input = sys.stdin.readline

# input
n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
virus = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]

            
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

#count safe area
def count_safe_area(graph) :
    cnt = sum(row.count(0) for row in graph)
    return cnt

#bfs
def bfs(graph) :
    q = deque(virus)
    while q :
        i, j = q.popleft()
        for d in range(4) :
            ni,nj = i + di[d] ,j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0 :
                graph[ni][nj] = 2
                q.append([ni, nj])

#solve
def solution() :
    max_ans = 0

    

bfs()
for g in graph :
    print(g)

