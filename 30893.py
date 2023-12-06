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
def dfs(v,  visited) :
    if v == E :
        return True
    
    #아무래도 접근 방식이 잘못된듯
    #이게 결국 후공이 원할 때 게임을 끝내버리면 나는 절대 못이기는 게임이 되어버림
    
    #ex) 내가 후공인데 옆길로 빠질 수 있으면? 무조건 후공 승리가 되어버림
    #그러니깐 그걸 따지는 방법을 생각해봐야할듯 -> 선공이 이기는 경우가 굉장히 희박

    return False

visited = [False for _ in range(N)]
visited[S] = True
dfs(S, visited)