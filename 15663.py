import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

ans = set()


def dfs(b, cnt):
    if cnt == m:
        ans.add(tuple(b))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(b + [a[i]], cnt + 1)
            visited[i] = False


visited = [False] * n
for i in range(n):
    b = [a[i]]
    visited[i] = True
    dfs(b, 1)
    visited[i] = False

ans = sorted(list(ans))

for a in ans:
    print(*a)
