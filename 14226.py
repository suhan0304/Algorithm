import sys
from collections import deque
input = sys.stdin.readline

s = int(input())

dp = [1000 for _ in range(s+1)]
dp[s] = 0

for i in range(s-1, 0, -1) :
    dp[i] = min(dp[i], dp[i+1] + 1)
    if i*2 <= s :
        dp[i] = min(dp[i], dp[i*2] + 2)
        
print(dp)