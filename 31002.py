import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

def solution(N, K):
    graph = [[] * N]

    print(graph)

solution(N, K)