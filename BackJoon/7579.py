import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [[0] * (sum(cost)+1) for _ in range(n+1)]


for i in range(1, n+1) :
    for j in range(0, sum(cost)+1) :
        if j >= cost[i-1] :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + memory[i-1])
        else :
            dp[i][j] = dp[i-1][j]

for i, me in enumerate(dp[n]) :
    if me >= m :
        print(i)
        break