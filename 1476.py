import sys

target = list(map(int, sys.stdin.readline().split()))

esm = [1, 1, 1]

ans = 1
while esm != target:
    esm = [
        esm[0] + 1 if esm[0] != 15 else 1,
        esm[1] + 1 if esm[1] != 28 else 1,
        esm[2] + 1 if esm[2] != 19 else 1,
    ]
    ans += 1

print(ans)
