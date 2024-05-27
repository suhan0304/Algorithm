import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

if a + b - 1 > n :
    print(-1)
    exit(0)