import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

def complete_graph(N):
    graph = [[] * N]