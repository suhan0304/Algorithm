from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs() :
    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()
        
        if cnt >= 10 :
            return -1
        
        for d in range(4) :
            nx1 = x1 + dx[d]
            ny1 = y1 + dy[d]
            nx2 = x2 + dx[d]
            ny2 = y2 + dy[d]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < 2 and 0 <= ny2 < m :
                if board[nx1][ny1] == "#" :
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#" :
                    nx2, ny2 = x2, y2
                coin.append((nx1,ny1,nx2,ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m :
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m :
                return cnt + 1
            else :
                continue
    return -1