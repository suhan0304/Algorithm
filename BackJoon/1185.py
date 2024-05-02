import sys
input = sys.stdin.readline

def find(n) :
    if parent[n] != n :
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a > b : parent[b] = a
    else : parent[a] = b

n, p = map(int,input().rstrip().split())

visit_cost = [-1]
for _ in range(n) :
    visit_cost.append(int(input()))

edges = []
for i in range(p) :
    s, e, l = map(int,input().rstrip().split())
    edges.append((s, e, l))
edges.sort(key = lambda x : x[2])

parent = list(range(n+1))
ans = 0
for s, e, l in edges :
    if find(s) != find(e) :
        union(s, e)
        ans += l
print(ans)