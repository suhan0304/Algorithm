import sys

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

ingre = dict() #재료

for _ in range(N) :
    name, cost = input().split()
    ingre[name] = int(cost)

for _ in range(M) :
    