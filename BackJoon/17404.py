import sys
input = sys.stdin.readline

n = int(input())

cost = []
for _ in range(n) :
    cost.append(list(map(int,input().rstrip().split())))
print(cost)

print(min(cost[n-1]))