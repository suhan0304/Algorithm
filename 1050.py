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
    before_cnt = len(combinations)
    for i in range(len(combinations)) :
        target, combination = combinations.popleft()
        cost = 0
        for comb in combination.split('+') :
            if target == comb[1:] :
                break
            if comb[1:] not in ingre :
                combinations.append([target, combination])
                break
            cost += int(comb[0]) * ingre[comb[1:]]
        else :
            if target in ingre :
                ingre[target] = min(cost, ingre[target])
            else :
                ingre[target] = cost
    after_cnt = len(combinations)
    if before_cnt == after_cnt :
        break

if 'LOVE' in ingre: 
    if ingre['LOVE'] > 10 ** 9 :
        print(1000000001)
    else :
        print(ingre['LOVE'])
else :
    print(-1)