import sys

input = sys.stdin.readline

n, a, b = map(int, input().split())


def nextRound(n, a, b, round):
    n = (n + 1) // 2
    a = (a + 1) // 2
    b = (b + 1) // 2
    return n, a, b, round + 1


round = 1

while n > 2:
    if n % 2 == 1 and a == n or n % 2 == 1 and b == n:
        n, a, b, round = nextRound(n, a, b, round)
    else:
        if a % 2 == 1 and b == a + 1 or b % 2 == 1 and a == b + 1:
            break
        else:
            n, a, b, round = nextRound(n, a, b, round)
print(round)
