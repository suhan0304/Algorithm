import sys
input = sys.stdin.readline

def power(a,b, c) :
    if b == 1 : return a%c
    if b == 2 : return (a*a)%c

    if b%2 :
        return((power(a,b//2,c)**2)*a)%c
    else :
        return((power(a,b//2,c)**2)%c)

a, b, c = map(int, input().rstrip().split())
print(power(a,b,c))
