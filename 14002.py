import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

ans = [[a[0]]]

ans_max = 1
ans_list = [a[0]]

for i in range(1, n):
    max_len = 1
    max_list = [a[i]]
    for j in range(i - 1, -1, -1):
        if ans[j][-1] < a[i]:
            if len(ans[j]) + 1 > max_len:
                max_list = ans[j] + [a[i]]
                max_len = len(max_list)
                if max_len > ans_max:
                    ans_max = max_len
                    ans_list = max_list
    ans.append(max_list)

print(ans_max)
print(*ans_list)
