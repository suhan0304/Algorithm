import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v)]
for i in range(v) :
    arr = list(map(int, input().rstrip().split()))
    s_v = arr[0]-1
    idx = 1
    while arr[idx] != -1 :
        e_v, cost = arr[idx]-1, arr[idx+1]
        graph[s_v].append((e_v,cost))
        idx+=2

def dfs(v, d) :
    for nv,nd in graph[v] :
        if visited[nv] == -1 :
            visited[nv] = d + nd
            dfs(nv, d+nd)
    return

visited = [-1]*v
visited[0] = 0
dfs(0, 0)

end_point = [0, 0]
for i in range(v) :
    if visited[i] > end_point[1] :
        end_point[0] = i
        end_point[1] = visited[i]

for i in range(v) : visited[i] = -1

visited = [-1]*v
visited[end_point[0]] = 0
dfs(end_point[0], 0)

print(max(visited))