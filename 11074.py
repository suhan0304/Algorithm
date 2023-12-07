import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

coin = []

for i in range(N) :
    coin.append(int(input()))
def solution(K) :
    ans = 0
    for i in range(0, len(arr)) :
        if K > arr[i] :
            while K >= arr[i] :
                K -= arr[i]
                ans += 1
        if K == 0 :
            return ans
    return 

print(solution(K))