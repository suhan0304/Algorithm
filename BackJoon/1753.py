import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
k = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e) :
    a, b, c = map(int,input().rstrip().split())
    graph[a].append((b, c))

def dijkstra(graph, start) :
    dist = [float('inf') for _ in range(v+1)]
    dist[start] = 0

    queue = []
    heapq.heappush(queue, [dist[start], start])

    while queue :
        current_d, current_v = heapq.heappop(queue)

        if dist[current_v] < current_d :
            continue

        for next_v, next_d in graph[current_v] :
            distance = next_d + current_d
            if distance < dist[next_v] :
                dist[next_v] = distance
                heapq.heappush(queue, [distance, next_v])

    return dist

ans = dijkstra(graph, k)[1:]

for a in ans :
    if a == float('inf') :
        print('INF')
    else :
        print(a)