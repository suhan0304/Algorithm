import sys

input = sys.stdin.readline

n = int(input())

ans = []

for _ in range(n):
    ans.append(list(map(int, input().split())))

for i in range(1, n):
    ans[i][0] = min(ans[i][0] + ans[i - 1][1], ans[i][0] + ans[i - 1][2])
    ans[i][1] = min(ans[i][1] + ans[i - 1][0], ans[i][1] + ans[i - 1][2])
    ans[i][2] = min(ans[i][2] + ans[i - 1][0], ans[i][2] + ans[i - 1][1])

print(min(ans[-1]))
