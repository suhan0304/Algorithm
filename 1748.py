import sys
import math

input = sys.stdin.readline

n = int(input())

ans = 0
for i in range(int(math.log10(n)) + 1):
    ans += n - (10**i) + 1
print(ans)
