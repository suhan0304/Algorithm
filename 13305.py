import sys

input = sys.stdin.readline

n = int(input())

line = list(map(int, input().split()))
vertex = list(map(int, input().split()))[:-1]

i = 0
ans = 0
while i < n - 1:
    ans += vertex[i] * line[i]
    j = i
    while j + 1 < n - 1 and vertex[i] <= vertex[j + 1]:
        ans += vertex[i] * line[j + 1]
        j += 1
    i = j
    i += 1

print(ans)
