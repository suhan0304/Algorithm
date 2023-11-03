import sys

input = sys.stdin.readline

n = int(input())
solution = list(map(int, input().split()))
solution.sort()

left = 0
right = n - 1

min_gap = abs(solution[left] + solution[right])
ans = [solution[left], solution[right]]

while left < right:
    sum = solution[left] + solution[right]
    if abs(sum) < min_gap:
        min_gap = abs(sum)
        ans = [solution[left], solution[right]]
        if ans == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])
