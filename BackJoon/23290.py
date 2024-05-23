import sys
from collections import deque
input = sys.stdin.readline

def check_graph(graph) :
    for g in graph :

    print()

def move_fish(fish, smell, graph) :
    dx = [0,-1,-1,-1,0,1,1,1]
    dy = [-1,-1,0,1,1,1,0,-1]

    for i in range(len(fish)) :
        x, y, d = fish[i]
        nx, ny = x+dx[d], y+dy[d]
        # wall, shark, fish smell = can't move
        if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny] < 100 and smell[nx][ny] == 0:
                    fish[i] = [nx, ny, d]
                    graph[x][y] -= 1
                    graph[nx][ny] += 1
        else :
            nd = d
            while True :
                nd -= 1
                nx, ny = x+dx[nd], y+dy[nd]
                if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny] < 100 and smell[nx][ny] == 0:
                    fish[i] = [nx, ny, (nd+8)%8]
                    graph[x][y] -= 1
                    graph[nx][ny] += 1
                    break
                if nd == d :
                    fish[i] = [x, y, nd]
                    break

def bfs(shark, graph) :
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    max_sum = 0
    max_visited, max_position = [], []
    q = deque()
    q.append([shark[0], shark[1], 0, 0, [(shark[0], shark[1])]])
    while q :
        x, y, current_sum, depth, visited = q.popleft()
        if depth == 3 :
            if current_sum > max_sum :
                max_sum = current_sum
                max_visited = visited
                max_position = [x, y]
        else :
            for d in range(4) :
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < 4 and 0 <= ny < 4 :
                    if (nx, ny) not in visited :
                        new_sum = current_sum + graph[nx][ny] if graph[nx][ny] > 0 else current_sum
                        new_visited = visited + [(nx, ny)]
                        q.append([nx, ny, new_sum, depth + 1, new_visited])
    return max_visited, max_position

def move_shark(fish, smell, shark, graph) :
    path, pos = bfs(shark, graph)
    for x, y in path :
        if 0 < graph[x][y] < 100 :
            graph[x][y] = 0
            smell[x][y] = -3
    i = 0
    while i < len(fish):
        x, y, d = fish[i]
        if (x, y) in path:
            fish.pop(i)
        else:
            i += 1

    graph[shark[0]][shark[1]] = 0
    graph[pos[0]][pos[1]] = 100
    shark[0], shark[1] = pos[0], pos[1]

def smell_decrease(graph) :
    for i in range(4) :
        for j in range(4) :
            if smell[i][j] < 0 :
                smell[i][j] += 1

def copy_fish(fish, remember_fish, graph) :
    for x, y, d in remember_fish :
        fish.append([x, y, d])
        graph[x][y] += 1

def practice(fish, shark, graph) :
    check_graph(graph)
    remember_fish = [x for x in fish]       #step1
    check_graph(graph)
    move_fish(fish, smell, graph)                  #step2
    check_graph(graph)
    move_shark(fish, smell, shark, graph)                #step3
    check_graph(graph)
    smell_decrease(graph)                   #step4
    check_graph(graph)
    copy_fish(fish, remember_fish, graph)   #step5

    check_graph(graph)

fish = []
m, s = map(int, input().split())
graph = [[0 for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]
for _ in range(m) :
    fx, fy, d = map(int, input().split())
    graph[fx-1][fy-1]+=1 #fish
    fish.append([fx-1,fy-1, d-1])
sx, sy = map(int, input().split())
graph[sx-1][sy-1] = 100 #shark
shark = [sx-1, sy-1]

for _ in range(s) :
    practice(fish, shark, graph)