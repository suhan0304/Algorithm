import sys

input = sys.stdin.readline

n = int(input())

sign = input().strip()

def check_sign(a) :
    sign_index = 0
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(i, n) :
            if i == j :
                dp[i][j] = a[i]
            else :
                dp[i][j] = dp[i][j-1] + a[j]
            if not(dp[i][j] < 0  and sign[sign_index] == '-' or
                   dp[i][j] == 0 and sign[sign_index] == '0' or 
                   dp[i][j] > 0  and sign[sign_index] == '+') :
                return False
            sign_index += 1
    else :
        return True
    
    
def dfs(a, cnt) :
    if cnt == n :
        if check_sign(a) :
            print(*a)
            exit()
        return
    
    for i in range(-10, 10+1, 1) :
        dfs(a + [i], cnt+1)

for i in range(-10, 10+1) :
    dfs([i], 1)