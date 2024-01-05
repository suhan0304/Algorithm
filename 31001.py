import sys
input = sys.stdin.readline

N, M, Q = input().rstrip().split()

group = dict()
price = dict()
stocks = dict()

for _ in range(int(N)) :
    G, H, P = input().rstrip().split()
    price[H] = int(P)
    stocks[H] = 0
    if G in group :
        group[G].append(H)
    else :
        group[G] = [H]

for _ in range(int(Q)) :
    M, st, num = input().rstrip().split()
    num = int(num)
    if M == "1" :
        if M >= price[st] * num :
            M -= price[st] * num
            stocks[st] += num
    elif M == "2" :
        if stocks[st] > num : 
            stocks[st] -= num
            M += num * price[st]
    elif M == "3" :
        price[st] += num
    elif M == "4" :
        for i in group[st] :
            price[i] += num
    elif M == "5" :
        for i in group[st] :
            price[i] = price[i] * (100 + num)/100
    elif M == "6" :
        print(M)
    elif M == "7" :
        temp_M = M
        for stock in stocks :
            if stocks[stock] != 0 :
                temp_M += price[stock] * stocks[stock]
        print(temp_M)



