import sys

input = sys.stdin.readline

n = int(input())
charge = []
for _ in range(n):
    charge.append(list(map(int, input().split())))

ans = 10**7


def dfs(now, dsum, cnt, start):
    global ans
    if cnt == n:
        if charge[now][start] != 0:
            dsum += charge[now][start]
            if dsum < ans:
                ans = dsum
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            if charge[now][i] != 0:
                dfs(i, dsum + charge[now][i], cnt + 1, start)
            visited[i] = False


visited = [False] * n
for i in range(n):
    visited[i] = True
    dfs(i, 0, 1, i)
    visited[i] = False

print(ans)
