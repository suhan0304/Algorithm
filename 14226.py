import sys
from collections import deque
input = sys.stdin.readline

s = int(input())
visited = [[-1] * (s+1) for i in range(s+1)]
visited[1][0] = 0
q = deque()
q.append((1,0))
while q :
    x, c = q.popleft()
    if x == s :
        print(visited[x][c])
        break
    dx = [c, 0, -1]
    for i in range(3) :
        nx = x + dx[i]
        
        if nx < 0 or nx > s :
            continue
        
        if visited[nx][x] == -1 and i == 1 :
            visited[nx][x] = visited[x][c] + 1
            q.append((nx,x))
        
        if visited[nx][c] == -1 and i != 1 :
            visited[nx][c] = visited[x][c] + 1
            q.append((nx,c))