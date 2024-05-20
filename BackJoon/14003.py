import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

for i in range(n) :
    for j in range(n) :