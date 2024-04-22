def dfs(graph, v):  # 순환 함수 말고도 stack 형식을 이용해서 구현해낼 수 있다.
    graph[v][v] = -1  # 방문한 노드는 방문했다고 표시
    print(v, end=" ")
    for i in range(1, n + 1):
        # 간선이 있고, 해당 노드에 방문학 적이 없다면
        if graph[v][i] == 1 and graph[i][i] != -1:
            dfs(graph, i)  # 재귀를 사용해 dfs 구현
    return


def bfs(graph, v):
    queue = []  # bfs는 큐를 이용해서 쉽게 구현
    queue.append(v)
    graph[v][v] = -1  # 방문한 노드는 방문했다고 표시
    while queue:  # 원소가 하나라도 있을시 True, 원소가 하나도 없으면 False
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1, n + 1):
            # 간선이 있고, 해당 노드에 방문학 적이 없다면
            if graph[v][i] == 1 and graph[i][i] != -1:
                queue.append(i)
                graph[i][i] = -1  # 방문한 노드는 방문했다고 표시
    return


n, m, v = map(int, input().split())

graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1

dfs(graph, v)

for i in range(1, n + 1):
    graph[i][i] = 0

print()
bfs(graph, v)
