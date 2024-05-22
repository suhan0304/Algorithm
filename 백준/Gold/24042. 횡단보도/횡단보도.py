import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m) :
    u, v = map(int, input().split())
    graph[u].append((i, v))
    graph[v].append((i, u))

def dijkstra() :
    q = []
    d = [sys.maxsize for _ in range(n+1)]
    heapq.heappush(q, (0, 1))
    d[1] = 0

    while q :
        time, v  = heapq.heappop(q)
        if v == n :
            print(time)
            return
        if d[v] < time : continue
        
        for i, nv in graph[v] :
            nt = i+((time-i)//m)*m if (time-i)%m==0 else i+((time-i)//m+1)*m
            if d[nv] > nt + 1 :
                d[nv] = nt + 1
                heapq.heappush(q, (nt+1, nv))

dijkstra()