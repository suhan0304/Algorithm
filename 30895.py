import sys
import math

input = sys.stdin.readline

def find_eff(X, Y, m) :
    return math.ceil(m//X) / math.ceil(m//(X+Y))

def find_range(X, Y, K) :
    m = math.lcm(X, X+Y)
    n = m
    while n <= K :
        n += m
    return n, m

def solution(X, Y, K) :
    n, m = find_range(X, Y, K)
    
    min_eff = math.ceil(K//X) / math.ceil(K//(X+Y))
    ans = K
    
    for i in range(n-m+1, n+1, X) :
        eff = find_eff(X, Y, i)
        if eff < min_eff :
            min_eff = eff
            ans = i
        
    for i in range(n-m+1, n+1, X+Y) :
        eff = find_eff(X, Y, i)
        if eff < min_eff :
            min_eff = eff
            ans = i
            
        
    return ans

X, Y, K = map(int, input().rstrip().split())
print(solution(X,Y,K))


    