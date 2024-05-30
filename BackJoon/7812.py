import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline


while True :
    n = (int(input()))
    if n == 0 : break

    graph = [[] for _ in range(n)]

    for _ in range(n-1) :
        v, u, w = map(int, input().split())
        graph[v].append((u, w))
        graph[u].append((v, w))

    for i in range(n) :
        val = 0
        dp = [0] * (n+1)