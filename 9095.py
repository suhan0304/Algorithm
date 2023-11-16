import sys

n = int(sys.stdin.readline())

idx = []
for _ in range(n) :
    idx.append(int(sys.stdin.readline()))
m = max(idx)

ans = [1, 1, 2]

for i in range(3,m+1) :
    ans.append(sum(ans[i-3:i]))   
    
for i in idx :
    print(ans[i])