import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [[a[0], a[0]]]
for i in range(1, n):
    dp.append([max(dp[i - 1][0] + a[i], a[i]), max(dp[i - 1][0], dp[i - 1][1] + a[i])])

ans = a[0]
for i in range(n):
    ans = max(ans, max(dp[i][0], dp[i][1]))
print(ans)
