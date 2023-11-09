import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# + - * /
oper = list(map(int, input().split()))


def back_tracking(idx, k, used, ans):
    if idx == n:
        global max_ans
        global min_ans
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)

    if used[k] + 1 > oper[k]:
        return

    if k == 0:
        ans += a[idx]
    elif k == 1:
        ans -= a[idx]
    elif k == 2:
        ans *= a[idx]
    elif k == 3:
        ans //= a[idx]
    used[k] += 1

    for o in range(4):
        back_tracking(idx + 1, o, used, ans)


max_ans = -1000000000
min_ans = 1000000000

for k in range(4):
    ans = a[0]
    used = [0, 0, 0, 0]
    back_tracking(1, k, used, ans)

print(max_ans)
print(min_ans)
