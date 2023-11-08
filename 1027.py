import sys

input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))

MAX = 1000000001


def check(n):
    left_max = MAX
    right_max = MAX

    cnt = 0
    for i in range(n - 1, -1, -1):
        if left_max == MAX:
            left_max = (M[n] - M[i]) / (n - i)
            cnt += 1
        else:
            if (M[n] - M[i]) / (n - i) < left_max:
                left_max = (M[n] - M[i]) / (n - i)
                cnt += 1

    for i in range(n + 1, len(M)):
        if right_max == MAX:
            right_max = (M[n] - M[i]) / (n - i)
            cnt += 1
        else:
            if (M[i] - M[n]) / (i - n) > right_max:
                right_max = (M[i] - M[n]) / (i - n)
                cnt += 1
    return cnt


ans = 0
k = 0
for i in range(len(M)):
    ans = max(check(i), ans)
print(ans)
