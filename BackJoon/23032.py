import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, start, end) :
    print(start)
    visited = [False] * (n+1)
    max_dist = 0
    q = deque([(start, 0)])

    while q :
        v, _ = q.pop()
        if v == end :
            return max_dist

        for nv, nd in graph[v] :
            if not visited[nv] :
                if max_dist < nd :
                    max_dist = nd
                visited[nv] = True
                q.append((nv, max_dist))
    return

def find(n) :
    if parent[n] != n :
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a > b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int,input().rstrip().split())

edges = [tuple(list(map(int,input().rstrip().split()))) for _ in range(m)]
edges.sort(key = lambda x : x[2])
parent = list(range(n+1))

mst_edges = []
mst_graph = [[] for _ in range(n+1)]
total_cost = 0
for a, b, c in edges :
    if find(a) != find(b) :
        union(a, b)
        total_cost += c
        mst_edges.append((a, b, c))
        mst_graph[a].append((b,c))
        mst_graph[b].append((a,c))

q_cnt = int(input())

for _ in range(q_cnt) :
    x, y = map(int,input().rstrip().split())
    dfs(mst_graph, x, y)
