import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(n)]

INF = 1e9

dp = [[-INF] * (m) for _ in range(n)]

dp[0] = cost[0][:]
for j in range(1, m) :
    dp[0][j] = dp[0][j-1] + cost[0][j]

for i in range(1, n) :
    for j in range(m) :
        dp[i][j] = (dp[i-1][j] if i > 0 else 0) + cost[i][j]

    right = [-INF for _ in range(m)]
    left = [-INF for _ in range(m)]

    right[0], left[-1] = dp[i][0], dp[i][-1]
    for j in range(1, m) :
        right[j] = max(dp[i-1][j] + cost[i][j], right[j-1] + cost[i][j]) 
    for j in range(m-2, -1, -1) :
        left[j] = max(dp[i-1][j] + cost[i][j], left[j+1] + cost[i][j]) 
    for j in range(0, m) :
        dp[i][j] = max(dp[i][j], right[j], left[j])


print(dp[-1][-1])