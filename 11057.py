import sys

n = int(sys.stdin.readline())

ans = [[0 for _ in range(10)] for _ in range(n)]
ans[0] = [1 for _ in range(10)]

for i in range(1, n):
    for j in range(0, 10):
        s = 0
        for k in range(0, j + 1):
            s += ans[i - 1][k]
        ans[i][j] = s % 10007

print(sum(ans[-1]) % 10007)
