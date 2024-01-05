import sys
input = sys.stdin.readline

N, M, Q = map(int, input().rstrip().split())

group = dict()
price = dict()
stocks = dict()

for _ in range(N) :
    G, H, P = input().rstrip().split()
    price[H] = int(P)
    stocks[H] = 0
    if G in group :
        group[G].append(H)
    else :
        group[G] = [H]

for _ in range(Q) :
    line = input().strip()
    if line == "6" or line == "7" :
        menu = line
    else :
        menu, st, num = line.split()
        num = int(num)
    if menu == "1" :
        if M >= price[st] * num :
            M -= price[st] * num
            stocks[st] += num
    elif menu == "2" :
        if stocks[st] >= num : 
            M += num * price[st]
            stocks[st] -= num
        elif stocks[st] < num :
            M += stocks[st] * price[st]
            stocks[st] = 0
    elif menu == "3" :
        price[st] += num
    elif menu == "4" :
        for i in group[st] :
            price[i] += num
    elif menu == "5" :
        for i in group[st] :
            price[i] = (price[i] * (100 + num)/100)//10 * 10
    elif menu == "6" :
        print(int(M))
    elif menu == "7" :
        temp_M = M
        for stock in stocks :
            if stocks[stock] != 0 :
                temp_M += price[stock] * stocks[stock]
        print(int(temp_M))