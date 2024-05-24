import sys
import math
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

n, m = map(int, input().rstrip().split())

stars = []
for _ in range(n) :
    stars.append(tuple(map(int, input().rstrip().split())))

edges = []
for i in range(n) :
    for j in range(i+1, n) :
        edges.append((i,j,math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)))
edges.sort(key = lambda x : x[2])

parent = list(range(n))

for _ in range(m) :
    a, b = map(int, input().rstrip().split())
    union(a-1, b-1)

ans = 0.
for a, b, c in edges :
    if find(a) != find(b) :
        union(a, b)
        ans += c
print("{:.2f}".format(round(ans,2)))
