import sys

input = sys.stdin.readline

n = int(input())

ans = []

for _ in range(n):
    ans.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            ans[i][j] += ans[i - 1][j]
        elif j == i:
            ans[i][j] += ans[i - 1][j - 1]
        else:
            ans[i][j] = ans[i][j] + max(ans[i - 1][j - 1], ans[i - 1][j])

print(max(ans[-1]))
