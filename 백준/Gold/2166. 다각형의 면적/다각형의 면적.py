import sys
input = sys.stdin.readline

n = int(input())
dots = [tuple(map(int,input().rstrip().split())) for _ in range(n)]
dots.append(dots[0])

ans = 0.
for i in range(n) :
    ans += dots[i][0] * dots[i+1][1]
    ans -= dots[i][1] * dots[i+1][0]
print(round(abs(ans/2),1))