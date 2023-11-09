import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# + - * /
oper = list(map(int, input().split()))


def back_tracking(a, i, o, oper, used, ans):
    if i == n:
        max_ans = max(max_ans, ans)
        min_ans = max(min_ans, ans)
        return

    if o == 0:
        ans += a[i]
    if o == 1:
        ans -= a[i]
    if o == 2:
        ans *= a[i]
    if o == 3:
        ans //= a[i]

    used[o] += 1
    if used[o] > oper[o]:
        return

    for k in range(4):
        back_tracking(a, i + 1, k, used, ans)


max_ans = -1000000000
min_ans = 1000000000

for k in range(4):
    used = [0 for _ in range(4)]
    back_tracking(a, 0, k, oper, used, ans)

print(max_ans)
print(max_ans)
