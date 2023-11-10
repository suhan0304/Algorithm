import sys

input = sys.stdin.readline

n, m = map(int, input().split())


cnt = [0] * m
ramp = []
for _ in range(n):
    ramp.append(input().strip())
    for i in range(m):
        if ramp[-1][i] == "0":
            cnt[i] += 1

print(cnt)
