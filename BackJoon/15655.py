import itertools
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = sorted(list(map(int, input().split())))

ans = list(itertools.combinations(a, m))

for a in ans:
    print(*a)
