import sys

n = int(sys.stdin.readline())

ans = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, int(i ** (0.5)) + 1):
        ans[i] = min(ans[i - (j**2)] + 1, ans[i] + 1, ans[i])

print(ans[n])
