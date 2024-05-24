import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().rstrip().split())))

min_s = 3e9
ans = [0, 0, 0]

for i in range(n-2) :
    l, r = i+1, n-1

    while l < r :
        s = arr[i] + arr[l] + arr[r]

        if abs(s) < abs(min_s) :
            ans = [arr[i], arr[l], arr[r]]
            min_s = s

        if s < 0 :
            l += 1
        elif s > 0 :
            r -= 1
        else :
            break

    if s == 0 :
        break

print(*ans)