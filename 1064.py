import sys

input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())

# D의 좌표를 구하지 않아도 둘레는 구할 수 있음
# 1. AC + CB * 2
# 2. AB + BC * 2
# 3. CA + CB * 2
# 두점의 거리를 구하는 함수를 만들어 쉽게 해결
