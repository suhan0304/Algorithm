import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

def make_graph(N) :
    graph = [[] * N]
    for i in range(N) :
        graph[N] = 