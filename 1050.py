import sys
from collections import defaultdict, deque
def input() :
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())

ingre = dict()
for _ in range(N) :
    name, cost = input().split()
    ingre[name] = int(cost)

# input - 조합식
combinations = deque()
for _ in range(M) :
    combinations.append(input().strip().split('='))

# 내 생각에 내가 틀리는 이유는 만들 수 있는 것을 빼버리기 때문인듯.
# 그러니깐 만들고 나면 popleft 해준거를 다시 넣지 않기 때문에 이미 완성한 조합법의 재료 중에서 하나가
# 최저 값이 갱신되면 해당 음식 또한 최저값으로 갱신되어야 함.

# -> 결국 조합식이 두 개 이상인 재료가 있으면 해당 재료는 두 개의 조합식을 계산해서 최저값으로 
# 다른 식에 들어가도록 해야함
# 재료1 = 100
# LOVE = 재료1*5  //LOVE가 500이 되어버림, LOVE가 25가 되도록 해야함
# 재료1 = 5
# 풀이 방법을 바꿔야 할듯

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