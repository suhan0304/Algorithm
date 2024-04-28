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
            dfs(b + [a[i]], cnt + 1)


visited = [False] * n
for i in range(n):
    b = [a[i]]
    dfs(b, 1)

ans = sorted(list(ans))

for a in ans:
    print(*a)
