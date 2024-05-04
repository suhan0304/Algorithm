import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]

INF = 1e5
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m) :
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))

def dijkstra(start) :
    q = []
    distance = [INF] * (n+1)

    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q :
        v, dist = heapq.heappop(q)

        if distance[v] < dist :
            continue

        for nv, nd in graph[v] :
            d = dist + nd

            if distance[nv] > d :
                distance[nv] = d
                heapq.heappush(q, (nv, d))
    return distance

ans = 0
for i in range(1, v+1) :
    go = dijkstra(i)
    back = dijkstra(x)
    ans = max(ans, go[x] + back[i])

print(ans)