import sys
input = sys.stdin.readline

N, M, Q = map(int, input().rstrip().split())

group = dict()
price = dict()

for _ in range(N) :
    G, H, P = map(int, input().rstrip().split())
    if G in group :
        group[G].append(H)
    else :
        group[G] = [H]