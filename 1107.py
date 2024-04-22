import sys
import math

input = sys.stdin.readline


def check(n):
    if n == 0 and n in button:
        return False
    while n > 0:
        if n % 10 in button:
            return False
        else:
            n //= 10
    return True


n = int(input())
m = int(input())
button = []
if m != 0:
    button = list(map(int, input().split()))

ans = abs(n - 100)
for i in range(0, 2 * n if n > 100 else 100):
    if check(i):
        k = 1 if i < 10 else int(math.log10(i) + 1)
        cnt = abs(n - i) + k
        ans = min(ans, cnt)
print(ans)
