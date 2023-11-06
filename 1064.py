import sys

input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())

import math


def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


def check(x1, y1, x2, y2, x3, y3):
    if x1 == x2 and x2 == x3:
        return False
    elif y1 == y2 and y2 == y3:
        return False
    if x2 == x1:
        return True
    else:
        return True if y3 != (y2 - y1) / (x2 - x1) * (x3 - x1) + y1 else False


if check(xa, ya, xb, yb, xc, yc):
    d1 = (distance(xa, ya, xc, yc) + distance(xc, yc, xb, yb)) * 2
    d2 = (distance(xa, ya, xb, yb) + distance(xb, yb, xc, yc)) * 2
    d3 = (distance(xc, yc, xa, ya) + distance(xa, ya, xb, yb)) * 2
    print(max(d1, d2, d3) - min(d1, d2, d3))
else:
    print(-1.0)
