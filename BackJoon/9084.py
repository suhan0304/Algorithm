import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())
    c = list(map(int, input().split()))
    m = int(input())
    dp = [[0] * (m+1) for _ in range(n+1)]

    dp[0][0] = 1
    for i in range(1, n+1) :
        dp[i][0] = 1
        for j in range(m+1) :
            dp[i][j] = dp[i-1][j]
            if j-c[i-1] >= 0 :
                dp[i][j] += dp[i][j-c[i-1]]
    print(dp[n][-1])

    