n = int(input())
ans = 0
board = [0] * n


def promising(x):
    for i in range(x):
        if board[x] == board[i] or abs(x - i) == abs(board[x] - board[i]):
            return False
    return True


def nqueen(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            board[x] = i  # [x, i]에 퀸을 위치
            if promising(x):
                nqueen(x + 1)


nqueen(0)
print(ans)
