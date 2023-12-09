import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

# input - 재료 & 비용
ingre = dict() #재료
for _ in range(N) :
    name, cost = input().split()
    ingre[name] = int(cost)

# input - 조합식
combinations = deque()
for _ in range(M) :
    combinations.append(input().strip().split('='))

while combinations :
    target, combination = combinations.popleft()
    cost = 0
    for comb in combination.split('+') :
        if comb[1:] not in ingre :
            combinations.append([target, combination])
            break
        cost += int(comb[0]) * ingre[comb[1:]]
    else :
        if target in ingre :
            ingre[target] = min(cost, ingre[target])
        else :
            ingre[target] = cost

for i in ingre :
    print(i)
for p in ingre :
    print(p)