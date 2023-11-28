import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
# input
m, n = map(int, input().rstrip().split())
graph = [list(map(int,input().rstrip().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dp[0][0] = 1

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

ans = 0

# dfs
def dfs(i, j) :
    if i == m-1 and j== n-1 :
        return 1
    
    if dp[i][j] != -1 :
        return dp[i][j]
        
    dp[i][j] = 0
    
    for d in range(4) :
        ni = i + di[d]
        nj = j + dj[d]
        
        if 0 <= ni < m and 0 <= nj < n and graph[ni][nj] < graph[i][j] :
            dp[i][j] += dfs(ni,nj)
    
    return dp[i][j]
    

print(dfs(0, 0))
for d in dp :
    print(d)