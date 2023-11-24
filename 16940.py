import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    visited = [False] * (n + 1)

    arr = []

    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        v = q.popleft()
        arr.append(v)

        for i in graph[v]:
            if not visited[i] and i == ans[len(arr)]:
                visited[i] = True
                q.append(i)
    print(arr)


n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

ans = list(map(int, input().rstrip().split()))

bfs()

if 