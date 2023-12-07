import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

coins = []

for i in range(N) :
    coins.append(int(input()))

def solution(K) :
    ans = 0
    for coin in coins :
        if K > coin :
            ans += K//coin
            K %= coin
        else :
            continue
    return ans

print(solution(K))