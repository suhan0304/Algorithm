import sys
import math
sys.setrecursionlimit(10**5+1) 
input = sys.stdin.readline

n = int(input())
log_max = int(math.log2(n))+1

graph = [[] for _ in range(n+1)]
ancestor = [[[0, 0, 0] for _ in range(log_max)]  for _ in range(n+1)]
depth = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(n-1) :
    u, v, c = map(int, input().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

def dfs(cur, d) :
    visited[cur] = True
    depth[cur] = d
    for nxt, cost in graph[cur] :
        if visited[nxt] :
            continue
        ancestor[nxt][0] = [cur, cost, cost]
        dfs(nxt, d+1)

def set_ancestor() :
    dfs(1, 0) 

    for j in range(1, log_max):
        for i in range(1, n + 1):
            ancestor[i][j][0] = ancestor[ancestor[i][j-1][0]][j-1][0]
            ancestor[i][j][1] = min(ancestor[i][j-1][1], ancestor[ancestor[i][j-1][0]][j-1][1])
            ancestor[i][j][2] = max(ancestor[i][j-1][2], ancestor[ancestor[i][j-1][0]][j-1][2])

def lca(a, b) :
    shortest_path = float('inf')
    longest_path = 0

    if depth[a] > depth[b] :
        a, b = b, a

    for i in range(log_max-1, -1, -1) :
        if depth[b] - depth[a] >= (1 << i) :
            shortest_path = min(shortest_path, ancestor[b][i][1])
            longest_path = max(longest_path, ancestor[b][i][2])
            b = ancestor[b][i][0]

    if a == b :
        return shortest_path, longest_path
    
    for i in range(log_max-1, -1, -1) :
        if ancestor[a][i][0] != ancestor[b][i][0] :
            shortest_path = min(shortest_path, ancestor[a][i][1], ancestor[b][i][1])
            longest_path = max(longest_path, ancestor[a][i][2], ancestor[b][i][2])
            a = ancestor[a][i][0]
            b = ancestor[b][i][0]
    shortest_path = min(shortest_path, ancestor[a][i][1], ancestor[b][i][1])
    longest_path = max(longest_path, ancestor[a][i][2], ancestor[b][i][2])

    return shortest_path, longest_path

set_ancestor()

m = int(input())
for _ in range(m) :
    a, b = map(int, input().split())
    print(*lca(a,b))