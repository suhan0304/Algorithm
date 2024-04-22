r1, c1, r2, c2 = map(int, input().split())

ans = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]

digit = 0
for r in range(r2 - r1 + 1):
    for c in range(c2 - c1 + 1):
        R = r1 + r
        C = c1 + c

        ans[r][c] = [R, C]

        n = max(abs(R), abs(C))
        if R >= C:
            ans[r][c] = (((n * 2) + 1) ** 2) - (abs(n - R) + abs(n - C))
        else:
            ans[r][c] = 4 * (n**2) - (abs((-n) - R) + abs((-n + 1) - C))
        if ans[r][c] > digit:
            digit = ans[r][c]

import math

digit = int(math.log10(digit)) + 1

for i in ans:
    for j in i:
        print(str(j).rjust(digit), end=" ")
    print()
