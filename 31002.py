import sys
input = sys.stdin.readline

NUM = (10**9) + 7

N, K = map(int, input().rstrip().split())

if N == 3 :
    print(3)
    exit()

edges = [N*(N-1)//2]
neighborEdges = [(N-2)*2]

print(edges)
print(neighborEdges)