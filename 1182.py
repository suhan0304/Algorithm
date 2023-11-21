import sys

input = sys.stdin.readline

n, s = map(int, input().split())

a = list(map(int, input().split()))

cnt = 0


def dfs(b, dsum):
    global cnt

    if dsum == s:
        cnt += 1
        return

    for i in range(n):
        if not visited[i] and b[-1] <= a[i]:
            visited[i] = True
            dfs(b + [a[i]], dsum + a[i])
            visited[i] = False


visited = [False] * n
for i in range(n):
    visited[i] = True
    dfs([a[i]], a[i])
    visited[i] = False

print(cnt)
