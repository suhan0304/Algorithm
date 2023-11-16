import sys

input = sys.stdin.readline


def eratosthenes_sieve(m):
    isPrime = [False, False] + [True] * m
    for i in range(2, int(m**0.5 + 1)):
        if isPrime[i]:
            for j in range(2 * i, m + 1, i):
                isPrime[j] = False
    prime = []
    for i in range(m + 1):
        if IsPrime[i]:
            prime.append(i)

    return prime


print(1)
