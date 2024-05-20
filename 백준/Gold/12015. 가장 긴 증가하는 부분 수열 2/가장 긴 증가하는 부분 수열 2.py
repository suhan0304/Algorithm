import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

dp = [arr[0]]

for i in range(n) :
    if dp[-1] < arr[i] :
        dp.append(arr[i])
    else :
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))