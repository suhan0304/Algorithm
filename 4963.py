import sys

input = sys.stdin.readline


def dfs(graph, i, j):
    graph[i][j] = "0"

    di = [-1, -1, -1, 1, 1, 1, 0, 0]
    dj = [-1, 0, 1, -1, 0, 1, -1, 1]

    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or m <= ni or nj < 0 or n <= nj:
            continue

        if graph[i][j] == "1":
            dfs(graph, ni, nj)


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

    ans = 0
    for i, j in arr:
        if graph[i][j] == "1":
            dfs(graph, i, j)
            ans += 1

    print(ans)
