import sys
import heapq
input = sys.stdin.readline

def dijkstra(arr) :
    dist = [[sys.maxsize for _ in range(t)] for _ in range(t)]
    arr[0][0] = 0
    q = [(0, 0, 0)]
    while q :
        x, y = heapq.heappop()


while True :
    arr = []
    t = int(input())
    if t == 0 :
        break
    for _ in range(t) :
        arr.append(list(map(int, input().split())))
