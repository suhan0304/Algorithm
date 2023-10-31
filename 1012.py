import sys

sys.setrecursionlimit(10**5)


def findCabbage(y, x):
    if ground[y][x] == 1:
        ground[y][x] = 0
        # 상하좌우 순서대로 배추가 있는지 확인 후 0으로 만든다
        if y > 0 and ground[y - 1][x] == 1:
            findCabbage(y - 1, x)
        elif y < N - 1 and ground[y + 1][x] == 1:
            findCabbage(y + 1, x)
        elif x > 0 and ground[y][x - 1] == 1:
            findCabbage(y, x - 1)
        elif x < M - 1 and ground[y][x + 1] == 1:
            findCabbage(y, x + 1)
        return


ans = []
T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)] for __ in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1

    cnt = 0
    for y in range(N):
        for x in range(M):
            if ground[y][x] == 1:
                cnt += 1
                findCabbage(y, x)

    ans.append(cnt)

for answer in ans:
    print(answer)
