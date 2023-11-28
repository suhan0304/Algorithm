import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# dfs
def dfs(i, j) :
    if i == m-1 and j== n-1 :
        return 1
    
    if dp[i][j] != -1 :
        return dp[i][j]
        
    cnt = 0
    
    for d in range(4) :
        ni = i + di[d]
        nj = j + dj[d]
        
        if 0 <= ni < m and 0 <= nj < n and graph[ni][nj] < graph[i][j] :
            cnt += dfs(ni, nj)
    
    dp[i][j] = cnt
    return dp[i][j]
    

# input
m, n = map(int, input().rstrip().split())
graph = [list(map(int,input().rstrip().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
print(dfs(0, 0))