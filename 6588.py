import sys

input = sys.stdin.readline
M = 10**6

isPrime = set(i for i in range(2, M))
for i in range(2, int(M**0.5 + 1)):
    if i in isPrime:
        isPrime.difference_update(range(i * i, M + 1, i))

while True:
    n = int(input())
    if n == 0:
        break

    for prime in isPrime:
        if n - prime in isPrime:
            print(n, "=", prime, "+", n - prime)
            break

    else:
        print("Goldbach's conjectrue is wrong.")
