import sys

input = sys.stdin.readline


def dfs(graph, i, j):
    global cnt
    graph[i][j] = "0"
    cnt += 1

    # 상 하 좌 후
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or n <= ni or nj < 0 or n <= nj:
            continue

        if graph[ni][nj] == "1":
            dfs(graph, ni, nj)


n = int(input())
graph = []
arr = []

for _ in range(n):
    graph.append(list(input().strip()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == "1":
            arr.append([i, j])

ans = []
for i, j in arr:
    if graph[i][j] == "1":
        cnt = 0
        dfs(graph, i, j)
        ans.append(cnt)

ans.sort()
print(len(ans))
for a in ans:
    print(a)
