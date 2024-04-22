import sys

input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int,input().rstrip().split()))

ans = [0 for _ in range(sum(arr)+2)] 

def dfs(b, idx) :
    ans[sum(b)] = -1

    for i in range(idx, n) :
        b.append(arr[i])
        dfs(b, i+1) 
        b.pop()

dfs([], 0)

for i in range(len(ans)) :
    if ans[i] == 0 :
        print(i)
        break