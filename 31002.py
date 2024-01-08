import sys
input = sys.stdin.readline

NUM = (10**9) + 7

N, K = map(int, input().rstrip().split())

if N == 3 :
    print(3)
    exit()

if K == 0 :
    print(N) 
    exit()

edges = N*(N-1)//2 % NUM
neighborEdges = (N-2)*2

for _ in range(K-1) :
    edges = ((neighborEdges * edges) // 2) % NUM
    neighborEdges = (neighborEdges-1) * 2

print(edges % NUM)