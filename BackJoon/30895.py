import sys
import math

input = sys.stdin.readline

def solution(X, Y, K) :
    ran = math.lcm(X, X+Y)
    
    min_eff = (math.ceil(K/X) / math.ceil(K/(X+Y)))
    ans = K
    for j in range(1, 3) :
        for i in range(K+1, K+j*ran+1, X) :
            eff = (math.ceil(i/X) / math.ceil(i/(X+Y)))
            if eff < min_eff :
                min_eff = eff
                ans = i
            
        
        for i in range(K+1, K+j*ran+1, X+Y) :
            eff = (math.ceil(i/X) / math.ceil(i/(X+Y)))
            if eff < min_eff :
                min_eff = eff
                ans = i
    
    return ans

X, Y, K = map(int, input().rstrip().split())
print(solution(X,Y,K))


    