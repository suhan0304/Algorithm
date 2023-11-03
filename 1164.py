import sys

n, l, w, h = map(int, sys.stdin.readline().split())

left = 0
right = max(l, w, h)


for _ in range(1000):
    mid = (left + right) / 2
    if (l // mid) * (w // mid) * (h // mid) >= n:
        left = mid
    else:
        right = mid


print("%.10f" % (right))
