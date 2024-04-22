import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

ans = [a[0]]

for i in range(1, n):
    ans.append(max(a[i] + ans[i - 1], a[i]))

print(max(ans))
