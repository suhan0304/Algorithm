import sys

input = sys.stdin.readline

n, l = map(int, input().split())

ans = []
while 1:
    x = (n - (l * (l - 1) / 2)) / l
    if n == 1 and l == 2:
        ans.append(str(0))
        ans.append(str(1))
        break
    if l > n:
        break
    if x < 0:
        break
    if l > 100:
        break

    if x == 0 or x == int(x):
        for i in range(l):
            ans.append(str(int(x + i)))
        break
    else:
        l += 1

if len(ans) > 0:
    print(" ".join(ans))
else:
    print(-1)
