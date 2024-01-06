import sys
input = sys.stdin.readline

N, M, Q = map(int, input().rstrip().split())

group = dict()
price = dict()

for _ in range(N) :
    G, H, P = input().rstrip().split()
    if G in group :
        group[G].append(H)
    else :
        group[G] = [H]

for _ in range(Q) :
    M, I1, I2 = input().rstrip().split()