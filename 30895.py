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
    return n-m+1, n+m+1

def solution(X, Y, K) :
    start, end = find_range(X, Y, K)
    #print(start, end)
    
    min_eff = math.ceil(K//X) / math.ceil(K//(X+Y))
    ans = K
    
    for i in range(start, end, X) :
        print(i, eff, end=' ||')
        if i <= K :
            continue
        eff = find_eff(X, Y, i)
        if eff < min_eff :
            min_eff = eff
            ans = i
    for i in range(start, end, X+Y) :
        print(i, eff, end=' ||')
        if i <= K :
            continue
        eff = find_eff(X, Y, i)
        if eff < min_eff :
            min_eff = eff
            ans = i
    print()
        
    return ans

X, Y, K = map(int, input().rstrip().split())
print(solution(X,Y,K))


    