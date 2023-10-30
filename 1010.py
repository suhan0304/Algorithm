def factorial(n):
    if n == 1:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1) 

T = int(input())
ans = []
for i in range(T) :
    m, n = map(input().split(), int)
    ans.append(factorial(n) / (factorial(n-m) * factorial(m)))