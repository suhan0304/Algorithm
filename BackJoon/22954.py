import sys
input = sys.stdin.readline
 
def union(u, v) :
    u = find(u)
    v = find(v)

    parent[v] = u 

def find(a) :
    if parent[a] != a :
        return find(parent[a])
    return a

n, m = map(int, input().split())

parent = list(range(n+1))
for _ in range(m) :
    u, v = map(int, input().split())
    if find(u) != find(v) :
        union(u, v)

print(parent)