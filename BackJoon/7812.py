import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs1(cur) :
    visited[cur] = True
    for v, w in graph[cur] :
        if visited[v] :
            continue
        dfs1(v)
        cnt[cur] += cnt[v]
        dp[cur] += w * cnt[v] + dp[v]

def dfs2(cur) :
    visited[cur] = True
    for v, w in graph[cur] :
        if visited[v] :
            continue
        dp[v] = dp[cur] - cnt[v] * w + (n - cnt[v]) * w
        dfs2(v)

while True :
    n = (int(input()))
    if n == 0 : break

    graph = [[] for _ in range(n)]

    for _ in range(n-1) :
        v, u, w = map(int, input().split())
        graph[v].append((u, w))
        graph[u].append((v, w))

    val = 0
    cnt = [1] * n
    dp = [0] * n
    visited = [False] * n
    dfs1(0)

    visited = [False] * n
    dfs2(0)

    print(min(dp))