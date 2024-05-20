import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

LIS = [arr[0]]
dp = [(0, arr[0])]

for i in range(n) :
    if LIS[-1] < arr[i] :
        LIS.append(arr[i])
        dp.append((len(LIS)-1, arr[i]))
    else :
        idx = bisect.bisect_left(LIS, arr[i])
        LIS[idx] = arr[i]
        dp.append((idx, arr[i]))


print(len(LIS))

last_idx = len(LIS) - 1
ans = []
for i in range(len(dp)-1, -1, -1) :
    if dp[i][0] == last_idx :
        ans.append(dp[i][1])
        last_idx -= 1

print(*ans[::-1])