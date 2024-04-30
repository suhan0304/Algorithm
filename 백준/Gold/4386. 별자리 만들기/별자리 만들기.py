import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(m) :
    if parent[m] != m :
        parent[m] = find(parent[m])
    return parent[m]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a > b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
stars = []
for i in range(n) :
    stars.append(tuple(map(float, input().rstrip().split())))

edges = []
for i in range(n) :
    for j in range(i+1, n) :
        edges.append((i, j, math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)))
edges.sort(key = lambda x : x[2])

parent = list(range(n))
ans = 0.
for a, b, dist in edges :
    if find(a) != find(b) :
        union(a,b)
        ans += dist
print(ans)