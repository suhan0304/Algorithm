import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
log_max = 17 

n = int(input())

ancestor = [[0] * (log_max) for _ in range(n+1)]
total_cost = [0] * (n+1)
depth = [0] * (n+1)
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    u, v, w = map(int, input().split())
    graph[v].append((u, w))
    graph[u].append((v, w))

def dfs(cur, d, cost) :
    visited[cur] = True
    depth[cur] = d
    total_cost[cur] = cost
    for nxt, c in graph[cur] :
        if visited[nxt] :
            continue
        ancestor[nxt][0] = cur
        dfs(nxt, d+1, cost + c)

def set_ancestor() :
    dfs(1, 0, 0)
    for i in range(1, log_max) :
        for j in range(1, n+1) :
            ancestor[j][i] = ancestor[ancestor[j][i-1]][i-1]

def lca(a, b) :
    if depth[a] > depth[b] :
        a, b = b, a
    for i in range(log_max-1, -1, -1) :
        if depth[b] - depth[a] >= (1 << i) :
            b = ancestor[b][i]

    if a == b : 
        return a
    
    for i in range(log_max-1, -1, -1) :
        if ancestor[a][i] != ancestor[b][i] :
            a = ancestor[a][i]
            b = ancestor[b][i]

    return ancestor[a][0]

set_ancestor()

m = int(input())
for _ in range(m) :
    a, b = map(int, input().split())
    ans = total_cost[a] + total_cost[b]
    ans -= 2 * total_cost[lca(a, b)]
    print(ans)
