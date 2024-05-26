import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

ans = 0
for i in range(1, w-1) :
    l = max(blocks[:i])
    r = max(blocks[i+1:])
    