import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

ans = [0] * (n)
ans[0] = 1

for i in range(1, n):
    max_len = 1
    for j in range(i, -1, -1):
        if a[j] > a[i]:
            if ans[j] + 1 > max_len:
                max_len = ans[j] + 1
    ans[i] = max_len

print(max(ans))
