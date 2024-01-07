import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

def complete_graph(N):
    graph = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            graph[i][j] = 1
            graph[j][i] = 1

    return graph