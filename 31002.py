import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
dp = [-1] * (10**9 + 7)

def solution(N, K):
    for i in range(K) :
        N = (N-1) * 2

    print(graph)

solution(N, K)