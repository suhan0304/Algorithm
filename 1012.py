T = int(input())
for i in range(T) :
    N, M, K = map(int, input().split())
    field = [[0] * M]* N
    for j in range(K) :
        y, x = map(int, input().split())
        field[x][y] = 0
    print(field)