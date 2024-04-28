import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(input().strip()))


def check(arr):
    max_cnt = 1
    for i in range(n):
        cnt_row, cnt_col = 1, 1
        for j in range(1, n):
            cnt_row = cnt_row + 1 if arr[i][j] == arr[i][j - 1] else 1
            cnt_col = cnt_col + 1 if arr[j][i] == arr[j - 1][i] else 1
            max_cnt = max(max_cnt, cnt_col, cnt_row)
    return max_cnt


ans = 1
for i in range(n):
    for j in range(1, n):
        if arr[i][j] != arr[i][j - 1]:
            arr[i][j], arr[i][j - 1] = arr[i][j - 1], arr[i][j]
            ans = max(ans, check(arr))
            arr[i][j], arr[i][j - 1] = arr[i][j - 1], arr[i][j]
        if arr[j][i] != arr[j - 1][i]:
            arr[j][i], arr[j - 1][i] = arr[j - 1][i], arr[j][i]
            ans = max(ans, check(arr))
            arr[j][i], arr[j - 1][i] = arr[j - 1][i], arr[j][i]
print(ans)
