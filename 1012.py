def findCabbage(x, y):
    if ground[x][y] == 1:
        ground[x][y] = -1
        # 상하좌우 순서대로 배추가 있는지 확인 후 0으로 만든다
        if x > 0 and ground[x - 1][y] == 1:
            findCabbage(x - 1, y)
        elif x < len(ground) - 1 and ground[x + 1][y] == 1:
            findCabbage(x + 1, y)
        elif y > 0 and ground[x][y - 1] == 1:
            findCabbage(x + 1, y)
        elif y < len(ground[0]) - 1 and ground[x][y + 1] == 1:
            findCabbage(x, y + 1)
        return


ans = []
T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    ground = [[0 for _ in range(N)] for __ in range(M)]
    for j in range(K):
        y, x = map(int, input().split())
        ground[x][y] = 1

    cnt = 0
    """
    for x in range(N - 1):
        for y in range(M - 1):
            if ground[x][y] == 0:
                continue
            else:
                cnt += 1
                findCabbage(x, y)

    ans.append(cnt)

    for j in ground:
        print(j)

    """
