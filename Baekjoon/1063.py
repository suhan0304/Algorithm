import sys

input = sys.stdin.readline

k, s, n = map(str, input().split())
n = int(n)

king = [ord(k[0]) - ord("A") + 1, int(k[1])]
stone = [ord(s[0]) - ord("A") + 1, int(s[1])]

# print(king[0], king[1])
# print(stone[0], stone[1])

# R L B T RT LT RB LB
dir = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

for _ in range(n):
    move = input()[:-1]
    # print(move, dir.index(move))
    # print(dx[dir.index(move)], dy[dir.index(move)])
    next_king = [king[0] + dx[dir.index(move)], king[1] + dy[dir.index(move)]]
    if next_king == stone:
        next_stone = [stone[0] + dx[dir.index(move)], stone[1] + dy[dir.index(move)]]
        if (
            next_stone[0] < 1
            or next_stone[0] > 8
            or next_stone[1] < 1
            or next_stone[1] > 8
        ):
            continue
        else:
            stone = next_stone
            king = next_king
    elif next_king[0] < 1 or next_king[0] > 8 or next_king[1] < 1 or next_king[1] > 8:
        continue
    else:
        king = next_king


print(chr(king[0] + ord("A") - 1) + str(king[1]))
print(chr(stone[0] + ord("A") - 1) + str(stone[1]))
