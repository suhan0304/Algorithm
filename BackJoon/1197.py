import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

start_v = 1
for i in range(2, v + 1):
    if len(graph[i]) < len(graph[start_v]):
        start_v = i

h = [(0, start_v)]
visited = [-1] * (v + 1)

while h:
    current_w, current_v = heapq.heappop(h)
    if visited[current_v] == -1:
        visited[current_v] = current_w

        for next_v, next_w in graph[current_v]:
            heapq.heappush(h, (next_w, next_v))

print(sum(visited[1:]))