import sys
input = sys.stdin.readline

for __ in range(3) :
    n = int(input())
    coins = []
    total = 0
    for _ in range(n) :
        coin, cnt = map(int, input().split())
        coins.append((coin,cnt))
        total += coin * cnt
    
    if total%2 == 1:
        print(0)
        continue
    total //= 2

    dp = [True] + [False] * total
    for coin, cnt in coins :

        for n in range(total, coin-1, -1) :
            if dp[n-coin] :
                for j in range(cnt) :
                    if n + coin * j <= total :
                        dp[n + coin * j] = True
                        

    print(1 if dp[-1] else 0)