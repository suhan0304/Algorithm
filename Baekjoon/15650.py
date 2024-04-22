import itertools
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = list(range(1, n + 1))

ans = list(itertools.combinations(a, m))

for a in ans:
    print(*a)
