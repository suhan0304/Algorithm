import sys
input = sys.stdin.readline

NUM = (10**9) + 7

N, K = map(int, input().rstrip().split())

def solution(N, K):
    for i in range(K) :
        N = ((N-1) * 2) % NUM
    
    print(N)

solution(N, K)