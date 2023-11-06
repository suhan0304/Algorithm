import sys

ipnut = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

p = []
for i in range(len(b)):
    idx = b.index(a[i])
    p.append(str(idx))
    b[idx] = -1
print(" ".join(p))
