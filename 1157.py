import sys
input = sys.stdin.readline

a = input().rstrip().lower()
fre = [0 for i in range(26)]
max_cnt = 0
ans = 0

for c in a :
    fre[ord(c)-ord('a')] += 1
    if fre[ord(c)-ord('a')] > max_cnt :
        max_cnt = fre[ord(c)-ord('a')]
        ans = c
    elif fre[ord(c)-ord('a')] == max_cnt :
        ans = '?'

print(ans.upper())


