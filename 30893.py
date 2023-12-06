import sys
sys.setrecursionlimit(10**9)

#input
input = sys.stdin.readline
N, S, E = map(int, input().rstrip().split())
S, E = S-1, E-1
graph = [[] for _ in range(N)]
for _ in range(N-1) :
    s, v = map(int, input().rstrip().split())
    s, v = s-1, v - 1
    graph[s].append(v)
    graph[v].append(s)

#dfs
def dfs(v, player, visited) :
    if v == E :
        return True
    
    for u in graph[v] :
        if not visited[u] :
            visited[u] = True
            if dfs(u, 2 if player == 1 else 1, visited) :
                visited[u] = False
            else :
                return

    return False

visited = [False for _ in range(N)]
visited[S] = True
dfs(S, 2, visited)