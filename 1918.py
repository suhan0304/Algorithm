import sys
from collections import deque
from collections import Counter

input = sys.stdin.readline

s = input().strip()

q = deque()
oper = deque()

cnt = 0

q = deque()
before_c = ''
for c in s :
    if c in ['+','-','*','/','(',')'] :
        if c in ['*','/'] and before_c in ['+','-'] :
            temp = q.pop()
            q.append('(')
            q.append(temp)
        if c in ['+','-'] and before_c in ['*','/'] :
            q.append(')')
        before_c = c
    q.append(c)

for i in range(q.count('(') - q.count(')')) :
    q.append(')')

print(q)