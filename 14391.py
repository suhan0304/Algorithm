import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(n)]


def proc():
    result = 0
    for i in range(1 << n * m):
        dsum = 0
        for r in range(n):
            srow = 0
            for c in range(m):
                idx = r * m + c
                if i & (1 << idx) != 0:
                    srow = srow * 10 + arr[r][c]
                else:
                    dsum += srow
                    srow = 0
            dsum += srow

        for c in range(m):
            scol = 0
            for r in range(n):
                idx = r * m + c
                if i & (1 << idx) == 0:
                    scol = scol * 10 + arr[r][c]
                else:
                    dsum += scol
                    scol = 0
            dsum += scol
        result = max(result, dsum)
    return result


print(proc())
