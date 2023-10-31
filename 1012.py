import sys

sys.setrecursionlimit(10**5)


def dfs(y, x, ground, m, n):
    ground[y][x] = 0
    if 0 <= y - 1 and ground[y - 1][x] == 1:
        dfs(y - 1, x, ground, m, n)
    elif y + 1 < m and ground[y + 1][x] == 1:
        dfs(y + 1, x, ground, m, n)
    elif 0 <= x - 1 and ground[y][x - 1] == 1:
        dfs(y, x - 1, ground, m, n)
    elif x + 1 < n and ground[y][x + 1] == 1:
        dfs(y, x + 1, ground, m, n)
    return


for _ in range(int(input())):
    ans = 0
    arr = []
    m, n, k = map(int, input().split())
    ground = [[0 for _ in range(n)] for __ in range(m)]
    for j in range(k):
        x, y = map(int, input().split())
        ground[x][y] = 1
        arr.append([x, y])

    for i in range(k):
        arr[i].reverse()

    for x, y in arr:
        if ground[y][x] == 1:
            dfs(y, x, ground, m, n)
            ans += 1

    print(ans)
