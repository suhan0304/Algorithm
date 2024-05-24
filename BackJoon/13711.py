import sys
import bisect
input = sys.stdin.readline

n = int(input())
    
arr = []

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
c = [0 for _ in range(n)]

for i in range(n) :
    c[a[i]-1] = i
for i in range(n) :
    arr.append(c[b[i]-1])

LIS = [arr[0]]

for i in range(n) :
    if LIS[-1] < arr[i] :
        LIS.append(arr[i])
    else :
        idx = bisect.bisect_left(LIS, arr[i])
        LIS[idx] = arr[i]

print(len(LIS))