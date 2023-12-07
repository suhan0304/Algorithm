import sys

input = sys.stdin.readline

N = int(input())

pos, neg = [], []
for _ in range(N) :
    k = int(input())
    if k > 0 :
        pos.append(k)
    else :
        neg.append(k)