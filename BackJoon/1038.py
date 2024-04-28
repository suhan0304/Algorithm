import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
ans = []
def dfs(s, k) :
    if len(s) > k :
        return
    
    global cnt

    if len(s) == k :
        ans.append(s)
        
    for i in range(0, 10) :
        if len(s) == 0 or s[-1] > str(i) :
            dfs(s+[str(i)], k)

for i in range(1, 11) :
    dfs([], i)

print(-1 if len(ans) <= n else "".join(ans[n]))
    