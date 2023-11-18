import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def dfs(a, cnt):
    if cnt == m:
        print(*a)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(a + [i + 1], cnt + 1)
            visited[i] = False


visited = [False] * n
for i in range(n):
    a = [i + 1]
    visited[i] = True
    dfs(a, 1)
    visited[i] = False
