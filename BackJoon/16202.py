import sys
input = sys.stdin.readline

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

def edges_update(edges, min_edge) :
    edges = [edge for edge in edges if edge[0] != min_edge]
    return edges

n, m, k = map(int, input().rstrip().split())
edges = [tuple([i+1] + list(map(int, input().rstrip().split()))) for i in range(m) ]
edges.sort()

parent = []
for i in range(k) :
    score = 0
    min_edge = 10**6
    parent = list(range(n+1))
    for d, x, y in edges :
        if find(x) != find(y) :
            if d < min_edge :
                min_edge = d
            union(x, y)
            score += d

    for j in range(1, n+1) :
        parent[j] = find(parent[j])
    
    if len(set(parent[1:])) == 1 : 
        print(score, end=' ')
        edges = edges_update(edges, min_edge)
    else :
        for j in range(k-i) :
            print(0, end=' ')
        break