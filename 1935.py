import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

s = input().strip()

m = []
for _ in range(n) :
    m.append(int(input()))

q = deque()
ans = 0
for c in s :
    if c in ['+','-','*','/'] :
        n2 = q.pop()
        n1 = q.pop()
        ans = n1 + n2 if c=='+' else n1-n2 if c=='-' else n1*n2 if c=='*' else n1/n2
        q.append(ans)
    else :
         q.append(m[ord(c)-ord('A')])   

print("%.2f"%q.pop())