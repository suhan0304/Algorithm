import sys

input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))


def check(n):
    return


ans = 0
for m in M:
    ans = check(m) if check(m) > ans else ans
