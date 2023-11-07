MOD = 1000000000


def dp(n, k):
    d[0][0] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for l in range(j + 1):
                d[i][j] += d[i - 1][j - l]
                d[i][j] %= MOD
    f = 0
    for i in d:
        f += i[-1]
    return f


n, k = map(int, input().split())
d = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
print(dp(n, k) % MOD)
