import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

t = int(input())

def dfs(cur, d) :
    visited[cur] = True
    depth[cur] = d 
    for nxt in graph[cur] :
        if visited[nxt] :
            continue
        dfs(nxt, d+1)

def lca(a, b) :
    while depth[a] != depth[b] :
        if depth[a] > depth[b] :
            a = parent[a]
        else :
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

for _ in range(t) :
    n = int(input())

    graph = [[] for _ in range(n+1)]
    parent = [0] * (n+1)
    depth = [0] * (n+1)
    visited = [False] * (n+1)

    for _ in range(n-1) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        parent[b] = a
    
    for i in range(n+1) :
        if parent[i] == 0 :
            dfs(i, 0)

    a, b = map(int, input().split())
    print(lca(a, b))