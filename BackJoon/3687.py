import sys
input = sys.stdin.readline

dp = ['','',1, 7, 4, 2, 6, 8] + [float('inf') for _ in range(100)]
for i in range(8, 101) :
    for j in range(2, i-1) :
        dp[i] = min(dp[i], int(str(dp[i-j])+(str(dp[j]) if j != 6 else '0')))

def max_num(n) :
    return ('7' + '1' * (n//2-1)) if n%2 else '1' * (n//2)

t = int(input())
for _ in range(t) :
    n = int(input())
    print(dp[n], max_num(n))

