import sys
n = int(sys.stdin.readline())
ans = [1, 1]
for i in range(2, n+1) :
    ans.append(ans[i-1] + ans[i-2]*2)
print(ans[n]%10007)