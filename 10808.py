import sys

input = sys.stdin.readline

s = input().strip()

a = [0] * 26

for c in s:
    a[ord(c) - ord("a")] += 1

print(*a)
