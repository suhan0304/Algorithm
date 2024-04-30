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

n, m = map(int, input().rstrip().split())
e = [tuple(map(int,input().rstrip().split())) for _ in range(m)]
e.sort(key = lambda x : x[2])

parent = []
