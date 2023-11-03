import sys

input = sys.stdin.readline

n, m = map(int, input().split())
min_package = 1000
min_each = 1000
for _ in range(m):
    package, each = map(int, input().split())
    if package < min_package:
        min_package = package
    if each < min_each:
        min_each = each

ans = 0

ans = ans + (n // 6) * min(min_package, min_each * 6)
n %= 6
ans = ans + min(min_package, min_each * n)

print(ans)
