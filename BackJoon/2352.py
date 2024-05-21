import sys
import bisect
input = sys.stdin.readline

n = int(input())
animal = set()

for _ in range(n) :
    __, l, r = map(int, input().rstrip().split())
    animal.add((l, r))

animal = list(animal)
animal.sort(key = lambda x : (x[0], -x[1]),reverse=True)

LIS = []
for i in range(len(animal)) :
    if i == 0 or LIS[-1] <= animal[i][1] :
        LIS.append(animal[i][1])
    else :
        idx = bisect.bisect_right(LIS, animal[i][1])
        LIS[idx] = animal[i][1]

print(len(LIS))