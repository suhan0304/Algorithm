import sys

input = sys.stdin.readline

x, y = map(int, input().split())

z = int(y / x * 100)
if x == y:
    print(-1)
else:
    # 1씩 했더니 시간초과 그럼 이분탐색 해보자
    l = 1
    r = x - y
    mid = 0
    while 1:
        mid = (l + r) // 2
        z2 = int(y + mid / x + mid * 100)
        if z + 1 == z2:
            break
        elif z + 1 < z2:
            right = mid - 1
        elif z + 1 > z2:
            left = mid + 1
    print(mid)
