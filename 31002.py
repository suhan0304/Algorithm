import sys
input = sys.stdin.readline

NUM = (10**9) + 7

N, K = map(int, input().rstrip().split())

if N == 3 :
    print(3)
    exit()
edges = N*(N-1)//2
neighborEdges = (N-2)*2

for _ in range(K-1) :
    edges = ((neighborEdges * edges) // 2) % NUM
    #print(_, edges)
    neighborEdges = (neighborEdges-1) * 2

print(edges % NUM)