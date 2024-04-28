import sys

input = sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))

min_1 = min(dice)
min_2 = 2 * (10**6)
min_3 = 3 * (10**6)
for i in range(6):
    for j in range(i + 1, 6):
        if dice[i] + dice[j] < min_2:
            if i + j != 5:
                min_2 = dice[i] + dice[j]
        for k in range(j + 1, 6):
            if dice[i] + dice[j] + dice[k] < min_3:
                if i + j != 5 and j + k != 5 and k + i != 5:
                    min_3 = dice[i] + dice[j] + dice[k]

ans = 0
if n == 1:
    ans = sum(sorted(dice)[:5])
else:
    ans += min_1 * ((n - 1) * (n - 2) * 4 + (n - 2) * (n - 2))
    ans += min_2 * ((n - 1) * 4 + (n - 2) * 4)
    ans += min_3 * 4
print(ans)
