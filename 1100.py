import sys

input = sys.stdin.readline

ans = 0
for i in range(8) :
    board = input().rstrip()
    for j in range(8) : 
        if (i+j)%2 == 0 :
            if board[j] == 'F' :
                ans += 1

print(ans)