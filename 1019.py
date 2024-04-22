import sys

input = sys.stdin.readline

n = input().strip()
ans = [0] * 10
k = len(n)

for x in n:
    k -= 1
    for i in range(int(x)):
        ans[i] += 10**k
        for j in range(10):
            if k >= 1:
                ans[j] += (10 ** (k - 1)) * k
    ans[0] -= 10**k
    if k:
        ans[int(x)] += int("".join(n[-k:])) + 1
    else:
        ans[int(x)] += 1

print(*ans)
