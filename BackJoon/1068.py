import sys

input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    if not graph[v] and v != -1:
        leaf.append(v)
        return
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return


n = int(input())
nodes = list(map(int, input().split()))
erase_node = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(len(nodes)):
    if i != erase_node:
        graph[nodes[i]].append(i)


leaf = []
visited = [False] * (n + 1)
dfs(graph, -1, visited)
# print(leaf)

print(len(leaf))
