n = [[0],
     [1],
     [2,4,8,6],
     [3,9,7,1],
     [4,6],
     [5],
     [6],
     [7,9,3,1],
     [8,4,2,6],
     [9,1]]

T = int(input())
for _ in range(T) :
    a, b = map(int, input().split())
    a%=10
    if a==0 :
        ans = 10
    else :
        ans = n[a][b%len(n[a])-1]
    print(ans)
