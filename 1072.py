import sys

input = sys.stdin.readline

x, y = map(int, input().split())

z = int(y / x * 100)
if x == y:
    print(-1)
else:
    # 1씩 했더니 시간초과 그럼 이분탐색 해보자
    l = y
    r = x
    z = int(l / r * 100)
    mid = 0
    while l <= r:
        mid = (l + r) // 2
        z2 = int(l / r * 100)
        print(l, mid, r, z, z2)
        if z + 1 == z2:
            break
        elif z + 1 < z2:
            r = mid - 1
        elif z + 1 > z2:
            l = mid + 1
    print(mid)
