import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = [[a[0], a[0]]]
for i in range(1, n):
    ans.append(
        [max(ans[i - 1][0] + a[i], a[i]), max(ans[i - 1][0], ans[i - 1][1] + a[i])]
    )

max_ans = a[0]
for i in range(n):
    max_ans = max(max_ans, max(ans[i][0], ans[i][1]))
print(max_ans)
