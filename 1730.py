import sys

input = sys.stdin.readline

n = int(input())

s = input()[:-1]

# U D L R

dir = ["U", "D", "L", "R"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x = 0
y = 0

arr = [["." for _ in range(n)] for _ in range(n)]

for i in range(len(s)):
    next_x = x + dx[dir.index(s[i])]
    next_y = y + dy[dir.index(s[i])]
    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
        continue
    else:
        if dir.index(s[i]) <= 1:
            arr[y][x] = "+" if arr[y][x] == "-" or arr[y][x] == "+" else "|"
            arr[next_y][next_x] = (
                "+" if arr[next_y][next_x] == "-" or arr[next_y][next_x] == "+" else "|"
            )
        elif dir.index(s[i]) >= 2:
            arr[y][x] = "+" if arr[y][x] == "|" or arr[y][x] == "+" else "-"
            arr[next_y][next_x] = (
                "+" if arr[next_y][next_x] == "|" or arr[next_y][next_x] == "+" else "-"
            )
        x = next_x
        y = next_y

for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()
