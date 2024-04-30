import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(n) :
    if parent[n] != n :
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a > b:
        parent[b] = a
    else :
        parent[a] = b

while 1 :
    m, n = map(int,input().rstrip().split())
    if m==n==0 : break
    edges = [tuple(map(int,input().rstrip().split())) for _ in range(n)]
    edges.sort(key = lambda x : x[2])

    parent = list(range(m))
    ans = 0
    for x, y, z in edges :
        if find(x) != find(y) :
            union(x, y)
        else :
            ans += z 

    print(ans)