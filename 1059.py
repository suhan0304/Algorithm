import sys

input = sys.stdin.readline

l = int(input())

S = list(map(int, input().split()))
S.sort()

n = int(input())

left = 0
right = len(l) - 1
for i in range(l - 1):
    if l[i] < n and n < l[i + 1]:
        left = l[i]
        right = l[i + 1]
        break

print(left, right)
