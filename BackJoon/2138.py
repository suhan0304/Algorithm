import sys
input = sys.stdin.readline

n = int(input())
cur = list(map(int, input()))
target = list(map(int, input()))

before = cur[:]

cnt = 0
for i in range(2) :
    cur[0] = (cur[0]+i)%2
    cur[1] = (cur[0]+i)%2
    for j in range(1, n) :
        if cur[j-1] != target[j-1] :
            cnt += 1
            cur[j-1] = (cur[j-1]+1)%2
            cur[j] = (cur[j]+1)%2
            if j != n - 1 :
                cur[j+1] = (cur[j+1]+1)%2
    for i in range(n) :
        if cur[i] != target[i] :
            cur = before[:]
            ans = 1
            break
    else :
        print(ans)
        exit(0)
    print(-1)