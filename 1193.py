import sys

input = sys.stdin.readline

X = int(input())

n = 0
m = 0
while X > m:
    n += 1
    m = int(n * (n + 1) / 2)

if n % 2 == 0:
    numerator = n - (m - X)
    denominator = 1 + +(m - X)
else:
    numerator = 1 + (m - X)
    denominator = n - (m - X)

print(str(numerator) + "/" + str(denominator))
