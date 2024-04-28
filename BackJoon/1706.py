import sys

input = sys.stdin.readline

l, c = map(int, input().split())
arr = []

for _ in range(l):
    arr.append(input()[:-1])


words = []
for i in range(l):
    words += arr[i].split("#")

for i in range(c):
    word = ""
    for j in range(l):
        word += arr[j][i]
    words += word.split("#")

ans = []
for word in words:
    if len(word) > 1:
        ans.append(word)
ans.sort()
print(ans[0])
