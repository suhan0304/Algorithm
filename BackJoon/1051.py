import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(input())[:-1])


def find_square(length, ans):
    for i in range(n - (length - 1)):
        for j in range(m - (length - 1)):
            if (
                arr[i][j] == arr[i][j + (length - 1)]
                and arr[i][j] == arr[i + (length - 1)][j]
                and arr[i][j] == arr[i + (length - 1)][j + (length - 1)]
            ):
                return length * length
    return ans


ans = 1
for length in range(2, n + 1):
    ans = find_square(length, ans)

print(ans)
