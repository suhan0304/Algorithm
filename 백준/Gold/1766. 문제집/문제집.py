import sys
import heapq
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())

graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    degree[b] += 1

q = []
for i in range(1, n+1) :
    if degree[i] == 0 :
        heapq.heappush(q, i)

ans = []
while q :
    v = heapq.heappop(q)
    ans.append(v)
    for nv in graph[v] :
        degree[nv] -= 1
        if degree[nv] == 0 :
            heapq.heappush(q, nv)
            
print(" ".join(map(str, ans)))