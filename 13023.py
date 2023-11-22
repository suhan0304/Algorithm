import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# dfs algorithm
def dfs(graph, v, visited, depth):
    if depth == 5:
        print(1)
        exit()

    for i in graph[v]:
        if not visited[i]:
            visited[v] = True
            dfs(graph, i, visited, depth + 1)
            visited[v] = False
    return


# input
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# solution
for i in range(n):
    visited = [False] * n
    if not visited[i]:
        dfs(graph, i, visited, 1)

print(0)
