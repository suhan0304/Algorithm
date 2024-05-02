import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(n) :
    if parent[n] != n :
        parent[n] = find(parent[n])
    return parent[n]

def union(a,b) :
    a = find(a)
    b = find(b)
    if a > b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().rstrip().split())
edges = [tuple(map(int,input().rstrip().split())) for _ in range(m)]
edges.sort(key = lambda x : x[2])

parent = list(range(n+1))
ans = 0
for a, b, c in edges :
    if find(a) != find(b) :
        union(a,b)
    else :
        ans += c

for i in range(n+1) :
    parent[i] = find(i)
    
print(ans if len(set(parent[1:])) == 1 else -1)