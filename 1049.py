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

ans = +(n // 6) * min(min_package, min_each * 6) + min(min_package, min_each * (n % 6))

print(ans)
