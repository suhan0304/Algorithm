import sys
input = sys.stdin.readline

cnt = [9, 9]

k = int(input().rstrip())

s = 0
i = 0
while s < k :
    s += cnt[i]
    i += 1
    if i == len(cnt) :
        cnt.append(cnt[i-1] * 10)

print(s)