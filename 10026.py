import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

ans = [0, 0]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y) :
    visited[x][y] = True
    color = arr[x][y]

    for d in range(4) :
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == color:
            dfs(nx,ny)

for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False:
            dfs(i,j)
            ans[0] += 1

for i in range(n):
    for j in range(n):
        if arr[i][j]=='R': arr[i][j]='G'

visited = [[False] * n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False:
            dfs(i,j)
            ans[1] += 1

print(ans[0], ans[1])