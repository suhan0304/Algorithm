import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra() :
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    dist[0][0] = 0

    while q :
        d, x, y = heapq.heappop(q)

        if x == t-1 and y == t-1 :
            print(f'Problem {cnt}: {dist[x][y]}')
            break

        for di in range(4) :
            nx = x + dx[di]
            ny = y + dy[di]

            if 0 <= nx < t and 0 <= ny < t :
                nd = d + graph[nx][ny]
                
                if nd < dist[nx][ny] :
                    dist[nx][ny] = nd
                    heapq.heappush(q, (nd, nx, ny))

cnt = 1
while True :
    t = int(input())
    if t == 0 :
        break

    graph = [list(map(int, input().split())) for _ in range(t)]
    dist = [[INF for _ in range(t)] for _ in range(t)]

    dijkstra()
    cnt += 1