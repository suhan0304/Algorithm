import sys
import math

input = sys.stdin.readline

X, Y, K = map(int, input().rstrip().split())



def solution() :
    eff = (math.ceil(K/X) / math.ceil(K/(X+Y)))
    ans = K
    for i in range(K+1, K+math.lcm(X, X+Y)*2+1, X) :
        cnt_none = math.ceil(i/X)
        cnt_item = math.ceil(i/(X+Y))
        if cnt_none/cnt_item < eff :
            eff = cnt_none/cnt_item
            ans = i

#print(eff)
print(solution())