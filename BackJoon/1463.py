import sys

input = sys.stdin.readline

x = int(input())

ans = [0,0,1,1]

for i in range(4,x+1) :
    ans.append(ans[i-1] + 1)
    if i % 3 == 0:
        ans[i] = min(ans[i//3]+1,ans[i]) 
    if i % 2 == 0 :
        ans[i] = min(ans[i//2]+1,ans[i]) 

print(ans[x])
    