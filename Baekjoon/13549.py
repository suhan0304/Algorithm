import sys
from collections import deque
input = sys.stdin.readline

M = 10 ** 5

n, k = map(int, input().rstrip().split())

if n == k :
    print(0)
    exit()

visited = [-1] * (M+1)
visited[n] = 0

q = deque()

q.append(n)

while q :
    x = q.popleft()

    if x == k :
        print(visited[x])
        break

    dx = [x, 1, -1]
    
    for i in range(3) :
        nx = x + dx[i]
        if nx < 0 or nx > M : continue
        
        if visited[nx] == -1 :
            if i == 0 :
                visited[nx] = visited[x]
                q.append(nx)
            else :
                visited[nx] = visited[x] + 1
                q.append(nx)
        
        else :
            if i == 0 :
                visited[nx] = min(visited[nx], visited[x])
            else :
                visited[nx] = min(visited[nx], visited[x]+1)