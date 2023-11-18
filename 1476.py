import sys

input = sys.stdin.readline

e, s, m = map(int, input().split())

ans = 1
while not (ans % 15 == e % 15 and ans % 28 == s % 28 and ans % 19 == m % 19):
    ans += 1

print(ans)
