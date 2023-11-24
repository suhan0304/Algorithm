import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(graph, v, visited, d):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dist[v][i] = d
            dfs(graph, i, visited, d + 1)


n = int(input().rstrip())
graph = [[] for _ in range(n)]
for _ in range(n):
    u, v = map(int, input().rstrip().split())
    u, v = u - 1, v - 1
    graph[u].append(v)
    graph[v].append(u)

dist = [[0] * n for _ in range(n)]
visited = [False] * n
dfs(graph, 1, visited, 1)

for d in dist:
    print(d)
