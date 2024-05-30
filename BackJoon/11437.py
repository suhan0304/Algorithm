import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(cur, d) :
    visited[cur] = True
    depth[cur] = d
    for nxt in graph[cur] :
        if visited[nxt] :
            continue
        parent[nxt] = cur
        dfs(nxt, d+1)

def lca(a, b) :
    while depth[a] != depth[b] :
        if depth[a] > depth[b] :
            a = parent[a]
        else :
            b = parent[b]

    while a != b :
        a = parent[a]
        b = parent[b]

    return a

n = int(input())

parent = [0] * (n+1)
depth = [0] * (n+1)
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

dfs(1, 0)

m = int(input())

for _ in range(m) :
    a, b = map(int, input().split())
    print(lca(a,b))
