import sys

input = sys.stdin.readline


def change(A, i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = "0" if A[x][y] == "1" else "1"
    return A


n, m = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(list(map(str, input()[:-1])))
for _ in range(n):
    B.append(list(map(str, input()[:-1])))

cnt = 0
for i in range(n - 3 + 1):
    for j in range(m - 3 + 1):
        if A[i][j] != B[i][j]:
            A = change(A, i, j)
            cnt += 1

print(cnt if A == B else -1)
