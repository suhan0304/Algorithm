import sys

input = sys.stdin.readline

N, S, E = map(int, input().rstrip().split())

graph = [[] for _ in range(N)]

for _ in range(N) :
    s, v = map(int, input().rstrip().split())