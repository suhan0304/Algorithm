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
