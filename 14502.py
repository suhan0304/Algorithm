import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

# input
n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

empty = []
virus = []
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 : empty.append((i,j))
        if graph[i][j] == 2 : virus.append((i,j))
            
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


#bfs
def bfs(graph) :
    virus_cnt = 0
    q = deque(virus)
    while q :
        i, j = q.popleft()
        for d in range(4) :
            ni,nj = i + di[d] ,j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0 :
                graph[ni][nj] = 2
                cnt += 1
                q.append([ni, nj])
    return virus_cnt

#solve
def solution() :
    max_ans = 0
    walls_comb = list(combinations(empty, 3))

    for walls in walls_comb :
        for wall in walls :
            graph[wall[0]][wall[1]] = 1
    
        cnt = bfs(graph)

        max_ans = max(max_ans, cnt)

        for wall in walls :
            graph[wall[0]][wall[1]] = 0

    return max_ans

print(solution())

