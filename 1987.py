import sys

input = sys.stdin.readline

r, c = map(int,input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(r)]

di = [1,0,-1,0]
dj = [0,1,0,-1]

visited = [False * 26]

print(visited)

def dfs(i, j, visited) :
    for d in range(4) :
        ni = i + di[d]
        nj =