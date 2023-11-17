import sys

n = int(sys.stdin.readline())

ans = [[1, 1, 1]]

q = 9901

for i in range(1, n):
    ans.append(
        [
            sum(ans[i - 1]) % q,
            (ans[i - 1][0] + ans[i - 1][2]) % q,
            (ans[i - 1][0] + ans[i - 1][1]) % q,
        ]
    )

print(sum(ans[-1]) % q)
