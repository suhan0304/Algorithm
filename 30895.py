import sys
import math

input = sys.stdin.readline

X, Y, K = map(int, input().rstrip().split())

m = math.lcm(X, X+Y)
print(m)

ans = [0, ((K+1)//X)/(K+1)]
for i in range(K+1, K+m+1) :
    cnt_none = i//X
    cnt_item = i//(X+Y)
    
    if cnt_none/cnt_item < ans[1] :