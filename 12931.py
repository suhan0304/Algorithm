import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

ans = 0
while sum(a) > 0 :
    # remove odd number element in array
    for i in range(len(a)) :
        if a[i] % 2 == 1 :
            a[i] -= 1
            ans += 1

    if sum(a) == 0 : break

    # devide 2 all even number in array
    a = [x / 2 for x in a]
    ans += 1

print(ans)