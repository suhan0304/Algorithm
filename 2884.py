import sys
input = sys.stdin.readline

h, m = int(input().rstrip().split())

if m >= 45 :
    m -= 45
else :
    h = h - 1 if h != 0 else 23
    m = m + 60 - 45 