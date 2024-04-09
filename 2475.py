import sys
input = sys.stdin.readline

a = list(map(int, input().rstrip().split()))
ans = 0
for i in range(5) : ans += a[i]**2
print(ans%10)