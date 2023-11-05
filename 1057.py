import sys

input = sys.stdin.readline

n, a, b = map(int, input().split())


def nextRound(n, a, b, round):
    n = (n + 1) // 2
    a = (a + 1) // 2
    b = (b + 1) // 2
    return n, a, b, round + 1


round = 1

while n > 2:
    # n이 홀수일때 끝자리에 a, b 둘 중 한명 있다면 바로 다음 라운드
    if n % 2 == 1 and a == n or n % 2 == 1 and b == n:
        n, a, b, round = nextRound(n, a, b, round)
    # n이 짝수이면 a, b가 붙는지를 확인
    # a와 b가 순서 상관없이 홀수, 홀수+1 일때 둘이 대전 아니면 다음 라운드
    else:
        if a % 2 == 1 and b == a + 1 or b % 2 == 1 and a == b + 1:
            break
        else:
            n, a, b, round = nextRound(n, a, b, round)
print(round)
