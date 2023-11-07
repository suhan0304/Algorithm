import sys

input = sys.stdin.readline


def eratosthenes_sieve(N):
    IsPrime[0] = IsPrime[1] = False
    for i in range(2, int(N**0.5) + 1):
        for j in range(i * 2, N + 1, i):
            IsPrime[j] = False
    prime = []
    for i in range(N + 1):
        if IsPrime[i]:
            prime.append(i)

    return prime


N = int(input())
IsPrime = [True] * (N + 2)
prime = eratosthenes_sieve(N)
# print(prime)

ans = 0
start = 0
end = 1
while start < end and end <= len(prime):
    s = sum(prime[start:end])
    if s == N:
        # print(start, end)
        ans += 1
        start += 1
        end += 1
    elif s < N:
        end += 1
    elif s > N:
        start += 1

print(ans)
