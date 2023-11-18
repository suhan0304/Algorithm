import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def dfs(a, cnt):
    if cnt == m:
        print(*a)
        return

    for i in range(n):
        dfs(a + [i + 1], cnt + 1)


visited = [False] * n
for i in range(n):
    a = [i + 1]
    dfs(a, 1)
