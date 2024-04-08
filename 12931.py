import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

ans = 0
while sum(a) > 0 :
    print(a)
    for i in range(len(a)) :
        if a[i] % 2 == 1 :
            a[i] -= 1
            ans += 1

        if a[i] != 0 :
            a[i] /= 2
    ans += 1

print(ans)