import sys

input = sys.stdin.readline

n = int(input())

arr = list(map,int(input().rstrip().split()))

ans = 0

def proc(a, dsum, cnt) :
    if cnt == len(arr) - 2:
        ans = max(ans,dsum)

    for i in range(1,len(arr)-1) :
        score = 
        temp = a.pop(i)

