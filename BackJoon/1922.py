import sys
input = sys.stdin.readline

def find_root(n) :
    if parent[n] != n :
        parent[n] = find_root(parent[n])
    return parent[n]

def union(a, b) :
    a = find_root(a)
    b = find_root(b)

    if a > b :
        parent[b] = a
    else :
        parent[a] = b

v = int(input())
e = int(input())
edges = [tuple(map(int,input().rstrip().split())) for _ in range(e)]
edges.sort(key = lambda x : x[2])


parent = list(range(v+1))
ans = 0
for a, b, c in edges :
    if find_root(a) != find_root(b) :
        union(a, b)
        ans += c

print(ans)
