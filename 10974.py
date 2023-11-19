import sys

input = sys.stdin.readline


def dfs(a, cnt):
    if cnt == n:
        print(*a)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(a + [i + 1], cnt + 1)
            visited[i] = False


n = int(input())
visited = [False] * n
for i in range(n):
    visited[i] = True
    dfs([i + 1], 1)
    visited[i] = False
