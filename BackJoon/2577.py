import sys
input = sys.stdin.readline

ans = 1

for i in range(3) :
    ans *= int(input())

for i in range(10) :
    print(str(ans).count(str(i)))