import sys

input = sys.stdin.readline

n, l = map(int, input().split())

ans = -1
while 1:
    if (n - int(l * (l - 1) / 2)) % l == 0:
        ans = int((n - int(l * (l - 1) / 2)) / l)
        break
    elif (n - int(l * (l - 1) / 2)) < 0:
        break
    else:
        l += 1

if ans >= 0:
    for i in range(l):
        print(ans + i, end=" ")
else:
    print(ans)
