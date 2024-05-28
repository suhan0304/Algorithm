import sys
input = sys.stdin.readline

for _ in range(3):
    total = 0 
    coins = [] 
   
    for _ in range(int(input())):
        coin, cnt = map(int, input().split())
        total += coin * cnt
        coins.append([coin, cnt])

    if total % 2 == 1:
        print(0)
        continue

    total //= 2
    dp = [True] + [False] * total

    answer = 0
    for i in range(len(coins)):
        coin, cnt = coins[i]
        for n in range(total, coin-1, -1):
            if dp[n-coin]:
                for j in range(cnt):
                    if n + coin * j <= total:
                        dp[n + coin * j] = True
                    else:
                        break
                        
        if dp[-1]: 
            answer = 1
            break

    print(answer)