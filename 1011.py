import math
import sys

input = sys.stdin.readline

ans = []
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    n = 1
    distance = y - x
    while n**2 <= distance:
        n += 1
    n -= 1

    print((n * 2 - 1) + math.ceil((distance - (n**2)) / n))
