import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ans = []
    m = int(input())

    ans.append(list(map(int, input().split())))
    ans.append(list(map(int, input().split())))
    ans.append([0 for _ in range(m)])

    for i in range(1, m):
        ans[0][i] = max(ans[0][i] + ans[1][i - 1], ans[0][i] + ans[2][i - 1])
        ans[1][i] = max(ans[1][i] + ans[0][i - 1], ans[1][i] + ans[2][i - 1])
        ans[2][i] = max(ans[0][i - 1], ans[1][i - 1], ans[2][i - 1])

    print(max(ans[0][-1], ans[1][-1], ans[2][-1]))
