import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    ans = x
    while True:
        if ans > math.lcm(M, N):
            ans = -1
            break
        if ans % N == y % N:
            break
        ans += M

    print(ans)
