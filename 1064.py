import sys

input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())

import math


def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


# D의 좌표를 구하지 않아도 둘레는 구할 수 있음
# 1. AC + CB * 2
# 2. AB + BC * 2
# 3. CA + AB * 2
# 두점의 거리를 구하는 함수를 만들어 쉽게 해결

# 평행사변형이 안나오는 세점 예외처리해줘야할듯

d1 = (distance(xa, ya, xc, yc) + distance(xc, yc, xb, yb)) * 2
d2 = (distance(xa, ya, xb, yb) + distance(xb, yb, xc, yc)) * 2
d3 = (distance(xc, yc, xa, ya) + distance(xa, ya, xb, yb)) * 2

print(max(d1, d2, d3) - min(d1, d2, d3))
