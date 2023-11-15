import sys

input = sys.stdin.readline

n, m = map(int, input().split())

isPrime = [False, False] + [True] * m
for i in range(2, int(m**0.5 + 1)):
    if isPrime[i]:
        for j in range(2 * i, m + 1, i):
            isPrime[j] = False

for i in range(n, m + 1):
    if isPrime[i]:
        print(i)
