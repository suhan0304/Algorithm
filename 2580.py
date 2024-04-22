import sys

input = sys.stdin.readline

sudoku = [list(map(int,input().rstrip().split())) for _ in range(9)]

def check(sudoku, i, j, check_num) :
    for k in range(9) :
        if sudoku[i][k] == check_num : return False
        if sudoku[k][j] == check_num : return False
        if sudoku[(i//3)*3 + k//3][(j//3)*3 + k%3] == check_num : return False
    return True

empty = []

for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 :
            empty.append([i, j])

def proc(sudoku, empty, idx) :
    if idx == len(empty) :
        for _ in sudoku :
            print(*_)
        exit()
    i, j = empty[idx][0], empty[idx][1]
    for n in range(1, 10) :
        if check(sudoku, i, j, n) :
            sudoku[i][j] = n
            proc(sudoku, empty, idx+1)
            sudoku[i][j] = 0


proc(sudoku, empty, 0)