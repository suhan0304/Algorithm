import sys

input = sys.stdin.readline

K = int(input())

for X in range(1, K):
    n = 1
    m = 0
    while 1 + int(n * (n - 1) / 2) <= X:
        n += 1
    n -= 1
    m = 1 + int(n * (n - 1) / 2)
    ans1 = n - (X - m)
    ans2 = 1 + (X - m)
    print(str(ans1) + "/" + str(ans2))
