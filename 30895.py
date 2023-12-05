import sys
import math

input = sys.stdin.readline

X, Y, K = map(int, input().rstrip().split())

def find_efficiency(m) :
    return (math.ceil(m/X) / math.ceil(m/(X+Y)))

def solution(X,Y, K) :
    lowest_ans = 10**9
    left, right = K, 10**9
    
    while left < right : 
        mid = (left + right) // 2 
        
        x_eff = (mid + X - 1) // X
        xy_eff = (mid + X + Y - 1) // (X + Y)
        
        if x_eff > xy_eff :
            right = mid
        else :
            left = mid + 1
    return left

result = solution(X, Y, K)
print("가장 낮은 효율의 정수:", result)