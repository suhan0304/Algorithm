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

n = int(input())
stars = [tuple([i] + list(map(int,input().rstrip().split()))) for i in range(n)]

edges = []
for i in [1, 2, 3] :
    sort_stars = sorted(stars, key = lambda x : x[i]) 
    edges = [(abs(star1[i] - star2[i]), star1[0], star2[0]) for star1 ,star2 in zip(sort_stars[:-1], sort_stars[1:])]
edges.sort()

ans = 0
parent = list(range(n+1))

