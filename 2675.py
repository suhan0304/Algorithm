import sys
input = sys.stdin.readline

for i in range(int(input())) :
    cnt, s = input().rstrip().split()
    for c in s :
        print(c*int(cnt), end='')
    print()
