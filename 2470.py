import sys

input = sys.stdin.readline

n = int(input())
solution = list(map(int, input().split()))
solution.sort()

left = 0
right = n - 1

min_gap = abs(solution[left] + solution[right])
ans = [solution[left], solution[right]]

while left <= right:
    gap = solution[left] + solution[right]
    if abs(gap) < min_gap:
        min_gap = abs(gap)
        ans = [left, right]
        if ans == 0:
            break
    if gap < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])
