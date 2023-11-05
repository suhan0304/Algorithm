import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, v, visited):
    cnt = 0
    queue = deque([v])
    visited[v] = True
    while queue and cnt < 2:
        v = queue.popleft()
        for i in graph[v]:
            # 간선이 있고, 해당 노드에 방문학 적이 없다면
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        cnt += 1
    return


n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    s = input()[:-1]
    for j in range(i + 1, len(s)):
        if s[j] == "Y":
            graph[i].append(j)
            graph[j].append(i)

ans = 0
for i in range(n):
    # bfs 방식으로 그냥 깊이가 2일때까지 방문한 노드의 수
    # -> 2-친구의 수
    visited = [False] * n
    bfs(graph, i, visited)
    if ans < visited.count(True) - 1:
        ans = visited.count(True) - 1
print(ans)
