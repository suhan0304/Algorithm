import sys

input = sys.stdin.readline

n = int(input())

standard = list(input().rstrip())
for _ in range(n-1) :
    compare = list(input().rstrip())
    for i in range(len(standard)) :
        if standard[i] != compare[i] :
            standard[i] = '?'

print("".join(standard))