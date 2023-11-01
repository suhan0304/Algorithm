import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(graph, v, visited, b, bit):
    if bit[0] == -1:
        return
    else:
        visited[v] = True
        # print(bit)
        bit[v] = b
        for i in graph[v]:
            if visited[i] and bit[i] == bit[v]:
                bit[0] = -1
                return
            elif not visited[i]:
                dfs(graph, i, visited, b * -1, bit)
        return


ans = []
T = int(input())
for ___ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    cnt = 0
    visited = [False] * (V + 1)
    bit = [0] * (V + 1)
    for i in range(1, V + 1):
        if not visited[i]:
            flag = 0
            dfs(graph, i, visited, 1, bit)
    if bit[0] != -1:
        print("YES")
    else:
        print("NO")
