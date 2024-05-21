import sys
import bisect
input = sys.stdin.readline

n = int(input())
animal = []

for _ in range(n) :
    a, l, r = map(int, input().rstrip().split())
    d = r-l     
    animal.append([a, l, r, d])

animal.sort(key = lambda x : (x[3], x[1]))

LIS = [animal[0]]

for i in range(n) :
    if LIS[-1][1] >= animal[i][1] and LTS[-1][2] <= animal[i][2] :
        LTS.append(animal[i])