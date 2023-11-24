import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dist[i] = dist[v] + 1
            dfs(graph, i, visited)
        if visited[i] and dist[v] >= dist[i] + 2:
            print("Yes")


n = int(input().rstrip())
graph = [[0] * n for _ in range(n)]
for _ in range(n):
    u, v = map(int, input().rstrip().split())
    u, v = u - 1, v - 1
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * n
dist[0] = 1
visited = [False] * n
dfs(graph, 0, visited)
print(dist)
