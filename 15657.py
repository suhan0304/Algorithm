import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))


def dfs(b, cnt):
    if cnt == m:
        print(*b)
        return

    for i in range(n):
        if a[i] >= b[-1]:
            dfs(b + [a[i]], cnt + 1)


visited = [False] * n
for i in range(n):
    b = [a[i]]
    dfs(b, 1)
