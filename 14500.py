import sys

input = sys.stdin.readline

# 상, 하, 좌, 우
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 최대값 변수
maxAns = 0


# dfs 기법 : 길이 4만큼 이동하면서 최대값 찾기
def dfs(i, j, dsum, cnt):
    global maxAns
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        maxAns = max(maxAns, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ni = i + dxdy[n][0]
        nj = j + dxdy[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 및 제거
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt + 1)
            visited[ni][nj] = False


# 길이가 4가 아닌 예외 경우 처리 ㅗ, ㅜ, ㅓ, ㅏ 모양
def exce(i, j):
    global maxAns
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # dxdy 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # n = 1, k = 012 -> t = 123 -> 상 우 좌 : ㅗ
            # n = 2, k = 012 -> t = 230 -> 우 좌 하 : ㅜ
            # n = 3, k = 012 -> t = 301 -> 좌 하 상 : ㅓ
            # n = 4, k = 012 -> t = 012 -> 하 상 우 : ㅏ
            # 위와 같은 방식으로 ㅗ ㅜ ㅓ ㅏ 방문
            t = (n + k) % 4
            ni = i + dxdy[t][0]
            nj = j + dxdy[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        maxAns = max(maxAns, tmp)


for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(maxAns)
