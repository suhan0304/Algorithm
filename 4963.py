import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    graph = []

    for _ in range(m):
        graph.append(input().strip().split())

    arr = []
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                arr.append([i, j])

    for i, j in arr:
        if graph[i][j] == "1":
            dfs
