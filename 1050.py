import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

# input - 재료 & 비용
material = dict() #재료
for _ in range(N) :
    name, cost = input().split()
    material[name] = int(cost)

# input - 조합식
combinations = deque()
for _ in range(M) :
    combinations.append(input().strip().split('='))

while combinations :
    target, combination = combinations.popleft()
    cost = 0
    for comb in combination.split('+') :
        if comb not in material
        cost += int(comb[0]) * material[comb[1:]]
    if target in material :
        material[target] = min(cost, material[target])
    else :
        material[target] = cost

for i in material :
    print(i)
for p in material :
    print(p)