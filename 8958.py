import sys
input = sys.stdin.readline

for i in range(int(input())) :
    s = input().rstrip()
    ans = [0]
    for i in range(len(s)) :
        if s[i] == 'O' :
            ans.append(ans[-1] + 1)
        else :
            ans.append(0)
    print(sum(ans))