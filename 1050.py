import sys

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

# input - 재료 & 비용
ingre = dict() #재료
for _ in range(N) :
    name, cost = input().split()
    ingre[name] = int(cost)

# input - 조합식
potion = dict() # 믈약
for _ in range(M) :
    target, combination = input().split('=')
    cost = 0
    for comb in combination.split('+') :
        cost += int(comb[0]) * ingre[comb[1:]]
    ingre[