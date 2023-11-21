import sys

input = sys.stdin.readline

n, s = map(int, input().split())

a = list(map(int, input().split()))

cnt = 0


def dfs(b, idx):
    global cnt

    if b and sum(b) == s:
        cnt += 1

    for i in range(idx, n):
        b.append(a[i])
        dfs(b, i + 1)
        b.pop()


dfs([], 0)
print(cnt)
