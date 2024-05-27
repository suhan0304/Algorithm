import sys
input = sys.stdin.readline

for __ in range(3) :
    n = int(input())
    coins = [list(map(int, input().split())) for _ in range(n)]
    coins.sort()
