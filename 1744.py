import sys

input = sys.stdin.readline

N = int(input().rstrip())

a = []
for _ in range(N) :
    a.append(input().rstrip())

tied = [0 for _ in range(N)]

