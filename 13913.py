import sys
from collections import deque

input = sys.stdin.readline

M = 10 ** 5

n, k = map(int, input().rstrip().split())

if n == k :
    print(0)
    print(n)
    exit()
if n > k :
    print(n-k)
    print(*list(range(n,k-1,-1)))
    exit()
    

visited = [False] * (M+1)
q = deque()

q.append([n, 0, [n]])

while q :
    m, depth, path = q.popleft()
    
    for i in [m-1, m+1, 2*m] :
        if i < 0 or M < i : continue
        if visited[i] : continue
        if i == k :
            print(depth+1)
            print(*(path+[i]))
            exit()
        visited[i] = True
        q.append([i, depth+1, path + [i]])