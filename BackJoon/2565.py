import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key = lambda x : x[0])

#print(arr)

LIS = []
dp = []

for i, j in arr :
    if not LIS :
        LIS.append(j)

    if LIS[-1] < j :
        LIS.append(j)
        dp.append((len(LIS)-1, j))
    else :
        idx = bisect.bisect_left(LIS, j)
        LIS[idx] = j
        dp.append((idx, j))

print(n - len(LIS))