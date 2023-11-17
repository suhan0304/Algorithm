import sys

n = int(sys.stdin.readline())

ans = [1, 0, 3, 0]

for i in range(4, 31):
    if i % 2 == 1:
        ans.append(0)
    else:
        ans.append(ans[i - 2] * 3 + sum(ans[: i - 3]) * 2)

print(ans[n])
