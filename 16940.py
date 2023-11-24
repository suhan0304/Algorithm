import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    visited = [False] * (n + 1)

    arr = []
    cnt = [0 for _ in range(n)]

    q = deque()
    q.append([1, 1])
    visited[1] = True

    while q:
        v, depth = q.popleft()
        cnt[depth] += 1
        arr.append([v, depth])

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append([i, depth + 1])
    return arr, cnt


n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

ans = list(map(int, input().rstrip().split()))

arr, cnt = bfs()

print(arr)
print(cnt)
