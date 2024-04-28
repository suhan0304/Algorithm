import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().rstrip().split()))

ans = 0

def proc(a, dsum, cnt) :
    if cnt == len(arr) - 2:
        global ans
        ans = max(ans,dsum)
        return 

    for i in range(1,len(a)-1) :
        proc(a[0:i] + a[i+1:len(a)], dsum + a[i-1] * a[i+1], cnt + 1)

proc(arr, 0, 0)
print(ans)

