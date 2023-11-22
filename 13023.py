import sys

input = sys.stdin.readline


def dfs(graph, v, visited, cnt):
    if cnt == n:
        global ans

    print(v)

    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, cnt + 1)
    return

#input
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
visited = [False] * n

for i in range(0, n):
    if not visited[i]:
        dfs(graph, i, visited, 1)

print(ans)
