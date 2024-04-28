import sys

input = sys.stdin.readline

n = int(input())

wine = []
for _ in range(n):
    wine.append(int(input()))

ans = [[0, 0, 0] for _ in range(n)]
ans[0] = [0, wine[0], 0]
for i in range(1, n):
    ans[i][0] = max(ans[i - 1])
    ans[i][1] = ans[i - 1][0] + wine[i]
    ans[i][2] = ans[i - 1][1] + wine[i]

print(max(ans[-1]))
