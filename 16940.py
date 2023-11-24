import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    visited = [False] * (n + 1)

    arr = [[] for _ in range(n + 1)]

    q = deque()
    q.append([1, 1])
    visited[1] = True

    while q:
        v, depth = q.popleft()
        arr[depth].append(v)

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append([i, depth + 1])
    return arr


n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

ans = list(map(int, input().rstrip().split()))

arr = bfs()

print(arr)
