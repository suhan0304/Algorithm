import sys

input = sys.stdin.readline

n = int(input())

sign = input().strip()
s = [['' for _ in range(n)] for _ in range(n)]
sign_index = 0
for i in range(n) :
    for j in range(i, n) :
        s[i][j] = sign[sign_index]
        sign_index += 1
#print(s)
    
def dfs(a, cnt) :
    if cnt == n :
        print(*a)
        return
    
    for i in range(-10, 10+1, 1) :
        dp[cnt][cnt] = i
        for j in range(0, cnt) :
            dp[j][cnt] = dp[j-1][cnt] + dp[cnt][cnt]
            if not (dp[j][cnt] == 0 and s[j][cnt] == '0' or 
                    dp[j][cnt] > 0 and s[j][cnt] == '+' or 
                    dp[j][cnt] < 0 and s[j][cnt] == '-'):
                return
        dfs(a + [i], cnt+1)

dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(-10, 10+1) :
    dp[0][0] = i
    dfs([i], 1)