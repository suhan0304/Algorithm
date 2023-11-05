import sys

input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    print(v, end=" ")
    return


n = int(input())
nodes = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i in range(len(nodes)):
    graph[i].append(nodes[i])
    graph[nodes[i]].append(i)

cnt = 0
visited = [False] * (n + 1)
dfs(graph, -1, visited)
print(cnt)
