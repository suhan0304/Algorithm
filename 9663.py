import sys


def promising(x):
    for i in range(x):
        if board[x] == board[i]:
            return 0
        elif abs(x - i) == abs(board[x] - board[i]):
            return 0
    return 1


def nqueen(x):
    global ans
    if x == N:
        ans += 1
        return
    else:
        for i in range(N):
            board[x] = i  # [x, i]에 퀸을 위치
            if promising(x):
                nqueen(x + 1)


N = int(sys.stdin.readline())
ans = 0
board = [0 for _ in range(N)]
nqueen(0)
print(ans)
