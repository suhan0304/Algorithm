import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [i for i in range(101)]
visited = [0 for _ in range(101)]

for _ in range(n + m) :
    u, v = map(int, input().rstrip().split())
    graph[u] = v

