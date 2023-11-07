import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * 201 for i in range(201)]

# k=1, 2일 때는 바로 대입
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1

for i in range(2, 201):
    # n = 1일때는 k로 나눌 때 1의 위치만 k개로 바뀌기 때문에 바로 계산 가능
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000

print(dp[k][n])
