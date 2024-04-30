import sys
input = sys.stdin.readline

n = int(input())
lines = [input().rstrip() for _ in range(n)]
lines = sorted(list(set(lines)))
lines.sort(key=len)
for i in range(len(lines)) :
    print(lines[i])