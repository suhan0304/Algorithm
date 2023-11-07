import sys

input = sys.stdin.readline


def matrix_square(a, b):
    ans = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans[i][j] += a[i][k] * b[k][j]
                ans[i][j] %= 1000
    return ans


N, B = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
arr = [A]
for i in range(len(bin(B)[2:]) - 1):
    arr.append(matrix_square(arr[i], arr[i]))
idx = bin(B)[:1:-1]
ans = []
for i in range(len(idx)):
    if idx[i] == "1":
        if len(ans) == 0:
            ans = arr[i]
        else:
            ans = matrix_square(ans, arr[i])
for line in ans:
    for x in line:
        print(x % 1000, end=" ")
    print()
