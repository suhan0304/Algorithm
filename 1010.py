def factorial(n):
    if n == 0 or n == 1:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1) 

T = int(input())
ans = []
for i in range(T) :
    m, n = map(int, input().split())
    ans.append(factorial(n) / (factorial(n-m) * factorial(m))) # combination 구하는 공식

for i in range(T) :
    print(int(ans[i]))