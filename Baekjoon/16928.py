import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [i for i in range(101)]

for _ in range(n + m) :
    u, v = map(int, input().rstrip().split())
    graph[u] = v


def bfs() :
    visited = [False for _ in range(101)]
    q = deque()
    q.append([graph[1], 0])

    visited[1] = True
    while q :
        i, depth = q.popleft()

        if i == 100 :
            print(depth)
            exit()

        for d in range(1,7) :
            ni = i + d

            if 0 <= ni < 101 and not visited[graph[ni]] :
                visited[graph[ni]] = True
                q.append([graph[ni], depth+1])
    
bfs()