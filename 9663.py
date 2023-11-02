import sys


def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def nqueen(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        row[x] = i  # [x, i]에 퀸을 위치
        if promising(x):
            visited[i] = True  # i열 퀸 배치 표시
            nqueen(x + 1)  # i열에 퀸을 배치시킨 후 다음 열로 이동
            visited[i] = False  # i열 퀸 배치 해제


n = int(sys.stdin.readline())
ans = 0
row = [0] * n
visited = [False] * n
nqueen(0)
print(ans)
