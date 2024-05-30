import sys
from collections import defaultdict
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(cur, parent) :
    global val

    for child, weight in graph[cur] :
        if child != parent:
            dfs(child, cur, min_val)
            dp[cur] += dp[child] + 1
            val += (dp[child]+1) * weight

while True :
    graph = defaultdict(list)

    n = (int(input()))
    if n == 0 : break

    for _ in range(n-1) :
        v, u, w = map(int, input().split())
        graph[v].append((u, w))
        graph[u].append((v, w))

    min_val = 1e9
    for i in range(n) :
        val = 0
        dp = [0] * (n+1)
        dfs(i, -1, min_val)
        if val < min_val :
            min_val = val
    print(min_val)