import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

ans = [[a[0]]]

max_len = 1
for i in range(1, n):
    for j in range(len(ans)):
        if ans[j][-1] < a[i]:
            ans.append(ans[j] + [a[i]])
            if len(ans[-1]) > max_len:
                max_len = len(ans[-1])

print(max_len)
