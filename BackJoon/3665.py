import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())

    graph = [[] for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]
    rank = list(map(int, input().rstrip().split()))

    for i in range(n) :
        for j in range(i+1, n) :
            graph[rank[i]].append(rank[j])
            degree[rank[j]] += 1

    m = int(input())
    for _ in range(m) :
        a, b = map(int,input().rstrip().split())
