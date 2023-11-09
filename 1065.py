import sys

x = int(sys.stdin.readline())


def hansu(x):
    if len(x) <= 99:
        return True
    else:
        if (x // 100 - (x // 10) % 10) == ((x // 10) % 10 - x % 10):
            return True
        else:
            return False


ans = 0
for i in range(1, x + 1):
    if hansu(i):
        print(i)
        ans += 1
print(ans)
