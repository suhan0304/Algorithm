import sys

input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x

if z > 98:
    print(-1)
else:
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if z < ((y + mid) * 100 // (x + mid)):
            right = mid - 1
        else:
            left = mid + 1
    print(left)
