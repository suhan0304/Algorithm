import sys

input = sys.stdin.readline

r, c = map(int,input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(r)]

di = [1,0,-1,0]
dj = [0,1,0,-1]

visited = [False]  * 26

print(visited)

max_ans = 0

def dfs(i, j, visited, depth) :
    global max_ans
    max_ans = max(depth,max_ans)

    for d in range(4) :
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < r and 0 <= nj < c and not visited[ord(graph[ni][nj])-ord['A']] :
            visited[ord(graph[ni][nj])] = True
            dfs(ni,nj,visited, depth + 1)
            visited[ord(graph[ni][nj])] = False

dfs(0, 0, visited, 0)