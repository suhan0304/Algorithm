import sys
input = sys.stdin.readline

N, M, Q = map(int, input().rstrip().split())

group = dict()
price = dict()
stock = dict()

for _ in range(N) :
    G, H, P = input().rstrip().split()
    price[H].append(int(P))
    stock[H] = 0
    if G in group :
        group[G].append(H)
    else :
        group[G] = [H]

for _ in range(Q) :
    M, COMPANY, NUM = input().rstrip().split()
    if M == "1" :
        if M >= price[COMPANY] * int(NUM) :
            M -= price[COMPANY] * int(NUM)
            stock[COMPANY] += int(NUM)
    elif M == "2" :
        if stock[COMPANY] > int(NUM) : 
            stock[COMPANY] -= int(NUM)
            M += int(NUM) * price[COMPANY]
