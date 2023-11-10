import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(input().strip())
k = int(input())

max_cnt = 0

for i in range(n):
    zero = 0
    for n in arr[i]:
        if n == "0":
            zero += 1
    cnt = 0
    if zero <= k and zero % 2 == k % 2:
        for j in range(n):
            if arr[i] == arr[j]:
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
