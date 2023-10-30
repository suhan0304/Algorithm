T = int(input())
for i in range(T) :
    N, M, K = map(int, input().split())
    ground = [[0 for _ in range(N)] for __ in range(M) ] 
    for j in range(K) :
        y, x = map(int, input().split())
        ground[x][y] = 1
    print(ground)
    