import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().strip().split()))

ans = a.copy()

max_ans = 0
for i in range(1, n):
    max_ans = 0
    ans[i] = a[i]
    for j in range(i):
        if a[j] < a[i]:
            ans[i] = max(ans[i], ans[j] + a[i])

print(max(ans))
