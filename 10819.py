import sys

input = sys.stdin.readline

ans = 0


def dfs(b, cnt):
    global ans
    if cnt == n:
        s = 0
        for i in range(1, len(b)):
            s += abs(b[i - 1] - b[i])
        if s > ans:
            ans = s
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(b + [a[i]], cnt + 1)
            visited[i] = False


n = int(input())
a = list(map(int, input().split()))
visited = [False] * n
for i in range(n):
    visited[i] = True
    dfs([a[i]], 1)
    visited[i] = False
print(ans)
