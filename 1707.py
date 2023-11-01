import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return


for ___ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for i in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
