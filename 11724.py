def dfs(graph, v):
    visited[v] = True
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(graph, i)
    return


n, m = map(int, input().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1

cnt = 0
visited = [False for _ in range(n + 1)]
for i in range(1, n + 1):
    if visited[i] == False:
        dfs(graph, i)
        cnt += 1

print(cnt)
