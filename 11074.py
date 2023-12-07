import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

arr = [int(input().rstrip()) for _ in range(N)]
arr.sort(reverse=True)

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