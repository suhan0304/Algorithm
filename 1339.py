import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
strings = [input().rstrip() for _ in range(n)]
max_length = max(len(s) for s in strings)

padded_strings = [s.rjust(max_length) for s in strings]

cnt = [0 for _ in range(26)] 
for i in range(max_length) :
    for s in padded_strings :
        if s[i] != ' ' :
            cnt[ord(s[i])-ord('A')] += (10**(max_length - i-1))

cnt.sort(reverse=True)

ans = 0
for i in range(10) :
    ans += cnt[i] * (9-i)
print(ans)