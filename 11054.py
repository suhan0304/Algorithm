import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

ans = [[a[0]]]

for i in range(1, n):
    max_len = 1
    li = [a[i]]
    for j in range(i):
        if ans[j][-1] < a[i] and max(ans[j]) < a[i]:
            if len(ans[j]) + 1 > max_len:
                li = ans[j] + [a[i]]
                max_len = len(li)
        if ans[j][-1] > a[i]:
            if len(ans[j]) + 1 > max_len:
                li = ans[j] + [a[i]]
                max_len = len(li)
    ans.append(li)

print(ans)
