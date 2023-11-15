import sys

input = sys.stdin.readline

s = input().strip()

ans = []
for i in range(len(s)):
    ans.append(s[i:])

ans.sort()

print("\n".join(ans))
