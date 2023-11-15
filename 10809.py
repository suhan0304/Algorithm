import sys

input = sys.stdin.readline

s = input().strip()

a = [-1] * 26

for i in range(len(s)):
    a[ord(s[i]) - ord("a")] = (
        i if a[ord(s[i]) - ord("a")] == -1 else a[ord(s[i]) - ord("a")]
    )

print(*a)
