import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().rstrip().split())))

l, r = 0, n-1
min_s = 2e9
ans = [0, 0]

while l < r :
    s = arr[l] + arr[r] 

    if abs(s) < abs(min_s) :
        ans = [arr[l], arr[r]]
        min_s = s
    
    if s < 0 :
        l += 1
    elif s > 0 :
        r -= 1
    else :
        break
print(*ans)