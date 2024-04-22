import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    visited = [-1 for _ in range(n + 1)]
    depth = [set() for _ in range(n + 1)]

    q.append(1)
    visited[1] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                depth[v].add(i)
                q.append(i)
    return depth


n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

test = list(map(int, input().rstrip().split()))

depth = bfs()
idx = 1
for i in test:
    if idx == n:
        break
    depth_length = len(depth[i])
    test_depth = set(test[idx : idx + depth_length])
    check_depth = depth[i]
    if test_depth != check_depth:
        print(0)
        exit()
    idx += depth_length
print(1)
