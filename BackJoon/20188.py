import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

graph = defaultdict(list)

n = int(input())
for _ in range(n-1) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [0] * (n+1)
ans = 0
def dfs(cur, parent) :
    global ans

    for child in graph[cur] :
        if child != parent :
            dfs(child, cur)
            dp[cur] += dp[child] + 1
            
    # 서브 트리와 서브 트리가 아닌 점을 골랐을 때, 해당 서브 트리의 root와 root의 parent를 연결하는 간선을 이용하는 횟수 = (서브트리 노드 개수 * 서브 트리 밖의 노드 개수)
    # (sub Tree 내부에서의 간선 이용 횟수는 아래에서 더해줄 예정
    a = (dp[cur]+1) * (n-(dp[cur]+1)) 

    # cur를 root로 하는 서브 트리에서 2개 고르는 경우 = 서브 트리 노드 개수에서 두 개 뽑는 경우 (Combination 공식 nC2)
    a += ((dp[cur]+1) * dp[cur])//2

    if cur != 1 :
        ans += a

dfs(1, 0)

print(ans)