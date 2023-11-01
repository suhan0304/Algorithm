import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(graph, v, group):
    visited[v] = group
    for i in graph[v]:
        if not visited[i]:
            flag = dfs(graph, i, -group)
            if not flag:
                return False
        elif visited[i] == visited[v]:
            return False
    return True


from collections import deque


def bfs(graph, v, group):
    queue = deque([v])
    visited[v] = group
    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -1 * visited[n]
            elif visited[i] == visited[n]:
                return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if not visited[i]:
            result = bfs(graph, i, 1)
            if not result:
                break

    print("YES" if result else "NO")
