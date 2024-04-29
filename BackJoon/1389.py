import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
INF = 100000
graph = [[INF for _ in range(n)] for _ in range(n) ]

for _ in range(m) :
    a, b = map(int, input().rstrip().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for i in range(n) :
    graph[i][i] = 0

for i in range(n) :
    for j in range(n) :
        for k in range(n) :
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

min_ans = INF
ans = 0
for i in range(n-1, -1, -1):
    s = sum(graph[i])
    if min_ans >= s:
        min_ans = s
        ans = i
print(ans+1)