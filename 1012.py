import sys

sys.setrecursionlimit(10**5)


def dfs(y1, x1, ground, m, n):
    ground[y1][x1] = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(4):
        y2 = y1 + dy[i]
        x2 = x1 + dx[i]
        if y2 < 0 or m <= y2 or x2 < 0 or n <= x2:
            continue

        if ground[y2][x2] == 1:
            dfs(y2, x2, ground, m, n)


for _ in range(int(input())):
    ans = 0

    arr = []
    m, n, k = map(int, input().split())
    ground = [[0 for _ in range(n)] for __ in range(m)]
    for _ in range(k):
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
