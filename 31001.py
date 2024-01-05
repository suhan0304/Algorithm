import sys
input = sys.stdin.readline

N, M, Q = map(int, input().rstrip().split())

group = dict()
price = dict()
stock = dict()

for _ in range(N) :
    G, H, P = input().rstrip().split()
    price[H].append(int(P))
    if G in group :
        group[G].append(H)
    else :
        group[G] = [H]

for _ in range(Q) :
    M, I1, I2 = input().rstrip().split()
    if M == "1" :
        if M >= price[I1] * int(I2) :
            M -= price[I1] * int(I2)
            if I1 in stock :
                stock[I1] += int(I2)
            else :
                stock[I1] = int(I2)