import sys

input = sys.stdin.readline

n = int(input())

ans = [0, 1, 1]
for i in range(3, n + 1):
    ans.append(ans[i - 2] + ans[i - 1])
print(ans[n])
