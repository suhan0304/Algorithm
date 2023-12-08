import sys

input = sys.stdin.readline

x, y, w, h = map(int,input().rstrip().split())

print(min(x, abs(x-w), y, abs(y-h)))

