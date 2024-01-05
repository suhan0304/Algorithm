import sys
input = sys.stdin.readline

N, M, Q = map( inut().rstrip().split())

group = dict()
price = dict()
stock = dict()

for _ in range(N) :
    G, H, P = input().rstrip().split()
    price[H].append(P))    stock[H] = 0
    if G in group :
        group[G].append(H)
    else :
        group[G] = [H]

for _ in range(Q) :
    M, st, num = input().rstrip().split()
    num = int(num)
    if M == "1" :
        if M >= price[st] * num :
            M -= price[st] * num
            stock[st] += num
    elif M == "2" :
        if stock[st] > num : 
            stock[st] -= num
            M += num * price[st]
    elif M == "3" :
        price[st] += num
    elif M == "4" :
        for i in group[st] :
            price[i] += num
