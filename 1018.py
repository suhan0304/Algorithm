N, M = map(int, input().split())

chessboard = []
for _ in range(N):
    chessboard.append(input())

chg_w = [[0 for _ in range(M)] for _ in range(N)]
chg_b = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        # i + j가 짝수인 칸
        if (i + j) % 2 == 0:
            if chessboard[i][j] == "B":
                chg_w[i][j] = 1
            else:
                chg_b[i][j] = 1
        # i + j가 짝수인 칸
        elif (i + j) % 2 == 1:
            if chessboard[i][j] == "W":
                chg_w[i][j] = 1
            else:
                chg_b[i][j] = 1

ans = 64
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        s_w = s_b = 0
        for k in range(8):
            s_w += sum(chg_w[i + k][j : j + 8])
            s_b += sum(chg_b[i + k][j : j + 8])
        ans = min(ans, s_w, s_b)
"""
import numpy as np

chg_w = np.array(chg_w)
chg_b = np.array(chg_b)

ans = 64
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        s_w = s_b = 0
        s_w = np.sum(chg_w[i : i + 8, j : j + 8])
        s_b = np.sum(chg_b[i : i + 8, j : j + 8])
        ans = min(ans, s_w, s_b)

"""
print(ans)
