import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


find_route = False


def findRing(route, v, visited):
    global find_route
    if find_route:
        return
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dist[i] = dist[v] + 1
            findRing(route + [i], i, visited)
        if visited[i] and dist[v] >= dist[i] + 2:
            find_route = True
            # print(i, v, route, dist[v], dist[i], dist)
            for j in route[dist[i] : dist[v] + 1]:
                ring[j] = -1
            return route


# bfs
def bfs(start):
    q = deque()
    q.append([start, 0])

    visited = [False] * n

    while q:
        v, depth = q.popleft()
        if ring[v] == -1:
            return depth

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append([i, depth + 1])


# input
n = int(input().rstrip())
graph = [[] * n for _ in range(n)]
for _ in range(n):
    u, v = map(int, input().rstrip().split())
    u, v = u - 1, v - 1
    graph[u].append(v)
    graph[v].append(u)

# find Ring
dist = [-1] * n
dist[0] = 0

visited = [False] * n
ring = [0 for _ in range(n)]
findRing([0], 0, visited)
# print(ring)

# solve
for i in range(n):
    print(bfs(i), end=" ")
