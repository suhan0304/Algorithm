import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

pieces = []
for i in range(k) :
    x, y, d = map(int, input().split())
    pieces.append([x-1, y-1, d-1])

position = [[deque() for _ in range(n)] for _ in range(n) ]

for i in range(k) :
    position[pieces[i][0]][pieces[i][1]].append(i)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def check(x, y, nx, ny, t) :
    if len(position[x][y]) + len(position[nx][ny]) >= 4 :
        print(t)
        exit(0)

turn = 1
while turn <= 1000 :
    for i in range(k) :
        x = pieces[i][0]
        y = pieces[i][1]
        d = pieces[i][2]

        if position[x][y][0] != i :
            continue

        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n :
            if board[nx][ny] == 0 :
                check(x, y, nx, ny, turn)
                while len(position[x][y]) > 0 :
                    move_idx = position[x][y].popleft()
                    pieces[move_idx] = [nx, ny, pieces[move_idx][2]]
                    position[nx][ny].append(move_idx)
                pieces[i] = [nx, ny, d]
                continue
            elif board[nx][ny] == 1 :
                check(x, y, nx, ny, turn)
                while len(position[x][y]) > 0 :
                    move_idx = position[x][y].pop()
                    pieces[move_idx] = [nx, ny, pieces[move_idx][2]]
                    position[nx][ny].append(move_idx)
                pieces[i] = [nx, ny, d]
                continue
        
        d = d + 1 if d%2 == 0 else d - 1
        pieces[i][2] = d

        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n :
            if board[nx][ny] == 0 :
                check(x, y, nx, ny, turn)
                while len(position[x][y]) > 0 :
                    move_idx = position[x][y].popleft()
                    pieces[move_idx] = [nx, ny, pieces[move_idx][2]]
                    position[nx][ny].append(move_idx)
                pieces[i] = [nx, ny, d]
                continue
            elif board[nx][ny] == 1 :
                check(x, y, nx, ny, turn)
                while len(position[x][y]) > 0 :
                    move_idx = position[x][y].pop()
                    pieces[move_idx] = [nx, ny, pieces[move_idx][2]]
                    position[nx][ny].append(move_idx)
                pieces[i] = [nx, ny, d]
    turn += 1
print(-1)